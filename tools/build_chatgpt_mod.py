#!/usr/bin/env python3
"""Build a UI-only CHATGPT MOD APK from the verified APKPure XAPK.

This tool is deliberately gated by the durable feature-approval marker. It
never uses Platinmods binaries as build inputs and has no gameplay cheat hooks.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
import zlib
from pathlib import Path, PurePosixPath
from typing import Sequence
from xml.etree import ElementTree

from apk_inputs import download_and_hash, extract_xapk_member, get_release, resolve_primary_apk, select_release_asset

APKTOOL_URL = "https://github.com/iBotPeaches/Apktool/releases/download/v3.0.3/apktool_3.0.3.jar"
EXPECTED_PACKAGE = "jp.konami.duellinks"
MENU_CALL = "invoke-static {p0}, Lcom/chatgptmod/menu/ModMenu;->install(Landroid/app/Activity;)V"
ACTIVITY_SMALI = "YgomMainActivity.smali"


class BuildError(RuntimeError):
    """Raised when a build precondition or tool operation fails."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_zip(path: Path, label: str, require_manifest: bool = False) -> None:
    """Read every member and verify the archive's CRC/decompression integrity."""
    try:
        with zipfile.ZipFile(path, "r") as archive:
            if require_manifest and "AndroidManifest.xml" not in archive.namelist():
                raise BuildError(f"{label} has no AndroidManifest.xml.")
            bad_member = archive.testzip()
            if bad_member:
                raise BuildError(f"{label} failed CRC validation at {bad_member}.")
    except BuildError:
        raise
    except (OSError, zipfile.BadZipFile, zipfile.LargeZipFile, RuntimeError,
            zlib.error, EOFError, NotImplementedError) as error:
        raise BuildError(f"{label} is not a valid readable ZIP/APK: {type(error).__name__}: {error}") from error


def parse_package(decoded_manifest: Path) -> str:
    try:
        root = ElementTree.parse(decoded_manifest).getroot()
    except (OSError, ElementTree.ParseError) as error:
        raise BuildError(f"Could not parse decoded manifest: {error}") from error
    return root.get("package", "")


def patch_activity_smali(activity_path: Path) -> bool:
    """Insert one menu initialization call after the Activity's onCreate super call.

    Returns True if patched. It fails closed for an unexpected method structure,
    and refuses duplicate insertion instead of silently patching a built APK twice.
    """
    source = activity_path.read_text(encoding="utf-8", errors="replace")
    method_header = re.compile(
        r"(?m)^\.method\s+[^\n]*\bonCreate\(Landroid/os/Bundle;\)V\s*$"
    )
    headers = list(method_header.finditer(source))
    if len(headers) != 1:
        raise BuildError(
            f"Expected exactly one onCreate(Bundle) method in {activity_path.name}; "
            f"found {len(headers)}."
        )

    method_start = headers[0].start()
    end_match = re.search(r"(?m)^\.end method\s*$", source[headers[0].end():])
    if not end_match:
        raise BuildError("The onCreate(Bundle) method has no .end method boundary.")
    method_end = headers[0].end() + end_match.end()
    method_text = source[method_start:method_end]
    if MENU_CALL in method_text or "Lcom/chatgptmod/menu/ModMenu;->install(" in method_text:
        raise BuildError("The CHATGPT MOD install hook is already present; refusing duplicate injection.")

    super_call = re.compile(
        r"(?m)^(?P<indent>[ \t]*)invoke-super(?:/range)?[ \t]+\{[^}]+\}, "
        r"L[^;]+;->onCreate\(Landroid/os/Bundle;\)V[ \t]*$"
    )
    calls = list(super_call.finditer(method_text))
    if len(calls) != 1:
        raise BuildError(
            "Could not uniquely identify the superclass onCreate(Bundle) call "
            "in YgomMainActivity; source may have changed."
        )
    match = calls[0]
    insertion = "\n" + match.group("indent") + MENU_CALL
    method_text = method_text[:match.end()] + insertion + method_text[match.end():]
    patched = source[:method_start] + method_text + source[method_end:]
    if patched.count(MENU_CALL) != 1:
        raise BuildError("Patch postcondition failed: the menu hook must occur exactly once.")
    activity_path.write_text(patched, encoding="utf-8")
    return True


