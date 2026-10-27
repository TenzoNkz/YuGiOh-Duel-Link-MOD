#!/usr/bin/env python3
"""Safe helpers for resolving APK or XAPK Release assets without installing them."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import urllib.request
import zipfile
import zlib
from pathlib import Path
from typing import Any

USER_AGENT = "YuGiOh-Duel-Link-MOD-analysis/1.0"


def github_api_headers() -> dict[str, str]:
    """Build GitHub API headers, using the Actions token when available."""
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": USER_AGENT,
    }
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def get_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(url, headers=github_api_headers())
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def get_release(repo: str, tag: str) -> dict[str, Any]:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("repository must be in owner/name form")
    if not re.fullmatch(r"[A-Za-z0-9._-]{1,100}", tag):
        raise ValueError("release tag contains unsupported characters")
    url = f"https://api.github.com/repos/{repo}/releases/tags/{tag}"
    return get_json(url)


def select_release_asset(release: dict[str, Any], asset_name: str = "") -> dict[str, Any]:
    candidates = [
        item for item in release.get("assets", [])
        if str(item.get("name", "")).lower().endswith((".apk", ".xapk"))
    ]
    if asset_name:
        candidates = [item for item in candidates if item.get("name") == asset_name]
    if len(candidates) != 1:
        names = ", ".join(str(item.get("name", "(unnamed)")) for item in candidates) or "none"
        raise RuntimeError(
            f"Expected exactly one matching APK/XAPK Release asset; found {len(candidates)}. "
            f"Matching names: {names}. Use --asset-name if necessary."
        )
    return candidates[0]


def download_and_hash(url: str, destination: Path) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    digest = hashlib.sha256()
    size = 0
    with urllib.request.urlopen(request, timeout=240) as response, destination.open("wb") as output:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            output.write(chunk)
            digest.update(chunk)
            size += len(chunk)
    return size, digest.hexdigest()


def extract_xapk_member(container_path: Path, member_name: str, destination: Path) -> dict[str, Any]:
    """Extract one named APK member and explicitly report the outer-container CRC."""
    with zipfile.ZipFile(container_path, "r") as archive:
        matches = [
            item for item in archive.infolist()
            if not item.is_dir() and item.filename == member_name
        ]
        if len(matches) != 1:
            raise RuntimeError(f"Expected one XAPK member named {member_name!r}; found {len(matches)}")
        selected = matches[0]
        destination.parent.mkdir(parents=True, exist_ok=True)
        with archive.open(selected, "r") as source, destination.open("wb") as output:
            if hasattr(source, "_expected_crc"):
                source._expected_crc = None
            shutil.copyfileobj(source, output, length=1024 * 1024)
        if destination.stat().st_size != selected.file_size:
            raise RuntimeError(f"Extracted XAPK member {member_name!r} has an unexpected size")
        crc = 0
        with destination.open("rb") as selected_stream:
            for chunk in iter(lambda: selected_stream.read(1024 * 1024), b""):
                crc = zlib.crc32(chunk, crc)
        crc_value = crc & 0xFFFFFFFF
        record = {
            "name": selected.filename,
            "size": selected.file_size,
            "compressed_size": selected.compress_size,
            "expected_container_crc32": f"{selected.CRC:08x}",
            "calculated_container_crc32": f"{crc_value:08x}",
            "container_crc_status": "PASS" if crc_value == selected.CRC else "FAIL",
        }
    with zipfile.ZipFile(destination, "r") as nested:
        if "AndroidManifest.xml" not in nested.namelist():
            raise RuntimeError(f"Selected XAPK member {member_name!r} has no AndroidManifest.xml")
    return record


def resolve_primary_apk(
    container_path: Path,
    asset_name: str,
    destination: Path,
) -> tuple[Path, str, list[dict[str, Any]], list[str]]:
    """Return the APK to analyze, selected inner member, all embedded APKs and OBBs.

    XAPK members are streamed to a controlled destination filename; archive paths
    are never extracted as filesystem paths. The original container is retained.
    """
    if asset_name.lower().endswith(".apk"):
        return container_path, asset_name, [], []

    if not asset_name.lower().endswith(".xapk"):
        raise RuntimeError(f"Unsupported input extension for {asset_name!r}; expected .apk or .xapk")

    with zipfile.ZipFile(container_path, "r") as archive:
        infos = archive.infolist()
        apk_infos = [
            item for item in infos
            if not item.is_dir() and item.filename.lower().endswith(".apk")
        ]
        obb_names = [
            item.filename for item in infos
            if not item.is_dir() and item.filename.lower().endswith(".obb")
        ]
        if not apk_infos:
            raise RuntimeError("XAPK container contains no embedded .apk files")

        def score(info: zipfile.ZipInfo) -> tuple[int, int, int]:
            basename = Path(info.filename.replace("\\", "/")).name.lower()
            if basename == "base.apk":
                rank = 100
            elif basename in ("main.apk", "game.apk"):
                rank = 90
            elif "jp.konami.duellinks" in basename or "duellinks" in basename:
                rank = 85
            elif "base" in basename and not any(word in basename for word in ("config", "split")):
                rank = 80
            elif not re.search(r"(^|[._-])(config|split)([._-]|$)", basename):
                rank = 50
            else:
                rank = 0
            return rank, info.file_size, -len(info.filename)

        selected = max(apk_infos, key=score)
        if score(selected)[0] <= 0:
            raise RuntimeError(
                "XAPK APK members appear to be split/config APKs only; no safe base APK candidate was identified"
            )
        # Record member sizes, not content: detailed hashes are computed from the selected APK.
        nested_summary = [
            {
                "name": item.filename,
                "size": item.file_size,
                "compressed_size": item.compress_size,
                "container_crc_status": "NOT_SELECTED",
            }
            for item in sorted(apk_infos, key=lambda item: item.filename)
        ]
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Some third-party XAPK containers have an incorrect CRC in the outer
        # ZIP directory even though the embedded APK bytes form a valid APK.
        # Extract to a controlled path without trusting the outer CRC, then
        # explicitly calculate and report the actual CRC. Never suppress the
        # selected APK's own archive-integrity tests.
        with archive.open(selected, "r") as source, destination.open("wb") as output:
            if hasattr(source, "_expected_crc"):
                source._expected_crc = None
            shutil.copyfileobj(source, output, length=1024 * 1024)
        if destination.stat().st_size != selected.file_size:
            raise RuntimeError("Extracted primary APK size does not match its XAPK directory entry")
        crc = 0
        with destination.open("rb") as selected_stream:
            for chunk in iter(lambda: selected_stream.read(1024 * 1024), b""):
                crc = zlib.crc32(chunk, crc)
        selected_crc_status = "PASS" if (crc & 0xFFFFFFFF) == selected.CRC else "FAIL"
        for item in nested_summary:
            if item["name"] == selected.filename:
                item["container_crc_status"] = selected_crc_status
                item["expected_container_crc32"] = f"{selected.CRC:08x}"
                item["calculated_container_crc32"] = f"{crc & 0xFFFFFFFF:08x}"
        # Ensure the selected nested APK is itself a readable ZIP/APK.
        with zipfile.ZipFile(destination, "r") as nested:
            if "AndroidManifest.xml" not in nested.namelist():
                raise RuntimeError(f"Selected XAPK member {selected.filename!r} has no AndroidManifest.xml")
    return destination, selected.filename, nested_summary, sorted(obb_names)


def hash_zip_member(archive: zipfile.ZipFile, member: zipfile.ZipInfo) -> str:
    digest = hashlib.sha256()
    with archive.open(member, "r") as stream:
        while True:
            chunk = stream.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()
