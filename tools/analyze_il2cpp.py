#!/usr/bin/env python3
"""Run pinned Il2CppDumper on APKPure's ARM64 IL2CPP library and metadata.

The XAPK is treated as data. The tool extracts only the primary APK and the
named ABI split to temporary paths, runs the dumper in that temporary workspace,
and persists only a concise report. No app is installed or executed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
import zlib
from datetime import datetime, timezone
from pathlib import Path

from apk_inputs import download_and_hash, extract_xapk_member, get_release, resolve_primary_apk, select_release_asset

DUMPER_VERSION = "6.7.46"
DUMPER_URL = "https://github.com/Perfare/Il2CppDumper/releases/download/v6.7.46/Il2CppDumper-net6-v6.7.46.zip"
USER_AGENT = "YuGiOh-Duel-Link-MOD-il2cpp-analysis/1.0"
METADATA_PATH = "assets/bin/Data/Managed/Metadata/global-metadata.dat"
ARM64_IL2CPP_PATH = "lib/arm64-v8a/libil2cpp.so"
FOCUSED_TERM_GROUPS = {
    "ShowMonster": re.compile(r"ShowMonster|showMonster", re.IGNORECASE),
    "Reveal Card": re.compile(r"RevealCard|Reveal_Card|CardFace|ShowCardFace", re.IGNORECASE),
    "CHEATCARD": re.compile(r"\bCHEATCARD\b|DuelComCheatCard", re.IGNORECASE),
    "PROCESS_DAMAGE": re.compile(r"\bPROCESS_DAMAGE[0-9]*\b", re.IGNORECASE),
    "Damage getter": re.compile(r"DLL_DuelGetDamageValue|DuelGetDamageValue", re.IGNORECASE),
    "Damage positions": re.compile(r"DamageSrcPosition|DamageDstPosition", re.IGNORECASE),
    "AutoPlay": re.compile(r"AutoPlay|autoPlay|GetAutoPlay|SetAutoPlay|ChangeAutoPlay", re.IGNORECASE),
    "Monster/status": re.compile(r"MonsterStatus|StatusDetails|ShowMonster", re.IGNORECASE),
}
CLASS_DECLARATION = re.compile(r"^\s*(?:public|private|internal|protected|abstract|sealed|static|partial|enum|struct|class|interface|\[)", re.IGNORECASE)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download_file(url: str, output: Path) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(request, timeout=180) as response, output.open("wb") as stream:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            stream.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    return size, digest.hexdigest()


def safe_extract_zip(zip_path: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "r") as archive:
        root = destination.resolve()
        for member in archive.infolist():
            path = (destination / member.filename).resolve()
            if path != root and root not in path.parents:
                raise RuntimeError(f"Tool ZIP contains a path outside extraction directory: {member.filename}")
        archive.extractall(destination)


def get_member_bytes(apk_path: Path, member_name: str) -> bytes:
    with zipfile.ZipFile(apk_path, "r") as archive:
        member = archive.getinfo(member_name)
        return archive.read(member)


def focused_dump_hits(dump_path: Path, limit_per_group: int = 3) -> tuple[list[str], dict[str, int]]:
    """Summarize useful symbol neighborhoods without letting generic AutoPlay hits dominate."""
    if not dump_path.is_file():
        return [], {}
    lines = dump_path.read_text(encoding="utf-8", errors="replace").splitlines()
    output: list[str] = []
    counts: dict[str, int] = {}
    emitted: set[int] = set()

    for group, pattern in FOCUSED_TERM_GROUPS.items():
        matches = [index for index, line in enumerate(lines) if pattern.search(line)]
        counts[group] = len(matches)
        if not matches:
            output.append(f"- {group}: 0 matching dump.cs lines.")
            continue
        output.append(f"- {group}: {len(matches)} matching dump.cs line(s); showing up to {limit_per_group} context(s).")
        selected = matches[:limit_per_group]
        for index in selected:
            # Include the nearest enclosing class/struct/enum declaration when possible.
            declaration = None
            for previous in range(index, max(-1, index - 250), -1):
                line = lines[previous]
                if re.search(r"^\s*(?:public|private|internal|protected).*\b(class|struct|enum|interface)\b", line):
                    declaration = previous
                    break
            context_indices = set(range(max(0, index - 1), min(len(lines), index + 2)))
            if declaration is not None:
                context_indices.add(declaration)
            for context_index in sorted(context_indices):
                if context_index in emitted or len(output) >= 100:
                    continue
                emitted.add(context_index)
                marker = "MATCH" if context_index == index else "CONTEXT"
                output.append(
                    f"  - [{marker}] dump.cs:{context_index + 1}: {lines[context_index].strip()[:260]}"
                )
    return output, counts

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", "TenzoNkz/YuGiOh-Duel-Link-MOD"))
    parser.add_argument("--release-tag", default="APKPure_Latest", help="APKPure Original source Release only")
    parser.add_argument("--output", default="IL2CPP_ANALYSIS_REPORT.md")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,100}", args.release_tag):
        parser.error("release tag contains unsupported characters")
    if args.release_tag != "APKPure_Latest":
        parser.error("This analysis stage intentionally accepts APKPure_Latest only")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# APKPure IL2CPP Analysis",
        "",
        f"**Generated:** {generated}",
        f"**Tool:** Perfare Il2CppDumper {DUMPER_VERSION}",
        "**Source rule:** APKPure Original is the input; Platinmods is not used by this stage.",
        "**Method:** extracts read-only binary inputs to a temporary workspace and runs static metadata recovery. No APK is installed or executed.",
        "",
    ]

    try:
        release = get_release(args.repo, args.release_tag)
        asset = select_release_asset(release)
        if not str(asset.get("name", "")).lower().endswith(".xapk"):
            raise RuntimeError("Expected APKPure XAPK asset; the Release asset is not an XAPK")
        with tempfile.TemporaryDirectory(prefix="apkpure-il2cpp-") as temporary:
            work = Path(temporary)
            xapk_path = work / "source.xapk"
            container_size, container_sha = download_file(str(asset["browser_download_url"]), xapk_path)
            expected = str(asset.get("digest") or "")
            expected_sha = expected.split(":", 1)[1] if expected.startswith("sha256:") else ""
            container_matches = container_sha.lower() == expected_sha.lower() if expected_sha else None

            primary_path, primary_name, inner_members, _obb_names = resolve_primary_apk(
                xapk_path, str(asset["name"]), work / "primary.apk"
            )
            split_meta = next((item for item in inner_members if "config.arm64_v8a.apk" in item["name"]), None)
            if split_meta is None:
                raise RuntimeError("Could not locate config.arm64_v8a.apk in APKPure XAPK")
            split_info = extract_xapk_member(xapk_path, split_meta["name"], work / "arm64-split.apk")
            metadata = get_member_bytes(primary_path, METADATA_PATH)
            library = get_member_bytes(work / "arm64-split.apk", ARM64_IL2CPP_PATH)
            metadata_path = work / "global-metadata.dat"
            library_path = work / "libil2cpp.so"
            metadata_path.write_bytes(metadata)
            library_path.write_bytes(library)

            tool_zip = work / "il2cppdumper.zip"
            tool_size, tool_sha = download_file(DUMPER_URL, tool_zip)
            tool_dir = work / "tool"
            safe_extract_zip(tool_zip, tool_dir)
            dumper_candidates = list(tool_dir.rglob("Il2CppDumper.dll"))
            if not dumper_candidates:
                raise RuntimeError("Pinned Il2CppDumper archive did not contain Il2CppDumper.dll")
            dumper_dll = dumper_candidates[0]
            output_dir = work / "dump-output"
            output_dir.mkdir()
            command = ["dotnet", str(dumper_dll), str(library_path), str(metadata_path), str(output_dir)]
            result = subprocess.run(
                command, input="1\n", capture_output=True, text=True,
                errors="replace", timeout=900, check=False,
            )
            log = (result.stdout or "") + "\n" + (result.stderr or "")
            dump_path = next(iter(output_dir.rglob("dump.cs")), None)
            script_path = next(iter(output_dir.rglob("script.json")), None)
            string_path = next(iter(output_dir.rglob("stringliteral.json")), None)
            focused_hits, focused_counts = focused_dump_hits(dump_path) if dump_path else ([], {})
            focused_count = sum(focused_counts.values())

            selected_outer_crc = next(
                (item.get("container_crc_status", "NOT_CHECKED") for item in inner_members if item["name"] == primary_name),
                "NOT_CHECKED",
            )
            lines.extend([
                "## Source integrity",
                f"- Release: {release.get('html_url', '(not provided)')}",
                f"- Tag: {args.release_tag}",
                f"- XAPK asset: {asset.get('name')}",
                f"- Container size: {container_size} bytes",
                f"- GitHub expected SHA-256: {expected_sha or 'not provided'}",
                f"- Calculated container SHA-256: {container_sha}",
                f"- Container digest match: {container_matches if container_matches is not None else 'NOT_PROVIDED'}",
                f"- Primary APK member: {primary_name}",
                f"- Primary APK outer CRC: {selected_outer_crc}",
                f"- ARM64 split member: {split_info['name']}",
                f"- ARM64 split outer CRC: {split_info['container_crc_status']}",
                f"- ARM64 libil2cpp.so size: {len(library)} bytes",
                f"- ARM64 libil2cpp.so SHA-256: {sha256_bytes(library)}",
                f"- global-metadata.dat size: {len(metadata)} bytes",
                f"- global-metadata.dat SHA-256: {sha256_bytes(metadata)}",
                f"- Dumper archive: {DUMPER_URL}",
                f"- Dumper archive size: {tool_size} bytes",
                f"- Dumper archive SHA-256: {tool_sha}",
                "",
                "## Il2CppDumper result",
                f"- Exit code: {result.returncode}",
                f"- dump.cs generated: {'YES' if dump_path else 'NO'}",
                f"- script.json generated: {'YES' if script_path else 'NO'}",
                f"- stringliteral.json generated: {'YES' if string_path else 'NO'}",
                f"- Focused dump.cs match lines: {focused_count}",
                "- Match count by term group:",
                *[f"  - {group}: {count}" for group, count in focused_counts.items()],
                "",
                "### Focused type/method context",
                *(focused_hits or ["- No focused method/type name was recovered by the current dump."]),
                "",
                "### Dumper log excerpt",
                *["    " + item[:240] for item in log.splitlines()[-30:]],
                "",
                "## Interpretation",
                "- Method names/type declarations recovered by Il2CppDumper are static metadata evidence; they do not prove a menu callback invokes the method or that behavior works at runtime.",
                "- The APKPure XAPK and selected entries have reported CRC/decompression problems. Even successful metadata extraction does not clear those integrity warnings.",
                "- Native library and metadata outputs are temporary; only this summary report is persisted.",
                "",
            ])
            outputs_generated = bool(dump_path and script_path and string_path)
            generated_output_marker = "Generate dummy dll" in log and "Dumping..." in log
            post_dump_console_error = (
                result.returncode != 0
                and outputs_generated
                and generated_output_marker
                and ("Console.ReadKey" in log or "Press any key to exit" in log)
            )
            if result.returncode == 0 and outputs_generated:
                status = "IL2CPP_DUMP_COMPLETE"
            elif outputs_generated and generated_output_marker:
                status = "IL2CPP_OUTPUTS_GENERATED_WITH_POST_DUMP_CONSOLE_ERROR" if post_dump_console_error else "IL2CPP_OUTPUTS_GENERATED_WITH_TOOL_WARNING"
            else:
                status = "IL2CPP_DUMP_PARTIAL"
            lines.extend([
                f"- Output generation confirmed from log: {'YES' if generated_output_marker else 'NO'}",
                f"- Final console-input exception after generation: {'YES' if post_dump_console_error else 'NO'}",
            ])
            if post_dump_console_error:
                lines.append("- Interpretation of non-zero exit: the dumper generated all three output files, then failed in its final Console.ReadKey prompt because stdin was redirected; this is not a clean exit, but the generated dump outputs are present.")
            lines.insert(3, f"**Status:** {status}")
            output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"Wrote {output_path} with status {status}")
            return 0 if outputs_generated and generated_output_marker else 2
    except (urllib.error.URLError, TimeoutError, OSError, RuntimeError, ValueError, json.JSONDecodeError,
            zipfile.BadZipFile, zipfile.LargeZipFile, KeyError, subprocess.SubprocessError, zlib.error) as error:
        lines.extend([
            "**Status:** IL2CPP_DUMP_FAILED",
            "",
            f"- Error: {type(error).__name__}: {error}",
            "",
            "The IL2CPP static recovery stage could not complete. Check source integrity and runner logs.",
            "",
        ])
        output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"IL2CPP analysis failed: {type(error).__name__}: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
