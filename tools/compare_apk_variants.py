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
import zlib
from datetime import datetime, timezone
from pathlib import Path

from apk_inputs import download_and_hash, extract_xapk_member, get_release, hash_zip_member, resolve_primary_apk, select_release_asset

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


def source_integrity_assessment(
    digest_ok: bool | None,
    outer_crc_failures: list[str],
    read_errors: dict[str, str],
) -> str:
    """Describe APKPure's integrity based only on the package actually analyzed."""
    problems = []
    if digest_ok is not True:
        problems.append(
            "container digest mismatch"
            if digest_ok is False
            else "Release digest not provided"
        )
    if outer_crc_failures:
        problems.append("embedded APK outer CRC failures: " + ", ".join(outer_crc_failures))
    if read_errors:
        problems.append(f"{len(read_errors)} unreadable or corrupt package entries")
    if problems:
        return "WARN: " + "; ".join(problems) + "."
    return "PASS: Release digest matched; embedded APK outer CRCs and per-entry reads passed."


def load_package(repo: str, tag: str, work: Path, role: str) -> dict:
    validate_tag(tag)
    release = get_release(repo, tag)
    asset = select_release_asset(release)
    name = str(asset.get("name", "(unnamed)"))
    suffix = ".xapk" if name.lower().endswith(".xapk") else ".apk"
    container = work / f"{role}-container{suffix}"
    size, container_digest = download_and_hash(str(asset["browser_download_url"]), container)
    expected = str(asset.get("digest") or "")
    expected_sha = expected.split(":", 1)[1] if expected.startswith("sha256:") else ""
    digest_ok = container_digest.lower() == expected_sha.lower() if expected_sha else None
    primary_path, selected_name, inner_apks, obbs = resolve_primary_apk(
        container, name, work / f"{role}-primary.apk"
    )
    members = []
    if suffix == ".xapk":
        for index, member in enumerate(inner_apks, start=1):
            if member["name"] == selected_name:
                members.append({
                    **member, "path": primary_path, "is_primary": True,
                    "container_crc_status": member.get("container_crc_status", "NOT_CHECKED"),
                })
                continue
            split_path = work / f"{role}-split-{index}.apk"
            try:
                extracted = extract_xapk_member(container, member["name"], split_path)
                inner_apks = [
                    extracted if current["name"] == member["name"] else current
                    for current in inner_apks
                ]
                members.append({
                    **extracted, "path": split_path, "is_primary": False,
                })
            except (zipfile.BadZipFile, zlib.error, EOFError, OSError, RuntimeError, NotImplementedError) as error:
                note = f"{type(error).__name__}: {error}"
                inner_apks = [
                    {**current, "analysis_error": note}
                    if current["name"] == member["name"] else current
                    for current in inner_apks
                ]
                members.append({
                    **member, "path": None, "is_primary": False,
                    "container_crc_status": "EXTRACTION_FAILED", "analysis_error": note,
                })
    else:
        members.append({
            "name": name, "size": size, "compressed_size": None,
            "path": primary_path, "is_primary": True,
            "container_crc_status": "NOT_APPLICABLE",
        })

    package = {
        "tag": tag, "release": release, "asset": asset, "asset_name": name,
        "container_size": size, "container_sha": container_digest, "expected_sha": expected_sha,
        "digest_ok": digest_ok, "container": container, "apk_path": primary_path,
        "selected_name": selected_name, "apk_size": primary_path.stat().st_size,
        "apk_sha": sha256_file(primary_path), "inner_apks": inner_apks, "obbs": obbs,
        "members": members,
    }
    entries: dict[str, dict] = {}
    read_errors: dict[str, str] = {}
    member_conflicts: list[str] = []
    for member in members:
        if member["path"] is None:
            read_errors[f"{member['name']}::<container>"] = member.get("analysis_error", "member extraction failed")
            continue
        member_errors = []
        try:
            with zipfile.ZipFile(member["path"], "r") as archive:
                member_infos = archive.infolist()
                member["entry_count"] = sum(not info.is_dir() for info in member_infos)
                member["native_count"] = sum(
                    not info.is_dir() and info.filename.startswith("lib/") and info.filename.endswith(".so")
                    for info in member_infos
                )
                member["dex_count"] = sum(
                    not info.is_dir() and bool(re.fullmatch(r"classes(?:[0-9]+)?\.dex", info.filename))
                    for info in member_infos
                )
                for item in member_infos:
                    if item.is_dir():
                        continue
                    # A split APK's own manifest and META-INF entries describe
                    # that split/signature, not the base app's logical resources.
                    if not member["is_primary"] and (
                        item.filename == "AndroidManifest.xml"
                        or item.filename.upper().startswith("META-INF/")
                    ):
                        continue
                    try:
                        item_digest = hash_zip_member(archive, item)
                        item_error = None
                    except (zipfile.BadZipFile, zlib.error, EOFError, OSError, RuntimeError, NotImplementedError) as error:
                        item_digest = None
                        item_error = f"{type(error).__name__}: {error}"
                        member_errors.append(f"{item.filename}: {item_error}")
                    record = {
                        "size": item.file_size,
                        "compressed": item.compress_size,
                        "sha256": item_digest,
                        "read_error": item_error,
                        "source_member": member["name"],
                    }
                    current = entries.get(item.filename)
                    if current is None:
                        entries[item.filename] = record
                    elif current["sha256"] == item_digest:
                        pass
                    elif current["sha256"] is None and item_digest is not None and member["is_primary"]:
                        entries[item.filename] = record
                        member_conflicts.append(
                            f"{item.filename}: primary failed to hash; a member also supplies a readable copy"
                        )
                    else:
                        member_conflicts.append(
                            f"{item.filename}: kept {current['source_member']}; conflicting copy in {member['name']}"
                        )
                    if item_error:
                        read_errors[f"{member['name']}::{item.filename}"] = item_error
        except (zipfile.BadZipFile, zlib.error, EOFError, OSError, RuntimeError, NotImplementedError) as error:
            member_errors.append(f"archive read: {type(error).__name__}: {error}")
            read_errors[f"{member['name']}::<archive>"] = member_errors[-1]
        member["read_errors"] = member_errors
        member["inner_crc_status"] = "FAIL" if member_errors else "PASS"
    package["entries"] = entries
    package["read_errors"] = read_errors
    package["member_conflicts"] = member_conflicts
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
        f"- Selected primary APK member: {package['selected_name']}",
        f"- Selected primary APK size: {bytes_label(package['apk_size'])}",
        f"- Selected primary APK SHA-256: {package['apk_sha']}",
        f"- Physical APK members inventoried: {len(package['members'])}",
        f"- Logical package entries across primary and split payloads: {package['entry_count']}",
        f"- Aggregate uncompressed payload size (unique paths): {bytes_label(package['uncompressed_size'])}",
        f"- DEX count across logical package: {len(package['dex'])}",
        f"- Native library count across primary and split payloads: {len(package['native'])}",
        f"- IL2CPP metadata files found by filename: {len(package['metadata'])}",
        f"- Signature-related entries in merged payload inventory: {len(package['signature_entries'])}",
    ]
    if package["inner_apks"]:
        lines.append("- Embedded APK members:")
        lines.extend(
            f"  - {item['name']} ({bytes_label(item['size'])}); outer-container CRC: {item.get('container_crc_status', 'NOT_SELECTED')}; inner ZIP: {item.get('inner_crc_status', 'NOT_INVENTORIED')}"
            for item in package["members"]
        )
        selected_member = next((item for item in package["members"] if item["name"] == package["selected_name"]), {})
        lines.append(f"- Selected primary APK member outer-container CRC: {selected_member.get('container_crc_status', 'NOT_APPLICABLE')}")
        if package["member_conflicts"]:
            lines.append(f"- Conflicting duplicate paths across split APKs: {len(package['member_conflicts'])}")
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
        comparable = [
            name for name in shared
            if left[name]["sha256"] is not None and right[name]["sha256"] is not None
        ]
        same = [name for name in comparable if left[name]["sha256"] == right[name]["sha256"]]
        changed = [name for name in comparable if left[name]["sha256"] != right[name]["sha256"]]
        unverified_shared = [
            name for name in shared
            if left[name]["sha256"] is None or right[name]["sha256"] is None
        ]
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
                "UNVERIFIED_CORRUPT_ENTRY" if a["sha256"] is None or b["sha256"] is None else
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
        base_member = next((item for item in base["members"] if item["name"] == base["selected_name"]), {})
        reference_member = next((item for item in reference["members"] if item["name"] == reference["selected_name"]), {})
        base_crc_failures = [item["name"] for item in base["members"] if item.get("container_crc_status") == "FAIL"]
        reference_crc_failures = [item["name"] for item in reference["members"] if item.get("container_crc_status") == "FAIL"]
        if base_crc_failures:
            warnings.append(
                "- APKPure embedded APK outer CRC failures: "
                + ", ".join(base_crc_failures)
                + ". The intended source package needs replacement or verification before patch/build."
            )
        if reference_crc_failures:
            warnings.append(
                "- Platinmods reference embedded APK outer CRC failures: "
                + ", ".join(reference_crc_failures)
                + ". Treat the reference comparison as incomplete; this does not by itself invalidate the APKPure base."
            )
        if base["read_errors"] or reference["read_errors"]:
            warnings.append(f"- Entries could not be fully decompressed/hashed: APKPure main/splits={len(base['read_errors'])}, Platinmods={len(reference['read_errors'])}. See the unverified-entry section below.")
        if base["read_errors"]:
            warnings.append("- BUILD BLOCKER: the APKPure source package has unreadable or corrupt entries. Do not patch/build until the source is replaced or its integrity is resolved.")
        if base["digest_ok"] is True and (base["read_errors"] or any(member.get("container_crc_status") == "FAIL" for member in base["members"])):
            warnings.append("- The XAPK container SHA-256 matches GitHub's release metadata, but this only confirms the downloaded bytes match the uploaded asset. It does not establish that the embedded package contents are internally valid.")
        if base["digest_ok"] is False or reference["digest_ok"] is False:
            warnings.append("- One or both container downloads did not match GitHub's declared SHA-256. Resolve before patching.")
        if base["apk_sha"] == reference["apk_sha"]:
            warnings.append("- Selected APK SHA-256 values match. Investigate XAPK sidecars/splits before inferring where differences reside.")
        base_integrity_assessment = source_integrity_assessment(
            base["digest_ok"], base_crc_failures, base["read_errors"]
        )
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
            f"- Shared entries with at least one unreadable/corrupt member: {len(unverified_shared)}",
            f"- Unreadable/corrupt entries across APKPure main/split APKs: {len(base['read_errors'])}",
            f"- Unreadable/corrupt entries in Platinmods APK: {len(reference['read_errors'])}",
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
            "## Shared entries with unreadable/corrupt content (first 60)",
            *([f"- {name}: APKPure={left[name]['read_error'] or 'readable'}, Platinmods={right[name]['read_error'] or 'readable'}" for name in unverified_shared[:60]] or ["- None found."]),
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
            "- For XAPK input, the comparison merges the primary APK's logical entries with unique entries from extracted splits (including native libraries), while excluding split-specific manifests/signature metadata. It does not synthesize or validate a single installable APK.",
            f"- APKPure source-integrity assessment: {base_integrity_assessment}",
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