def require_approval(candidates_path: Path) -> None:
    if not candidates_path.is_file():
        raise BuildError(f"Missing feature register: {candidates_path}")
    candidates = candidates_path.read_text(encoding="utf-8")
    # The approval must be the exact current checkpoint line, not merely a mention
    # of the required marker in explanatory prose elsewhere in the file.
    approved_line = re.compile(
        r"(?m)^\s*\*\*Build approval:\s*APPROVED_FOR_IMPLEMENTATION\s*\*\*\s*$"
    )
    if not approved_line.search(candidates):
        raise BuildError(
            "Build approval is still pending. The exact standalone line "
            "'**Build approval: APPROVED_FOR_IMPLEMENTATION**' must be explicitly set "
            "in MOD_CANDIDATES.md before running a build."
        )


def check_reports(root: Path) -> None:
    """Require verified integrity and the currently documented Activity integration point."""
    required = [
        "APP_ANALYSIS_REPORT.md",
        "APK_CODE_ANALYSIS.md",
        "IL2CPP_ANALYSIS_REPORT.md",
        "APK_VARIANT_COMPARISON.md",
        "MOD_CANDIDATES.md",
        "MOD_INTEGRATION_PLAN.md",
    ]
    missing = [name for name in required if not (root / name).is_file()]
    if missing:
        raise BuildError("Missing durable preflight report(s): " + ", ".join(missing))

    static = (root / "APP_ANALYSIS_REPORT.md").read_text(encoding="utf-8")
    code = (root / "APK_CODE_ANALYSIS.md").read_text(encoding="utf-8")
    il2cpp = (root / "IL2CPP_ANALYSIS_REPORT.md").read_text(encoding="utf-8")
    comparison = (root / "APK_VARIANT_COMPARISON.md").read_text(encoding="utf-8")
    plan = (root / "MOD_INTEGRATION_PLAN.md").read_text(encoding="utf-8")

    if "**Status:** INVENTORY_COMPLETE" not in static or "- CRC scan: PASS" not in static:
        raise BuildError("The static APK inventory is not clean and CRC-verified.")
    if "**Status:** CODE_ANALYSIS_PARTIAL" not in code and "**Status:** CODE_ANALYSIS_COMPLETE" not in code:
        raise BuildError("APK code analysis is missing or failed.")
    if "- Apktool exit code: 0" not in code:
        raise BuildError("APKTool must decode the current primary APK successfully.")
    if "- Full inner ZIP CRC/decompression scans passed for every extracted APK member." not in code:
        raise BuildError("The current primary and split APKs must pass inner ZIP CRC/decompression checks.")
    if "## Android Activity entry-point trace" not in code:
        raise BuildError("The Android Activity entry-point trace is missing.")
    if "outer CRC: FAIL" in code or "outer XAPK CRC=FAIL" in code or "read failed (" in code:
        raise BuildError("Code analysis still reports an unreadable or CRC-failing package member.")
    if "APKPure source-integrity assessment: PASS:" not in comparison:
        raise BuildError("APK variant comparison does not confirm current APKPure source integrity.")
    if "Primary APK outer CRC: FAIL" in il2cpp or "ARM64 split outer CRC: FAIL" in il2cpp:
        raise BuildError("The IL2CPP report indicates an outer APK member CRC failure.")
    if "Primary APK inner CRC scan: PASS" not in il2cpp or "ARM64 split inner CRC scan: PASS" not in il2cpp:
        raise BuildError("The IL2CPP source inputs have not both passed inner CRC validation.")
    if "STATIC_ENTRYPOINT_MAPPED" not in plan:
        raise BuildError("The Activity integration plan is missing its static entry-point status.")
    require_approval(root / "MOD_CANDIDATES.md")


def run(command: Sequence[str], label: str) -> None:
    try:
        result = subprocess.run(list(command), text=True, capture_output=True, check=False)
    except OSError as error:
        raise BuildError(f"{label} could not start: {error}") from error
    if result.returncode != 0:
        details = (result.stdout + "\n" + result.stderr).strip()
        raise BuildError(f"{label} failed with exit {result.returncode}:\n{details[-6000:]}")


