#!/usr/bin/env python3
"""Deep static APK analysis using pinned JADX and Apktool releases.

The APK is treated as input data only. Decompiled source and extracted files stay
inside a temporary directory; only a summarized Markdown report is persisted.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
import zipfile
import zlib
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree

from apk_inputs import extract_xapk_member, github_api_headers, resolve_primary_apk, select_release_asset, get_release

USER_AGENT = "YuGiOh-Duel-Link-MOD-code-analysis/1.0"
JADX_VERSION = "1.5.6"
JADX_URL = "https://github.com/skylot/jadx/releases/download/v1.5.6/jadx-1.5.6.zip"
APKTOOL_VERSION = "3.0.3"
APKTOOL_URL = "https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar"
ANDROID_NS = "{http://schemas.android.com/apk/res/android}"
JAVA_TERMS = re.compile(
    r"autoplay|auto.?play|show.?monster|status.?details|reveal.?card|"
    r"damage|multiplier|multipli|cheat.?card|comcheatcard|duelgetdamagevalue",
    re.IGNORECASE,
)
RESOURCE_TERMS = re.compile(
    r"autoplay|auto.?play|show.?monster|status.?details|reveal.?card.?face|"
    r"damage.?multiplier|platinmods|g-bo",
    re.IGNORECASE,
)
NATIVE_TERMS = re.compile(
    r"Java_com_platinmods_|DLL_DuelGetDamageValue|DLL_DuelGetDamageSrcPosition|"
    r"DLL_DuelGetDamageDstPosition|DLL_DuelComCheatCard|autoplay|auto.?play|"
    r"show.?monster|reveal.?card|damage|multiplier|cheat.?card",
    re.IGNORECASE,
)
TRACE_PATTERNS = {
    "com/platinmods/FloatingModMenuService.java": re.compile(
        r"getFeatureList|settingsList|localChanges|changeFeature|loadPref|"
        r"inputFieldFeature|featureNum|featureName|setOnCheckedChangeListener",
        re.IGNORECASE,
    ),
    "com/platinmods/PMLauncher.java": re.compile(
        r"System\.loadLibrary|isGameLibLoaded|FloatingModMenuService|"
        r"startService|native|settingsList|getFeatureList",
        re.IGNORECASE,
    ),
    "com/platinmods/Preferences.java": re.compile(
        r"changeFeature|loadPref|savePref|Changes|SharedPreferences|native",
        re.IGNORECASE,
    ),
    "com/platinmods/MainActivity.java": re.compile(
        r"loadLibrary|isGameLibLoaded|FloatingModMenuService|Toast|native|service",
        re.IGNORECASE,
    ),
}
FOCUSED_BINARY_TERMS = re.compile(
    r"AutoPlay\s*Bot|Show\s*Monster(?:\s*&\s*Status\s*Details)?|"
    r"Reveal\s*Card\s*Face|CHEATCARD|PROCESS_DAMAGE[0-9]?|"
    r"DLL_DuelGetDamageValue|DLL_DuelComCheatCard|"
    r"Java_com_platinmods_(?:FloatingModMenuService_(?:getFeatureList|settingsList)|Preferences_Changes)",
    re.IGNORECASE,
)


def request_json(url: str) -> dict:
    request = urllib.request.Request(url, headers=github_api_headers())
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def archive_crc_status(archive: zipfile.ZipFile) -> tuple[str, str]:
    """Fully read each ZIP member and return an explicit CRC/decompression status."""
    try:
        bad_member = archive.testzip()
        if bad_member:
            return "FAIL", f"first failing entry: {bad_member}"
        return "PASS", "all archive entries passed"
    except (zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error, EOFError,
            OSError, RuntimeError, NotImplementedError) as error:
        return "FAIL", f"{type(error).__name__}: {error}"


def download(url: str, path: Path) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(request, timeout=180) as response, path.open("wb") as output:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            output.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    return size, digest.hexdigest()


def run_command(command: list[str], timeout: int) -> dict:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            errors="replace",
            timeout=timeout,
            check=False,
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "error": "",
        }
    except Exception as exc:
        return {
            "returncode": 127,
            "stdout": "",
            "stderr": "",
            "error": f"{type(exc).__name__}: {exc}",
        }


def scan_text_files(root: Path, limit: int = 100, pattern: re.Pattern = JAVA_TERMS) -> tuple[list[str], int]:
    hits: list[str] = []
    total = 0
    if not root.exists():
        return hits, total
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in (".java", ".xml", ".txt", ".json"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            if pattern.search(line):
                total += 1
                if len(hits) < limit:
                    try:
                        relative = path.relative_to(root)
                    except ValueError:
                        relative = path.name
                    snippet = " ".join(line.strip().split())
                    if len(snippet) > 200:
                        snippet = snippet[:197] + "..."
                    hits.append(f"- {relative}:{line_no}: {snippet}")
    return hits, total


def scan_binary_strings(data: bytes, limit: int = 20, pattern: re.Pattern = NATIVE_TERMS) -> tuple[list[str], int]:
    hits: list[str] = []
    total = 0
    seen: set[str] = set()
    for match in re.finditer(rb"[ -~]{4,}", data):
        value = match.group().decode("ascii", errors="ignore").strip()
        if value and pattern.search(value):
            total += 1
            if value not in seen and len(hits) < limit:
                seen.add(value)
                clipped = value if len(value) <= 220 else value[:217] + "..."
                hits.append(clipped)
    return hits, total


def extract_focused_binary_matches(data: bytes, limit: int = 80) -> tuple[list[str], int]:
    """Return short context windows around specific menu and duel-engine string clues."""
    output: list[str] = []
    seen: set[str] = set()
    total = 0
    for segment in re.finditer(rb"[ -~]{4,}", data):
        value = segment.group().decode("ascii", errors="ignore")
        for match in FOCUSED_BINARY_TERMS.finditer(value):
            total += 1
            start = max(0, match.start() - 60)
            end = min(len(value), match.end() + 60)
            snippet = " ".join(value[start:end].split())
            if snippet not in seen and len(output) < limit:
                seen.add(snippet)
                output.append(snippet[:220])
    return output, total


def scan_key_java_sources(root: Path, limit_per_file: int = 25) -> tuple[list[str], int]:
    """Capture relevant source lines from each Platinmods menu-framework class."""
    hits: list[str] = []
    total = 0
    if not root.exists():
        return hits, total

    for relative_name, pattern in TRACE_PATTERNS.items():
        path = root / relative_name
        if not path.is_file():
            hits.append(f"- {relative_name}: not produced by JADX.")
            continue
        try:
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError as exc:
            hits.append(f"- {relative_name}: could not read source ({type(exc).__name__}).")
            continue

        file_matches = 0
        file_match_total = 0
        for index, line in enumerate(lines):
            if not pattern.search(line):
                continue
            total += 1
            file_match_total += 1
            if file_matches >= limit_per_file:
                continue
            snippet = " ".join(line.strip().split())
            if len(snippet) > 240:
                snippet = snippet[:237] + "..."
            hits.append(f"- {relative_name}:{index + 1}: {snippet}")
            file_matches += 1
        hits.append(f"- {relative_name}: displayed {file_matches} of {file_match_total} matching source lines.")

    return hits, total


def decode_manifest(decoded_dir: Path) -> list[str]:
    manifest_path = decoded_dir / "AndroidManifest.xml"
    if not manifest_path.is_file():
        return ["- Apktool did not produce a decoded AndroidManifest.xml."]
    try:
        root = ElementTree.parse(manifest_path).getroot()
    except (ElementTree.ParseError, OSError) as exc:
        return [f"- Could not parse decoded AndroidManifest.xml: {type(exc).__name__}: {exc}"]
    package_name = root.get("package", "not decoded")
    uses_sdk = root.find("uses-sdk")
    min_sdk = uses_sdk.get(ANDROID_NS + "minSdkVersion", "not declared") if uses_sdk is not None else "not declared"
    target_sdk = uses_sdk.get(ANDROID_NS + "targetSdkVersion", "not declared") if uses_sdk is not None else "not declared"
    version_code = root.get(ANDROID_NS + "versionCode", "not declared")
    version_name = root.get(ANDROID_NS + "versionName", "not declared")
    lines = [
        f"- Package name: {package_name}",
        f"- Version name: {version_name}",
        f"- Version code: {version_code}",
        f"- minSdkVersion: {min_sdk}",
        f"- targetSdkVersion: {target_sdk}",
    ]
    application = root.find("application")
    if application is not None:
        lines.append(f"- Application class: {application.get(ANDROID_NS + 'name', 'not declared')}")
        lines.append(f"- Application label reference: {application.get(ANDROID_NS + 'label', 'not declared')}")
    permissions = []
    for node in list(root):
        if node.tag in ("uses-permission", "uses-permission-sdk-23", "uses-permission-sdk-m"):
            permission = node.get(ANDROID_NS + "name", "")
            if permission:
                permissions.append(permission)
    lines.append(f"- Declared permission entries: {len(permissions)}")
    lines.extend(f"  - {permission}" for permission in permissions[:50])
    component_tags = ("activity", "activity-alias", "service", "receiver", "provider")
    components = []
    if application is not None:
        for node in list(application):
            if node.tag not in component_tags:
                continue
            name = node.get(ANDROID_NS + "name", "(unnamed)")
            exported = node.get(ANDROID_NS + "exported", "unspecified")
            permission = node.get(ANDROID_NS + "permission", "")
            components.append((node.tag, name, exported, permission))
    lines.append(f"- Declared activity/service/receiver/provider entries: {len(components)}")
    for kind, name, exported, permission in components[:80]:
        suffix = f", permission={permission}" if permission else ""
        lines.append(f"  - {kind}: {name}, exported={exported}{suffix}")
    if len(components) > 80:
        lines.append(f"  - ... {len(components) - 80} more component entries not displayed")
    return lines


def summarize_android_entrypoint(source_root: Path, limit: int = 40) -> list[str]:
    """Summarize lifecycle, native bridge and view/window calls in the game Activity."""
    candidates = list(source_root.rglob("YgomMainActivity.java")) if source_root.exists() else []
    preferred = [
        path for path in candidates
        if "jp/konami/duellinks/plugins" in path.as_posix()
    ]
    candidate = preferred[0] if preferred else (candidates[0] if candidates else None)
    if candidate is None:
        return ["- YgomMainActivity.java was not present in the current JADX output."]

    try:
        source_lines = candidate.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as error:
        return [f"- Could not read {candidate.name}: {type(error).__name__}: {error}"]

    class_pattern = re.compile(r"^\s*(?:public\s+)?(?:abstract\s+|final\s+)?class\s+YgomMainActivity\b")
    method_pattern = re.compile(
        r"^\s*(?:public|protected|private)\s+(?:(?:static|final|synchronized|native)\s+)*"
        r"[\w.$<>?, \[\]]+\s+(\w+)\s*\("
    )
    relevant_pattern = re.compile(
        r"YgomMainActivity|\bonCreate\b|\bonStart\b|\bonResume\b|\bonPause\b|"
        r"\bonStop\b|\bonDestroy\b|\bonNewIntent\b|System\.loadLibrary|"
        r"\bloadLibrary\b|\bnative\b|UnityPlayer|WindowManager|"
        r"\baddContentView\b|\bsetContentView\b|\bstartService\b|"
        r"\bgetWindow\b|\brequestWindowFeature\b|\bdispatchKeyEvent\b|"
        r"\bonActivityResult\b|\bWebView\b",
        re.IGNORECASE,
    )
    lifecycle = {"onCreate", "onStart", "onResume", "onPause", "onStop", "onDestroy",
                 "onNewIntent", "onActivityResult", "dispatchKeyEvent"}
    selected: list[tuple[int, str]] = []
    for index, line in enumerate(source_lines, start=1):
        stripped = line.strip()
        method_match = method_pattern.match(line)
        method_name = method_match.group(1) if method_match else ""
        if class_pattern.match(line) or method_name in lifecycle or relevant_pattern.search(line):
            compact = re.sub(r"\s+", " ", stripped)
            if len(compact) > 260:
                compact = compact[:257] + "..."
            selected.append((index, compact))
    if not selected:
        return [f"- {candidate.relative_to(source_root).as_posix()} was found but no Activity lifecycle/native/window markers matched."]
    output = [f"- Source: {candidate.relative_to(source_root).as_posix()} ({len(source_lines)} lines)."]
    output.extend(
        f"- L{number}: {line}"
        for number, line in selected[:limit]
    )
    if len(selected) > limit:
        output.append(f"- Truncated: {len(selected) - limit} additional matching lines were not included.")
    return output


def summarize_java_packages(source_root: Path, java_sources: list[Path]) -> list[str]:
    package_counts: Counter[str] = Counter()
    app_classes: list[str] = []
    mod_menu_classes: list[str] = []
    for path in java_sources:
        try:
            relative = path.relative_to(source_root).as_posix()
        except ValueError:
            relative = path.name
        parts = relative.split("/")
        package = ".".join(parts[: min(3, max(1, len(parts) - 1))]) if len(parts) > 1 else "(default package)"
        package_counts[package] += 1
        if relative.startswith("jp/konami/duellinks/"):
            app_classes.append(relative)
        if relative.startswith("com/platinmods/"):
            mod_menu_classes.append(relative)
    lines = [
        "## Decompiled class namespace summary",
        f"- Decompiled class files found: {len(java_sources)}",
        f"- Classes under jp/konami/duellinks/: {len(app_classes)}",
        f"- Classes under com/platinmods/: {len(mod_menu_classes)}",
        "- Top package-prefix counts:",
    ]
    lines.extend(f"  - {package}: {count}" for package, count in package_counts.most_common(20))
    lines.append("- Sample classes under jp/konami/duellinks/:")
    lines.extend(f"  - {name}" for name in sorted(app_classes)[:40] or ["(none found)"])
    lines.append("- Classes under com/platinmods/:")
    lines.extend(f"  - {name}" for name in sorted(mod_menu_classes)[:40] or ["(none found)"])
    return lines


def indented_excerpt(text: str, max_lines: int = 24) -> list[str]:
    chosen = (text or "(no output)").splitlines()[-max_lines:]
    return ["    " + line[:220] for line in chosen]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-tag", required=True)
    parser.add_argument(
        "--repo",
        default=os.environ.get("GITHUB_REPOSITORY", "TenzoNkz/YuGiOh-Duel-Link-MOD"),
    )
    parser.add_argument("--output", default="APK_CODE_ANALYSIS.md")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,100}", args.release_tag):
        parser.error("release tag contains unsupported characters")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("repository must be in owner/name form")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    base_lines = [
        "# APK Code Analysis Report",
        "",
        f"**Generated:** {generated}",
        "**Method:** JADX/Apktool static analysis; the APK was not installed or executed.",
        f"- Repository: {args.repo}",
        f"- Requested release tag: {args.release_tag}",
        f"- JADX pinned version: {JADX_VERSION}",
        f"- Apktool pinned version: {APKTOOL_VERSION}",
        "",
    ]

    try:
        release = get_release(args.repo, args.release_tag)
        asset = select_release_asset(release)
        expected_digest = asset.get("digest") or ""
        expected_sha = expected_digest.split(":", 1)[1] if expected_digest.startswith("sha256:") else ""

        with tempfile.TemporaryDirectory(prefix="apk-code-analysis-") as temporary:
            work = Path(temporary)
            asset_name = str(asset.get("name", "(unnamed)"))
            suffix = ".xapk" if asset_name.lower().endswith(".xapk") else ".apk"
            container_path = work / ("source-container" + suffix)
            actual_size, actual_sha = download(asset["browser_download_url"], container_path)
            apk_path = container_path
            embedded_apk_name = asset_name
            nested_apks = []
            obb_names = []
            selected_container_crc = "NOT_APPLICABLE"
            analysis_apks: list[dict] = []
            if suffix == ".xapk":
                apk_path, embedded_apk_name, nested_apks, obb_names = resolve_primary_apk(
                    container_path, asset_name, work / "source-primary.apk"
                )
                selected_member = next((item for item in nested_apks if item["name"] == embedded_apk_name), {})
                selected_container_crc = selected_member.get("container_crc_status", "NOT_CHECKED")
                # Keep the base APK and every ABI/config split separate. This is
                # inventory only: no split contents are merged or treated as
                # proof that the selected main APK can be installed by itself.
                for split_index, member in enumerate(nested_apks, start=1):
                    if member["name"] == embedded_apk_name:
                        analysis_apks.append({
                            "name": member["name"],
                            "path": apk_path,
                            "is_primary": True,
                            "container_crc_status": selected_container_crc,
                            "size": member["size"],
                        })
                        continue
                    member_path = work / f"xapk-split-{split_index}.apk"
                    try:
                        extracted = extract_xapk_member(container_path, member["name"], member_path)
                        nested_apks = [
                            extracted if current["name"] == member["name"] else current
                            for current in nested_apks
                        ]
                        analysis_apks.append({
                            "name": extracted["name"],
                            "path": member_path,
                            "is_primary": False,
                            "container_crc_status": extracted["container_crc_status"],
                            "size": extracted["size"],
                        })
                    except Exception as split_error:
                        nested_apks = [
                            {**current, "analysis_error": f"{type(split_error).__name__}: {split_error}"}
                            if current["name"] == member["name"] else current
                            for current in nested_apks
                        ]
                if not analysis_apks:
                    raise RuntimeError("No APK member could be extracted from the XAPK")
            else:
                analysis_apks.append({
                    "name": asset_name,
                    "path": apk_path,
                    "is_primary": True,
                    "container_crc_status": "NOT_APPLICABLE",
                    "size": apk_path.stat().st_size,
                })
            digest_matches = actual_sha.lower() == expected_sha.lower() if expected_sha else None

            base_lines.extend([
                "## Source Release and integrity",
                f"- Release page: {release.get('html_url', '(not supplied)')}",
                f"- Release tag: {release.get('tag_name', args.release_tag)}",
                f"- Release asset: {asset_name}",
                f"- GitHub-reported size: {asset.get('size', 'unknown')} bytes",
                f"- Downloaded container size: {actual_size} bytes",
                f"- Expected container SHA-256: {expected_sha or 'not provided'}",
                f"- Calculated container SHA-256: {actual_sha}",
                f"- Container digest comparison: {'PASS' if digest_matches is True else 'FAIL' if digest_matches is False else 'NOT_AVAILABLE'}",
                f"- Package input type: {'XAPK' if suffix == '.xapk' else 'APK'}",
                f"- APK selected for code analysis: {embedded_apk_name}",
                f"- Selected APK size: {apk_path.stat().st_size} bytes",
                f"- Embedded APK members: {len(nested_apks)}",
                *([f"- Embedded APK member: {item['name']} ({item['size']} bytes); outer CRC: {item.get('container_crc_status', 'NOT_SELECTED')}; scan: {'EXTRACTED' if any(p['name'] == item['name'] for p in analysis_apks) else item.get('analysis_error', 'NOT_EXTRACTED')}" for item in nested_apks] or ["- No nested APK members; analyzing the Release asset directly."]),
                f"- Embedded APKs extracted for static inventory: {len(analysis_apks)}",
                f"- OBB members in XAPK: {len(obb_names)}",
                *([f"- OBB member: {name}" for name in obb_names[:20]] or ["- No OBB member detected."]),
                f"- Selected APK member CRC in outer XAPK: {selected_container_crc}",
                "",
            ])
            if digest_matches is False:
                base_lines.extend([
                    "**Status:** INTEGRITY_FAILURE",
                    "",
                    "The downloaded asset did not match GitHub's reported SHA-256. Decompilation was skipped.",
                ])
                output_path.write_text("\n".join(base_lines) + "\n", encoding="utf-8")
                return 2

            tool_dir = work / "tools"
            tool_dir.mkdir()
            jadx_zip = tool_dir / "jadx.zip"
            apktool_jar = tool_dir / "apktool.jar"
            download(JADX_URL, jadx_zip)
            download(APKTOOL_URL, apktool_jar)

            jadx_root = tool_dir / "jadx"
            jadx_root.mkdir()
            with zipfile.ZipFile(jadx_zip, "r") as archive:
                root_resolved = jadx_root.resolve()
                for item in archive.infolist():
                    target = (jadx_root / item.filename).resolve()
                    if target != root_resolved and root_resolved not in target.parents:
                        raise RuntimeError("JADX archive contains a path outside its extraction directory")
                archive.extractall(jadx_root)
            jadx_bins = [path for path in jadx_root.rglob("jadx") if path.is_file() and "bin" in path.parts]
            if not jadx_bins:
                raise RuntimeError("Could not locate the JADX CLI in the downloaded distribution")
            jadx_bin = jadx_bins[0]
            jadx_bin.chmod(jadx_bin.stat().st_mode | 0o111)

            apktool_out = work / "apktool-decoded"
            jadx_out = work / "jadx-decoded"
            apktool_result = run_command(
                ["java", "-jar", str(apktool_jar), "d", "-f", "-o", str(apktool_out), str(apk_path)],
                timeout=900,
            )
            jadx_result = run_command(
                [str(jadx_bin), "--show-bad-code", "-d", str(jadx_out), str(apk_path)],
                timeout=1200,
            )

            manifest_lines = decode_manifest(apktool_out)
            java_sources = list(jadx_out.rglob("*.java")) if jadx_out.exists() else []
            decoded_resources = list(apktool_out.rglob("*")) if apktool_out.exists() else []
            source_root = jadx_out / "sources"
            if not source_root.exists():
                source_root = jadx_out
            source_hits, source_hit_count = scan_text_files(source_root, limit=100)
            key_source_hits, key_source_hit_count = scan_key_java_sources(source_root, limit_per_file=25)
            resource_hits, resource_hit_count = scan_text_files(apktool_out / "res", limit=40, pattern=RESOURCE_TERMS)
            package_summary_lines = summarize_java_packages(source_root, java_sources)
            entrypoint_lines = summarize_android_entrypoint(source_root)

            native_hits: list[str] = []
            native_hit_count = 0
            focused_native_hits: list[str] = []
            focused_native_count = 0
            inventory: list[str] = []
            split_inventory: list[str] = []
            split_read_errors: list[str] = []
            inner_crc_failures = False
            for package_item in analysis_apks:
                package_path = package_item["path"]
                package_name = package_item["name"]
                try:
                    with zipfile.ZipFile(package_path, "r") as archive:
                        names = archive.namelist()
                        inner_crc, inner_crc_detail = archive_crc_status(archive)
                        if inner_crc != "PASS":
                            inner_crc_failures = True
                            split_read_errors.append(
                                f"- Package {package_name}: inner ZIP CRC/decompression scan {inner_crc} ({inner_crc_detail})"
                            )
                        so_names = sorted(name for name in names if name.endswith(".so"))
                        metadata_names = sorted(name for name in names if name.endswith("global-metadata.dat"))
                        split_inventory.append(
                            f"- {package_name} ({'primary APK' if package_item['is_primary'] else 'config/split APK'}): "
                            f"{len(names)} entries, {len(so_names)} native libraries, "
                            f"{len(metadata_names)} IL2CPP metadata file(s), "
                            f"outer XAPK CRC={package_item['container_crc_status']}, inner ZIP CRC={inner_crc}"
                            + (f" ({inner_crc_detail})" if inner_crc != "PASS" else "")
                            + "."
                        )
                        if not package_item["is_primary"]:
                            for split_name in sorted(name for name in names if name.endswith((".so", "global-metadata.dat"))):
                                split_info = archive.getinfo(split_name)
                                inventory.append(f"- [{package_name}] {split_name}: {split_info.file_size} bytes")
                        wanted = [
                            name for name in names
                            if name.endswith((".so", "global-metadata.dat"))
                            and (
                                "libplatinmods.so" in name
                                or "libduel.so" in name
                                or "libil2cpp.so" in name
                                or "libunity.so" in name
                                or name.endswith("global-metadata.dat")
                            )
                        ]
                        for name in wanted:
                            info = archive.getinfo(name)
                            label = f"[{package_name}] {name}"
                            if package_item["is_primary"]:
                                inventory.append(f"- {name}: {info.file_size} bytes")
                            try:
                                native_bytes = archive.read(name)
                            except (zipfile.BadZipFile, zlib.error, EOFError, OSError, RuntimeError, NotImplementedError) as entry_error:
                                split_read_errors.append(f"- {label}: read failed ({type(entry_error).__name__}: {entry_error})")
                                continue
                            matches, count = scan_binary_strings(native_bytes, limit=20, pattern=NATIVE_TERMS)
                            native_hit_count += count
                            if matches:
                                native_hits.append(f"### {label}")
                                native_hits.extend(f"- {value}" for value in matches)
                            focused, focused_count = extract_focused_binary_matches(native_bytes, limit=50)
                            focused_native_count += focused_count
                            if focused:
                                focused_native_hits.append(f"### {label}")
                                focused_native_hits.extend(f"- {value}" for value in focused)
                except (zipfile.BadZipFile, zlib.error, EOFError, OSError, RuntimeError, NotImplementedError) as package_error:
                    split_read_errors.append(
                        f"- Package {package_name}: inventory failed ({type(package_error).__name__}: {package_error})"
                    )

            combined_jadx_output = (jadx_result.get("stdout", "") or "") + "\n" + (jadx_result.get("stderr", "") or "")
            error_match = re.search(r"finished with errors, count: *([0-9]+)", combined_jadx_output, re.IGNORECASE)
            jadx_error_count = int(error_match.group(1)) if error_match else 0
            status = "CODE_ANALYSIS_COMPLETE"
            any_split_crc_failure = any(item.get("container_crc_status") == "FAIL" for item in nested_apks)
            if (
                apktool_result["returncode"] != 0
                or jadx_result["returncode"] != 0
                or selected_container_crc == "FAIL"
                or any_split_crc_failure
                or inner_crc_failures
                or split_read_errors
            ):
                status = "CODE_ANALYSIS_PARTIAL"

            base_lines.extend([
                f"**Status:** {status}",
                "",
                "## Android manifest (decoded by Apktool)",
                *manifest_lines,
                "",
                "## Tool execution",
                f"- Apktool exit code: {apktool_result['returncode']}",
                f"- JADX exit code: {jadx_result['returncode']}",
                f"- JADX-reported decompiler error count: {jadx_error_count}",
                f"- Decompiled Java source files found: {len(java_sources)}",
                f"- Decoded Apktool output entries: {len(decoded_resources)}",
                "",
                "### Apktool output excerpt",
                *indented_excerpt(apktool_result.get("stderr", "") or apktool_result.get("stdout", "")),
                "",
                "### JADX output excerpt",
                *indented_excerpt(jadx_result.get("stderr", "") or jadx_result.get("stdout", "")),
                "",
                *package_summary_lines,
                "",
                "## Android Activity entry-point trace",
                *entrypoint_lines,
                "",
                "## APK split inventory",
                *(split_inventory or ["- No APK members were successfully inventoried."]),
                "",
                "## Native/IL2CPP inventory across readable APK members",
                *(inventory or ["- No targeted native libraries/metadata were read successfully."]),
                "",
                "## APK/split read warnings",
                *(split_read_errors or ["- Full inner ZIP CRC/decompression scans passed for every extracted APK member."]),
                "",
                "## Search hits in decompiled Java",
                f"- Matching lines found: {source_hit_count}; displaying up to {len(source_hits)}.",
                *(source_hits or ["- No matching term was found in the scanned Java source."]),
                "",
                "## Known reference menu-framework paths checked in APKPure DEX",
                f"- Matching source lines found: {key_source_hit_count}; displaying context for up to {len(key_source_hits)} lines.",
                *(key_source_hits or ["- No known reference menu-framework class was present in the selected Java source output."]),
                "",
                "## Search hits in decoded resources",
                f"- Matching lines found: {resource_hit_count}; displaying up to {len(resource_hits)}.",
                *(resource_hits or ["- No matching term was found in the scanned decoded resource XML/text."]),
                "",
                "## Focused strings: feature labels, menu callbacks, and duel damage",
                f"- Focused string matches found: {focused_native_count}.",
                *(focused_native_hits or ["- No focused string match was found in selected native/IL2CPP files."]),
                "",
                "## Search hits in selected native/IL2CPP strings",
                f"- Total matching printable strings: {native_hit_count}.",
                *(native_hits or ["- No matching printable strings were found in the selected native files."]),
                "",
                "## Interpretation guardrails",
                "- Exact string hits locate potential code/resources; they do not prove event wiring, control flow, or that a menu toggle works.",
                "- JADX primarily analyzes DEX/Java/Kotlin code. Unity IL2CPP game logic may be compiled into native libraries and metadata; full native tracing requires separate tooling and careful symbol/metadata analysis.",
                "- Static decompilation does not prove server-authoritative behavior, online compatibility, or runtime success.",
                "- The APK was not executed or installed. Temporary decompiled source was not committed to the repository.",
                "- For XAPK input, JADX/Apktool decompile the selected primary APK; native-library and metadata inventory also scans other readable split APKs. Split payloads are not merged or proven installable as a single APK.",
                "- The outer XAPK member CRC is reported separately from the selected APK's own ZIP structure. A failed outer CRC must be investigated and prevents treating the source container as clean, even if static analysis can read the inner APK bytes.",
                "",
                "## Recommended next step",
                "Review the source/resource/native-string hits together with the decompiled manifest. Record exact file/class/method evidence for each feature in MOD_CANDIDATES.md, then separate code-reading hypotheses from any isolated test results.",
                "",
            ])
            output_path.write_text("\n".join(base_lines) + "\n", encoding="utf-8")
            print(f"Wrote {output_path} with status {status}")
            if apktool_result["returncode"] != 0 or (jadx_result["returncode"] != 0 and not java_sources):
                print(f"Critical tool error: Apktool exit={apktool_result['returncode']}; JADX exit={jadx_result['returncode']}", file=sys.stderr)
                return 2
            if jadx_result["returncode"] != 0:
                print("JADX emitted partial output with decompiler errors; see the report for its error count.", file=sys.stderr)
            return 0

    except Exception as error:
        base_lines.extend([
            "**Status:** CODE_ANALYSIS_FAILED",
            "",
            f"- Error: {type(error).__name__}: {error}",
            "",
            "Static decompilation did not finish. Inspect the workflow logs, fix the reported issue, and rerun.",
            "",
        ])
        output_path.write_text("\n".join(base_lines) + "\n", encoding="utf-8")
        print(f"Code analysis failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
