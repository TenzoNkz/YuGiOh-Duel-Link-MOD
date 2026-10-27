#!/usr/bin/env python3
"""Deep static APK analysis using pinned JADX and Apktool releases.

The APK is treated as input data only. Decompiled source and extracted files stay
inside a temporary directory; only a summarized Markdown report is persisted.
"""
from __future__ import annotations

import argparse
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
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree

from apk_inputs import resolve_primary_apk, select_release_asset, get_release

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
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": USER_AGENT,
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


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
    uses_sdk = root.find("uses-sdk")
    min_sdk = uses_sdk.get(ANDROID_NS + "minSdkVersion", "not declared") if uses_sdk is not None else "not declared"
    target_sdk = uses_sdk.get(ANDROID_NS + "targetSdkVersion", "not declared") if uses_sdk is not None else "not declared"
    version_code = root.get(ANDROID_NS + "versionCode", "not declared")
    version_name = root.get(ANDROID_NS + "versionName", "not declared")
    return [
        f"- Package name: {root.get('package', 'not decoded')}",
        f"- Version name: {version_name}",
        f"- Version code: {version_code}",
        f"- minSdkVersion: {min_sdk}",
        f"- targetSdkVersion: {target_sdk}",
    ]


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
            if suffix == ".xapk":
                apk_path, embedded_apk_name, nested_apks, obb_names = resolve_primary_apk(
                    container_path, asset_name, work / "source-primary.apk"
                )
                selected_member = next((item for item in nested_apks if item["name"] == embedded_apk_name), {})
                selected_container_crc = selected_member.get("container_crc_status", "NOT_CHECKED")
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
                *([f"- Embedded APK member: {item['name']} ({item['size']} bytes)" for item in nested_apks] or ["- No nested APK members; analyzing the Release asset directly."]),
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

            native_hits: list[str] = []
            native_hit_count = 0
            focused_native_hits: list[str] = []
            focused_native_count = 0
            inventory: list[str] = []
            with zipfile.ZipFile(apk_path, "r") as archive:
                names = archive.namelist()
                wanted = [
                    name for name in names
                    if name.endswith((".so", "global-metadata.dat"))
                    and (
                        "libplatinmods.so" in name
                        or "libduel.so" in name
                        or "libil2cpp.so" in name
                        or name.endswith("global-metadata.dat")
                    )
                ]
                for name in wanted:
                    info = archive.getinfo(name)
                    inventory.append(f"- {name}: {info.file_size} bytes")
                    native_bytes = archive.read(name)
                    matches, count = scan_binary_strings(native_bytes, limit=20, pattern=NATIVE_TERMS)
                    native_hit_count += count
                    if matches:
                        native_hits.append(f"### {name}")
                        native_hits.extend(f"- {value}" for value in matches)
                    focused, focused_count = extract_focused_binary_matches(native_bytes, limit=50)
                    focused_native_count += focused_count
                    if focused:
                        focused_native_hits.append(f"### {name}")
                        focused_native_hits.extend(f"- {value}" for value in focused)

            combined_jadx_output = (jadx_result.get("stdout", "") or "") + "\n" + (jadx_result.get("stderr", "") or "")
            error_match = re.search(r"finished with errors, count: *([0-9]+)", combined_jadx_output, re.IGNORECASE)
            jadx_error_count = int(error_match.group(1)) if error_match else 0
            status = "CODE_ANALYSIS_COMPLETE"
            if apktool_result["returncode"] != 0 or jadx_result["returncode"] != 0 or selected_container_crc == "FAIL":
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
                "## Selected native/IL2CPP inventory",
                *(inventory or ["- No target native libraries/metadata were found in the APK ZIP listing."]),
                "",
                "## Search hits in decompiled Java",
                f"- Matching lines found: {source_hit_count}; displaying up to {len(source_hits)}.",
                *(source_hits or ["- No matching term was found in the scanned Java source."]),
                "",
                "## Key Platinmods menu-framework source references",
                f"- Matching source lines found: {key_source_hit_count}; displaying context for up to {len(key_source_hits)} lines.",
                *(key_source_hits or ["- No target menu-framework references were found in the selected Java classes."]),
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
                "- For XAPK input, JADX/Apktool analyze the selected primary APK only; any split APKs and OBB payloads require separate compatibility/integration checks before producing a single installable APK.",
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
