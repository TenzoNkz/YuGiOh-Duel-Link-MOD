#!/usr/bin/env python3
"""Non-executing inventory for a public APK asset attached to a GitHub Release.

The APK is downloaded as data, never installed or executed. This first-stage
workflow verifies the reported digest, checks ZIP structure/CRCs when safe,
and inventories DEX files, native libraries, and engine indicators.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from apk_inputs import download_and_hash, resolve_primary_apk, select_release_asset, get_release

USER_AGENT = "YuGiOh-Duel-Link-MOD-static-analysis/1.0"
MAX_MEMBERS_FOR_CRC = 100_000
MAX_UNCOMPRESSED_BYTES_FOR_CRC = 5 * 1024 * 1024 * 1024


def human_bytes(value: int) -> str:
    units = ("B", "KiB", "MiB", "GiB", "TiB")
    amount = float(value)
    for unit in units:
        if amount < 1024 or unit == units[-1]:
            return f"{amount:.2f} {unit}" if unit != "B" else f"{value} B"
        amount /= 1024
    return f"{value} B"


def status_text(ok: bool | None) -> str:
    if ok is True:
        return "PASS"
    if ok is False:
        return "FAIL"
    return "NOT_AVAILABLE"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-tag", required=True, help="Existing public GitHub Release tag")
    parser.add_argument(
        "--repo",
        default=os.environ.get("GITHUB_REPOSITORY", "TenzoNkz/YuGiOh-Duel-Link-MOD"),
        help="Repository in owner/name form",
    )
    parser.add_argument("--asset-name", default="", help="Exact APK or XAPK asset name; useful when a Release has multiple package assets")
    parser.add_argument("--output", default="APP_ANALYSIS_REPORT.md", help="Markdown report output path")
    args = parser.parse_args()

    if not re.fullmatch(r"[A-Za-z0-9._-]{1,100}", args.release_tag):
        parser.error("release tag contains unsupported characters")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.repo):
        parser.error("repository must be in owner/name form")

    release = get_release(args.repo, args.release_tag)
    asset = select_release_asset(release, args.asset_name)
    asset_name = asset.get("name", "(unnamed)")
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="apk-static-analysis-") as temporary:
        work = Path(temporary)
        suffix = ".xapk" if asset_name.lower().endswith(".xapk") else ".apk"
        container_path = work / ("source-container" + suffix)
        downloaded_bytes, actual_sha256 = download_and_hash(
            asset["browser_download_url"], container_path
        )
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
        expected_digest = asset.get("digest") or ""
        expected_sha256 = (
            expected_digest.split(":", 1)[1]
            if expected_digest.startswith("sha256:")
            else ""
        )
        digest_matches = (
            actual_sha256.lower() == expected_sha256.lower()
            if expected_sha256
            else None
        )

        archive_opened = False
        crc_result = "NOT_CHECKED"
        crc_bad_file = ""
        archive_error = ""
        infos = []
        try:
            with zipfile.ZipFile(apk_path, "r") as archive:
                infos = archive.infolist()
                archive_opened = True
                uncompressed_total = sum(item.file_size for item in infos)
                if (
                    len(infos) <= MAX_MEMBERS_FOR_CRC
                    and uncompressed_total <= MAX_UNCOMPRESSED_BYTES_FOR_CRC
                ):
                    crc_bad_file = archive.testzip() or ""
                    crc_result = "PASS" if not crc_bad_file else "FAIL"
                else:
                    crc_result = "SKIPPED_RESOURCE_LIMIT"
        except (zipfile.BadZipFile, OSError, RuntimeError, NotImplementedError) as exc:
            archive_error = f"{type(exc).__name__}: {exc}"
            archive_opened = False
            crc_result = "FAIL"

        file_names = [item.filename for item in infos]
        dex_infos = sorted(
            [item for item in infos if re.fullmatch(r"classes(?:[0-9]+)?\.dex", item.filename)],
            key=lambda item: item.filename,
        )
        native_infos = [
            item for item in infos
            if item.filename.startswith("lib/") and item.filename.endswith(".so")
        ]
        abi_counts: Counter[str] = Counter()
        for item in native_infos:
            parts = item.filename.split("/")
            if len(parts) >= 3:
                abi_counts[parts[1]] += 1

        engine_markers = {
            "Unity": ("libunity.so", "libil2cpp.so", "global-metadata.dat", "assets/bin/data/"),
            "Unreal Engine": ("libue4.so", "libunreal.so", ".pak"),
            "Cocos2d": ("libcocos2dcpp.so", "libcocos2djs.so"),
            "Flutter": ("libflutter.so", "libapp.so"),
            "React Native": ("libreactnativejni.so", "index.android.bundle"),
        }
        engine_hits = {}
        lowered_names = [(name, name.lower()) for name in file_names]
        for engine, markers in engine_markers.items():
            hits = []
            for original, lower in lowered_names:
                if any(marker in lower for marker in markers):
                    hits.append(original)
            if hits:
                engine_hits[engine] = hits[:20]

        signature_entries = [
            name for name in file_names
            if name.upper().startswith("META-INF/")
            and name.upper().endswith((".RSA", ".DSA", ".EC", ".SF"))
        ]
        manifest_present = "AndroidManifest.xml" in file_names
        largest = sorted(infos, key=lambda item: item.file_size, reverse=True)[:20]
        total_uncompressed = sum(item.file_size for item in infos)
        dex_lines = [
            f"- {item.filename}: {item.file_size} bytes ({human_bytes(item.file_size)})"
            for item in dex_infos
        ] or ["- No root-level classes*.dex file detected."]
        abi_lines = [
            f"- {abi}: {count} shared library file(s)"
            for abi, count in sorted(abi_counts.items())
        ] or ["- No native libraries under lib/<ABI>/ were detected."]
        engine_lines = []
        for engine, hits in sorted(engine_hits.items()):
            engine_lines.append(f"- **{engine}:** " + ", ".join(hits[:8]))
        if not engine_lines:
            engine_lines = ["- No common engine marker was found by the basic filename scan; this does not prove the APK uses no engine."]
        signature_lines = [f"- {name}" for name in signature_entries[:20]]
        if not signature_lines:
            signature_lines = ["- No META-INF certificate/signature entries detected in the ZIP listing. APK v2/v3 signing blocks are not ZIP entries and are not validated by this script."]
        largest_lines = [
            f"- {item.filename}: {human_bytes(item.file_size)} uncompressed"
            for item in largest
        ] or ["- No archive entries could be listed."]

        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        lines = [
            "# APK Static Analysis Report",
            "",
            f"**Status:** {'INVENTORY_COMPLETE_WITH_WARNINGS' if (digest_matches is False or crc_result == 'FAIL' or selected_container_crc == 'FAIL') else 'INVENTORY_COMPLETE'}",
            f"**Generated:** {timestamp}",
            "**Method:** static archive inspection only; the APK was not executed or installed.",
            "",
            "## Source Release",
            f"- Repository: {args.repo}",
            f"- Release title: {release.get('name') or '(untitled)'}",
            f"- Release tag: {release.get('tag_name') or args.release_tag}",
            f"- Release page: {release.get('html_url') or '(not provided)'}",
            f"- Asset: {asset_name}",
            f"- Asset download URL: {asset.get('browser_download_url') or '(not provided)'}",
            f"- GitHub-reported size: {asset.get('size', 'unknown')} bytes",
            f"- Actual downloaded size: {downloaded_bytes} bytes ({human_bytes(downloaded_bytes)})",
            f"- Expected GitHub SHA-256: {expected_sha256 or 'not provided'}",
            f"- Calculated SHA-256: {actual_sha256}",
            f"- SHA-256 comparison: {status_text(digest_matches)}",
            "",
            "## Selected APK and XAPK container",
            f"- Input type: {'XAPK container with embedded APK' if suffix == '.xapk' else 'APK'}",
            f"- APK analyzed: {embedded_apk_name}",
            f"- Analyzed APK size: {apk_path.stat().st_size} bytes",
            f"- Embedded APK members: {len(nested_apks)}",
            *([f"- Embedded APK member: {item['name']} ({item['size']} bytes)" for item in nested_apks] or ["- No nested APK members; the Release asset itself is the APK."]),
            f"- OBB members in container: {len(obb_names)}",
            *([f"- OBB member: {name}" for name in obb_names[:20]] or ["- No .obb member found in the XAPK container."]),
            "",
            f"- Selected APK member CRC in the XAPK container: {selected_container_crc}",
            "## Selected APK archive integrity",
            f"- ZIP/APK opened: {status_text(archive_opened)}",
            f"- Central-directory entry count: {len(infos)}",
            f"- Total uncompressed size: {total_uncompressed} bytes ({human_bytes(total_uncompressed)})",
            f"- CRC scan: {crc_result}",
        ]
        if crc_bad_file:
            lines.append(f"- First CRC-failing entry: {crc_bad_file}")
        if archive_error:
            lines.append(f"- Archive error: {archive_error}")
        lines.extend([
            "",
            "## Structural inventory",
            f"- AndroidManifest.xml present: {'YES' if manifest_present else 'NO'}",
            f"- DEX file count: {len(dex_infos)}",
            *dex_lines,
            "",
            f"- Native library count (.so): {len(native_infos)}",
            *abi_lines,
            "",
            "## Common engine indicators",
            *engine_lines,
            "",
            "## Signature-related ZIP entries",
            *signature_lines,
            "",
            "## Largest entries by uncompressed size",
            *largest_lines,
            "",
            "## What this report does not prove",
            "- This script does not decode the binary AndroidManifest.xml, so package name, versionName, minSdk, and targetSdk are not asserted.",
            "- It does not validate Android APK signatures or identify a trusted signer.",
            "- It does not decompile DEX/native code, trace feature callbacks, or prove that any toggle works.",
            "- Filename indicators are heuristics only; they are not definitive engine identification.",
            "- For XAPK input, this report inventories the selected primary APK and lists embedded APK/OBB members; it does not install the split set or prove that a single APK alone is sufficient.",
            "- It does not execute, install, patch, or rebuild the APK.",
            "",
            "## Recommended next step",
            "Review the inventory and, if needed, run a separate tool-assisted static decompilation stage. Record file/class/method evidence for every candidate and keep hypotheses separate from verified findings.",
            "",
        ])
        output_path.write_text("\n".join(lines), encoding="utf-8")

    if digest_matches is False or crc_result == "FAIL" or selected_container_crc == "FAIL":
        print(
            "WARNING: the report was written, but the digest comparison or archive integrity check failed.",
            file=sys.stderr,
        )
        return 2
    print(f"Wrote {output_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (urllib.error.URLError, TimeoutError, OSError, RuntimeError, json.JSONDecodeError) as error:
        print(f"APK static analysis failed: {type(error).__name__}: {error}", file=sys.stderr)
        raise SystemExit(1)
