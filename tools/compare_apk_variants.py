#!/usr/bin/env python3
"""Compare APKPure Original with Platinmods as a reference, never as build input.

Downloads public Release assets as data, resolves the primary APK from XAPK,
and compares archive member names/sizes/SHA-256. Does not install or execute apps.
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
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from apk_inputs import download_and_hash, get_release, hash_zip_member, resolve_primary_apk, select_release_asset

DEFAULT_REPO = "TenzoNkz/YuGiOh-Duel-Link-MOD"


def validate_tag(value: str) -> None:
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,100}", value):
        raise ValueError("release tag contains unsupported characters")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def bytes_label(size: int) -> str:
    return f"{size:,} bytes ({size / (1024 * 1024):.2f} MiB)"


def load_package(repo: str, tag: str, work: Path, role: str) -> dict:
    validate_tag(tag)
    release = get_release(repo, tag)
    asset = select_release_asset(release)
    name = str(asset.get("name", "(unnamed)"))
    suffix = ".xapk" if name.lower().endswith(".xapk") else ".apk"
    container = work / f"{role}-container{suffix}"
    size, digest = download_and_hash(str(asset["browser_download_url"]), container)
    expected = str(asset.get("digest") or "")
    expected_sha = expected.split(":", 1)[1] if expected.startswith("sha256:") else ""
    digest_ok = digest.lower() == expected_sha.lower() if expected_sha else None
    apk_path, selected_name, inner_apks, obbs = resolve_primary_apk(
        container, name, work / f"{role}-primary.apk"
    )
    package = {
        "tag": tag, "release": release, "asset": asset, "asset_name": name,
        "container_size": size, "container_sha": digest, "expected_sha": expected_sha,
        "digest_ok": digest_ok, "container": container, "apk_path": apk_path,
        "selected_name": selected_name, "apk_size": apk_path.stat().st_size,
        "apk_sha": sha256_file(apk_path), "inner_apks": inner_apks, "obbs": obbs,
    }
    with zipfile.ZipFile(apk_path, "r") as archive:
        entries = {}
        for item in archive.infolist():
            if item.is_dir():
                continue
            entries[item.filename] = {
                "size": item.file_size,
                "compressed": item.compress_size,
                "sha256": hash_zip_member(archive, item),
            }
    package["entries"] = entries
    package["entry_count"] = len(entries)
    package["uncompressed_size"] = sum(entry["size"] for entry in entries.values())
    package["dex"] = sorted(name for name in entries if re.fullmatch(r"classes(?:[0-9]+)?\.dex", name))
    package["native"] = sorted(name for name in entries if name.startswith("lib/") and name.endswith(".so"))
    package["metadata"] = sorted(name for name in entries if name.endswith("global-metadata.dat"))
    package["signature_entries"] = sorted(
        name for name in entries
        if name.upper().startswith("META-INF/") and name.upper().endswith((".RSA", ".DSA", ".EC", ".SF"))
    )
    return package


def source_lines(package: dict, role: str) -> list[str]:
    release = package["release"]
    lines = [
        f"### {role}",
        f"- Release page: {release.get('html_url', '(not provided)')}",
        f"- Release tag: {package['tag']}",
        f"- Asset: {package['asset_name']}",
        f"- Downloaded container size: {bytes_label(package['container_size'])}",
        f"- Expected container SHA-256: {package['expected_sha'] or 'not provided'}",
        f"- Calculated container SHA-256: {package['container_sha']}",
        f"- GitHub digest comparison: {package['digest_ok'] if package['digest_ok'] is not None else 'NOT_PROVIDED'}",
        f"- Container type: {'XAPK' if package['asset_name'].lower().endswith('.xapk') else 'APK'}",
        f"- Selected APK member: {package['selected_name']}",
        f"- Selected APK size: {bytes_label(package['apk_size'])}",
        f"- Selected APK SHA-256: {package['apk_sha']}",
        f"- APK archive entries: {package['entry_count']}",
        f"- Total uncompressed APK size: {bytes_label(package['uncompressed_size'])}",
        f"- DEX count: {len(package['dex'])}",
        f"- Native library count: {len(package['native'])}",
        f"- IL2CPP metadata files found by filename: {len(package['metadata'])}",
        f"- META-INF signature-related entries: {len(package['signature_entries'])}",
    ]
    if package["inner_apks"]:
        lines.append("- Embedded APK members:")
        lines.extend(
            f"  - {item['name']} ({bytes_label(item['size'])}); outer-container CRC: {item.get('container_crc_status', 'NOT_SELECTED')}"
            for item in package["inner_apks"]
        )
        selected_member = next((item for item in package["inner_apks"] if item["name"] == package["selected_name"]), {})
        lines.append(f"- Selected APK member outer-container CRC: {selected_member.get('container_crc_status', 'NOT_APPLICABLE')}")
    if package["obbs"]:
        lines.append("- OBB members:")
        lines.extend(f"  - {name}" for name in package["obbs"][:30])
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPO))
    parser.add_argument("--base-tag", default="APKPure_Latest", help="APKPure Release tag; sole intended mod base")
    parser.add_argument("--reference-tag", default="Latest", help="Platinmods Release tag; comparison only")
    parser.add_argument("--output", default="APK_VARIANT_COMPARISON.md")
    args = parser.parse_args()
    validate_tag(args.base_tag)
    validate_tag(args.reference_tag)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    with tempfile.TemporaryDirectory(prefix="apk-variant-compare-") as temp:
        work = Path(temp)
        base = load_package(args.repo, args.base_tag, work, "apkpure")
        reference = load_package(args.repo, args.reference_tag, work, "platinmods")
        left, right = base["entries"], reference["entries"]
        left_names, right_names = set(left), set(right)
        shared = sorted(left_names & right_names)
        same = [name for name in shared if left[name]["sha256"] == right[name]["sha256"]]
        changed = [name for name in shared if left[name]["sha256"] != right[name]["sha256"]]
        base_only, ref_only = sorted(left_names - right_names), sorted(right_names - left_names)
        important = [
            "AndroidManifest.xml", *base["dex"], *reference["dex"],
            "lib/arm64-v8a/libplatinmods.so", "lib/armeabi-v7a/libplatinmods.so",
            "lib/arm64-v8a/libduel.so", "lib/armeabi-v7a/libduel.so",
            "lib/arm64-v8a/libil2cpp.so", "lib/armeabi-v7a/libil2cpp.so",
            "assets/bin/Data/Managed/Metadata/global-metadata.dat",
        ]
        important = list(dict.fromkeys(important))
        key_rows = []
        for name in important:
            a, b = left.get(name), right.get(name)
            if not a and not b:
                continue
            status = "APKPURE_ONLY" if a and not b else "PLATINMODS_ONLY" if b and not a else (
                "IDENTICAL" if a["sha256"] == b["sha256"] else "DIFFERENT"
            )
            key_rows.append(f"| {name} | {a['size'] if a else '—'} | {b['size'] if b else '—'} | {status} |")
        priority = sorted(
            changed,
            key=lambda name: (
                not (name == "AndroidManifest.xml" or name.endswith(".dex") or name.endswith(".so")
                     or name.endswith("global-metadata.dat") or "platinmods" in name.lower()),
                -max(left[name]["size"], right[name]["size"]), name,
            ),
        )
        warnings = []
        base_member = next((item for item in base["inner_apks"] if item["name"] == base["selected_name"]), {})
        reference_member = next((item for item in reference["inner_apks"] if item["name"] == reference["selected_name"]), {})
        if base_member.get("container_crc_status") == "FAIL" or reference_member.get("container_crc_status") == "FAIL":
            warnings.append("- At least one selected embedded APK has an outer XAPK-member CRC mismatch. The bytes were analyzed as data, but the original container is not clean and must be verified before any patch/build.")
        if base["digest_ok"] is False or reference["digest_ok"] is False:
            warnings.append("- One or both container downloads did not match GitHub's declared SHA-256. Resolve before patching.")
        if base["apk_sha"] == reference["apk_sha"]:
            warnings.append("- Selected APK SHA-256 values match. Investigate XAPK sidecars/splits before inferring where differences reside.")
        if not any("libplatinmods.so" in name.lower() for name in ref_only + changed):
            warnings.append("- No libplatinmods.so-only/different entry was detected by exact path; inspect other possible library names.")
        if not warnings:
            warnings.append("- No automatic integrity warning was raised. This does not prove any mod feature works.")

        lines = [
            "# APKPure Original vs Platinmods — Static Variant Comparison", "",
            f"Generated: {generated}",
            "Purpose: APKPure Original is the sole intended mod base. Platinmods is a comparison reference only.",
            "Method: Release digest checks, primary APK resolution, archive entry inventory, and per-entry SHA-256 comparison. No app was installed or executed.", "",
            "## Source identity",
            *source_lines(base, "APKPure Original — intended modification base"),
            "",
            *source_lines(reference, "Platinmods — reference only"),
            "",
            "## Comparison summary",
            f"- Shared entry paths: {len(shared)}",
            f"- Shared entries with identical SHA-256: {len(same)}",
            f"- Shared entries with different SHA-256: {len(changed)}",
            f"- APKPure-only entries: {len(base_only)}",
            f"- Platinmods-only entries: {len(ref_only)}", "",
            "## Key package and executable entries",
            "| Entry path | APKPure bytes | Platinmods bytes | Result |",
            "|---|---:|---:|---|",
            *(key_rows or ["| No key entries detected | — | — | UNKNOWN |"]),
            "",
            "## Highest-priority differing entries",
            "| Entry path | APKPure bytes | Platinmods bytes | Classification |",
            "|---|---:|---:|---|",
        ]
        for name in priority[:100]:
            kind = "DEX/code" if name.endswith(".dex") else "native code" if name.endswith(".so") else "IL2CPP metadata" if name.endswith("global-metadata.dat") else "manifest/resources/assets"
            lines.append(f"| {name} | {left[name]['size']:,} | {right[name]['size']:,} | {kind} |")
        if not priority:
            lines.append("| No different shared paths | — | — | None found |")
        lines.extend([
            "",
            "## APKPure-only entries (first 60)",
            *([f"- {name} — {bytes_label(left[name]['size'])}" for name in base_only[:60]] or ["- None found."]),
            "",
            "## Platinmods-only entries (first 60)",
            *([f"- {name} — {bytes_label(right[name]['size'])}" for name in ref_only[:60]] or ["- None found."]),
            "",
            "## Limitations and interpretation",
            *warnings,
            "- Different entry hashes prove byte differences only, not what changed semantically.",
            "- APK v2/v3 signing blocks are not ordinary ZIP entries; this report does not verify signer identity or Android update compatibility.",
            "- For XAPK input, the selected primary APK is compared. Other split APKs and OBBs are listed but are not merged into a single installable APK here.",
            "- Platinmods is not the build base. Do not copy its binary components into CHATGPT MOD without independent technical review and necessary rights.",
            "",
            "## Next reverse-engineering actions",
            "1. Read APK_CODE_ANALYSIS.md for package, DEX, resource, and native-string findings from the APKPure primary APK.",
            "2. Trace candidate features from menu label/resource through DEX callbacks into native dispatch where evidence permits.",
            "3. Record verified facts, hypotheses, and test results separately in MOD_CANDIDATES.md.",
            "4. Keep final APK patch/build blocked until the desired features and XAPK/split compatibility have evidence.",
            "",
        ])
        output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (urllib.error.URLError, TimeoutError, OSError, RuntimeError, ValueError, json.JSONDecodeError, zipfile.BadZipFile) as error:
        print(f"Variant comparison failed: {type(error).__name__}: {error}", file=sys.stderr)
        raise SystemExit(1)