def download_tool(url: str, destination: Path) -> Path:
    request = urllib.request.Request(url, headers={"User-Agent": "CHATGPT-MOD-build-tool/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as output:
            shutil.copyfileobj(response, output, length=1024 * 1024)
    except OSError as error:
        raise BuildError(f"Could not download pinned build tool {url}: {error}") from error
    if not destination.is_file() or destination.stat().st_size == 0:
        raise BuildError(f"Downloaded tool is empty: {destination}")
    return destination


def discover_library_members(split_apks: Sequence[Path]) -> list[tuple[Path, str]]:
    libraries: list[tuple[Path, str]] = []
    seen_paths: set[str] = set()
    allowed_abis = {"arm64-v8a"}
    for split in split_apks:
        with zipfile.ZipFile(split, "r") as archive:
            for info in archive.infolist():
                if info.is_dir() or not info.filename.endswith(".so") or not info.filename.startswith("lib/"):
                    continue
                parts = PurePosixPath(info.filename).parts
                if len(parts) != 3:
                    raise BuildError(f"Unexpected native-library path in split: {info.filename}")
                abi = parts[1]
                if abi not in allowed_abis:
                    raise BuildError(
                        f"This single-APK prototype only supports the ARM64 source split; found ABI {abi!r}."
                    )
                if info.filename in seen_paths:
                    raise BuildError(f"Duplicate native-library path across splits: {info.filename}")
                seen_paths.add(info.filename)
                libraries.append((split, info.filename))
    required = {
        "lib/arm64-v8a/libduel.so",
        "lib/arm64-v8a/libil2cpp.so",
        "lib/arm64-v8a/libunity.so",
    }
    missing = sorted(required - seen_paths)
    if missing:
        raise BuildError("Required ARM64 native libraries are missing: " + ", ".join(missing))
    return sorted(libraries, key=lambda item: item[1])


def copy_split_libraries(split_apks: Sequence[Path], decoded_dir: Path) -> int:
    """Merge validated ARM64 split libraries into the rebuilt single-APK prototype."""
    libraries = discover_library_members(split_apks)
    destination_root = decoded_dir / "lib" / "arm64-v8a"
    destination_root.mkdir(parents=True, exist_ok=True)
    copied = 0
    for split, member_name in libraries:
        destination = destination_root / PurePosixPath(member_name).name
        with zipfile.ZipFile(split, "r") as archive:
            data = archive.read(member_name)
        if destination.exists():
            if destination.read_bytes() != data:
                raise BuildError(f"Refusing to overwrite a different native library: {destination}")
            continue
        destination.write_bytes(data)
        copied += 1
    return copied


def compile_menu_dex(java_source: Path, class_dir: Path, dex_dir: Path,
                     android_jar: Path, d8: Path, javac: str, java: str) -> Path:
    if not java_source.is_file():
        raise BuildError(f"Menu source file is missing: {java_source}")
    if not android_jar.is_file():
        raise BuildError(f"Android platform android.jar was not found: {android_jar}")
    class_dir.mkdir(parents=True, exist_ok=True)
    dex_dir.mkdir(parents=True, exist_ok=True)
    run([
        javac, "-source", "8", "-target", "8",
        "-classpath", str(android_jar),
        "-d", str(class_dir), str(java_source),
    ], "Compile CHATGPT MOD Java helper")
    class_files = sorted(class_dir.rglob("*.class"))
    if not class_files:
        raise BuildError("Java compilation produced no class files.")
    run([
        str(d8), "--lib", str(android_jar), "--min-api", "21",
        "--output", str(dex_dir), *[str(path) for path in class_files],
    ], "Convert CHATGPT MOD helper classes to DEX")
    dex_files = sorted(dex_dir.glob("classes*.dex"))
    if len(dex_files) != 1 or dex_files[0].name != "classes.dex":
        raise BuildError(
            "The helper must fit in exactly one DEX file; got "
            + ", ".join(path.name for path in dex_files)
        )
    return dex_files[0]


def add_helper_dex(apk_path: Path, helper_dex: Path, dex_name: str) -> None:
    if not re.fullmatch(r"classes(?:[2-9]|[1-9][0-9]+)\.dex", dex_name) or dex_name == "classes.dex":
        raise BuildError(f"Unexpected helper DEX name: {dex_name}")
    with zipfile.ZipFile(apk_path, "a", compression=zipfile.ZIP_STORED) as archive:
        if dex_name in archive.namelist():
            raise BuildError(f"Refusing to overwrite existing DEX entry {dex_name}.")
        archive.write(helper_dex, dex_name)


def next_dex_name(apk_path: Path) -> str:
    with zipfile.ZipFile(apk_path, "r") as archive:
        numbers: list[int] = []
        for name in archive.namelist():
            if name == "classes.dex":
                numbers.append(1)
            else:
                match = re.fullmatch(r"classes([2-9]|[1-9][0-9]+)\.dex", name)
                if match:
                    numbers.append(int(match.group(1)))
        number = max(numbers, default=0) + 1
    if number < 2:
        number = 2
    return f"classes{number}.dex"


def build(args: argparse.Namespace) -> dict[str, str]:
    root = Path(args.repo_root).resolve()
    check_reports(root)

    if args.base_release_tag != "APKPure_Latest":
        raise BuildError("Only APKPure_Latest is allowed as the source base.")
    if not args.repo or "/" not in args.repo:
        raise BuildError("Repository must be supplied in owner/name form.")
    if not args.output:
        raise BuildError("An output path is required.")
    if not args.android_jar or not args.d8 or not args.zipalign or not args.apksigner:
        raise BuildError("Android platform jar, d8, zipalign and apksigner paths are required.")
    if not args.keystore or not args.key_alias:
        raise BuildError("A signing keystore and key alias must be supplied explicitly.")
    store_password = os.environ.get(args.store_password_env, "")
    key_password = os.environ.get(args.key_password_env, "")
    if not store_password or not key_password:
        raise BuildError("Signing password environment variables are missing; refusing an unsigned artifact.")

    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    android_jar = Path(args.android_jar).resolve()
    d8 = Path(args.d8).resolve()
    zipalign = Path(args.zipalign).resolve()
    apksigner = Path(args.apksigner).resolve()
    keystore = Path(args.keystore).resolve()
    for tool in (d8, zipalign, apksigner):
        if not tool.is_file():
            raise BuildError(f"Android build tool not found: {tool}")
    if not keystore.is_file():
        raise BuildError(f"Signing keystore not found: {keystore}")

    release = get_release(args.repo, args.base_release_tag)
    asset = select_release_asset(release, args.asset_name)
    asset_name = str(asset.get("name", ""))
    if not asset_name.lower().endswith(".xapk"):
        raise BuildError("APKPure_Latest must supply the original XAPK for split-aware processing.")
    asset_url = asset.get("browser_download_url")
    if not isinstance(asset_url, str) or not asset_url:
        raise BuildError("The APKPure Release does not expose a downloadable XAPK URL.")

    with tempfile.TemporaryDirectory(prefix="chatgpt-mod-build-") as temporary:
        work = Path(temporary)
        container = work / asset_name
        download_size, container_hash = download_and_hash(asset_url, container)
        expected_size = int(asset.get("size", -1))
        expected_digest = str(asset.get("digest", "")).strip()
        if download_size != expected_size:
            raise BuildError(
                f"Downloaded XAPK size {download_size} does not match Release metadata {expected_size}."
            )
        if not expected_digest:
            raise BuildError(
                "The APKPure Release API did not provide a SHA-256 digest; refusing to build without a source digest."
            )
        normalized = expected_digest.removeprefix("sha256:").lower()
        if not re.fullmatch(r"[0-9a-f]{64}", normalized) or container_hash != normalized:
            raise BuildError("Downloaded APKPure XAPK SHA-256 does not match the Release digest.")
        verify_zip(container, "APKPure XAPK container")

        primary, primary_name, members, obbs = resolve_primary_apk(container, asset_name, work / "primary.apk")
        if obbs:
            raise BuildError("The current build path expects no OBB payload; found: " + ", ".join(obbs))
        primary_member = next((item for item in members if item["name"] == primary_name), None)
        if primary_member and primary_member.get("container_crc_status") != "PASS":
            raise BuildError("Primary APK member outer XAPK CRC does not pass.")
        verify_zip(primary, "APKPure primary APK", require_manifest=True)

        split_paths: list[Path] = []
        for index, member in enumerate(members):
            if member["name"] == primary_name:
                continue
            member_name = str(member["name"])
            if not member_name.lower().endswith(".apk"):
                continue
            split_path = work / "splits" / f"split-{index}-{PurePosixPath(member_name).name}"
            split_result = extract_xapk_member(container, member_name, split_path)
            if split_result["container_crc_status"] != "PASS":
                raise BuildError(f"Embedded split outer CRC failed: {member_name}")
            verify_zip(split_path, f"Embedded split {member_name}", require_manifest=True)
            split_paths.append(split_path)
        if not split_paths:
            raise BuildError("No configuration split APK was found; refusing to assume the primary APK is complete.")

        apktool_jar = Path(args.apktool_jar).resolve() if args.apktool_jar else work / "apktool.jar"
        if not apktool_jar.is_file():
            download_tool(APKTOOL_URL, apktool_jar)

        decoded = work / "decoded"
        run([args.java, "-jar", str(apktool_jar), "d", "-f", str(primary), "-o", str(decoded)],
            "Decode APKPure primary APK")
        decoded_manifest = decoded / "AndroidManifest.xml"
        package_name = parse_package(decoded_manifest)
        if package_name != EXPECTED_PACKAGE:
            raise BuildError(
                f"Decoded package name was {package_name!r}; expected {EXPECTED_PACKAGE!r}."
            )

        copied_libraries = copy_split_libraries(split_paths, decoded)
        activities = list(decoded.rglob(ACTIVITY_SMALI))
        if len(activities) != 1:
            raise BuildError(
                f"Expected one decoded {ACTIVITY_SMALI}; found {len(activities)}."
            )
        patch_activity_smali(activities[0])

        java_source = root / "src" / "mod_menu" / "com" / "chatgptmod" / "menu" / "ModMenu.java"
        class_dir = work / "helper-classes"
        dex_dir = work / "helper-dex"
        helper_dex = compile_menu_dex(java_source, class_dir, dex_dir, android_jar, d8, args.javac, args.java)

        unsigned = work / "unsigned.apk"
        run([args.java, "-jar", str(apktool_jar), "b", str(decoded), "-o", str(unsigned)],
            "Rebuild APKPure primary APK with menu hook")
        verify_zip(unsigned, "Rebuilt unsigned APK", require_manifest=True)
        helper_entry = next_dex_name(unsigned)
        add_helper_dex(unsigned, helper_dex, helper_entry)

        # Align before signing. The signing key is supplied by the operator and is
        # not copied into this repository or written to the build report.
        aligned = work / "aligned.apk"
        run([str(zipalign), "-f", "-p", "4", str(unsigned), str(aligned)], "Align rebuilt APK")
        sign_command = [
            str(apksigner), "sign",
            "--ks", str(keystore),
            "--ks-key-alias", args.key_alias,
            "--ks-pass", f"env:{args.store_password_env}",
            "--key-pass", f"env:{args.key_password_env}",
            "--out", str(output),
            str(aligned),
        ]
        run(sign_command, "Sign CHATGPT MOD test APK")
        run([str(apksigner), "verify", "--verbose", "--print-certs", str(output)],
            "Verify APK signature")
        verify_zip(output, "Signed CHATGPT MOD APK", require_manifest=True)

        return {
            "asset_name": asset_name,
            "container_sha256": container_hash,
            "container_size": str(download_size),
            "primary_apk": primary_name,
            "package_name": package_name,
            "copied_arm64_libraries": str(copied_libraries),
            "helper_dex_entry": helper_entry,
            "output_path": str(output),
            "output_size": str(output.stat().st_size),
            "output_sha256": sha256_file(output),
            "signing_note": "Signed with an explicitly supplied key; in-place update compatibility must be tested separately.",
        }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="GitHub repository owner/name.")
    parser.add_argument("--base-release-tag", required=True, help="Must be APKPure_Latest.")
    parser.add_argument("--asset-name", default="", help="Exact XAPK asset name if the Release has multiple APK/XAPK assets.")
    parser.add_argument("--output", required=True, help="Destination for the signed test APK.")
    parser.add_argument("--repo-root", default=".", help="Repository root containing reports and source files.")
    parser.add_argument("--android-jar", default=os.environ.get("ANDROID_JAR", ""), help="Android platform android.jar.")
    parser.add_argument("--d8", default=os.environ.get("D8", ""), help="Path to Android SDK d8 executable.")
    parser.add_argument("--zipalign", default=os.environ.get("ZIPALIGN", ""), help="Path to Android SDK zipalign executable.")
    parser.add_argument("--apksigner", default=os.environ.get("APKSIGNER", ""), help="Path to Android SDK apksigner executable.")
    parser.add_argument("--keystore", default=os.environ.get("MOD_SIGNING_KEYSTORE", ""), help="Explicit signing keystore path.")
    parser.add_argument("--key-alias", default=os.environ.get("MOD_SIGNING_KEY_ALIAS", ""), help="Signing key alias.")
    parser.add_argument("--store-password-env", default="MOD_SIGNING_STORE_PASSWORD", help="Environment variable containing keystore password.")
    parser.add_argument("--key-password-env", default="MOD_SIGNING_KEY_PASSWORD", help="Environment variable containing key password.")
    parser.add_argument("--apktool-jar", default="", help="Optional path to a local Apktool jar; otherwise pinned Apktool is downloaded.")
    parser.add_argument("--java", default="java", help="Java executable.")
    parser.add_argument("--javac", default="javac", help="Java compiler executable.")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        summary = build(args)
    except (BuildError, OSError, RuntimeError, ValueError) as error:
        print(f"CHATGPT MOD build blocked/failed: {error}", file=sys.stderr)
        return 2
    print("CHATGPT MOD test APK built and verified:")
    for key, value in summary.items():
        print(f"- {key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
