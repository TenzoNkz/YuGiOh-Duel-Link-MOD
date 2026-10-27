import io
import struct
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from apk_inputs import extract_xapk_member, resolve_primary_apk, select_release_asset


def fake_apk_bytes(entries: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in entries.items():
            archive.writestr(name, data)
    return buffer.getvalue()


class ApkInputTests(unittest.TestCase):
    def test_select_release_asset_accepts_apk_and_xapk(self) -> None:
        release = {"assets": [
            {"name": "notes.txt"},
            {"name": "YuGiOh.xapk"},
        ]}
        self.assertEqual(select_release_asset(release)["name"], "YuGiOh.xapk")

    def test_xapk_prefers_main_game_apk_over_config_split(self) -> None:
        primary = fake_apk_bytes({
            "AndroidManifest.xml": b"test-manifest",
            "classes.dex": b"dex-bytes",
            "lib/arm64-v8a/libil2cpp.so": b"native",
        })
        config = fake_apk_bytes({"AndroidManifest.xml": b"split-manifest"})
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            container = root / "input.xapk"
            with zipfile.ZipFile(container, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("com.konami.duellinks.apk", primary)
                archive.writestr("config.arm64_v8a.apk", config)
                archive.writestr("Android/obb/main.obb", b"obb")
            selected, name, members, obbs = resolve_primary_apk(
                container, "input.xapk", root / "selected.apk"
            )
            self.assertEqual(name, "com.konami.duellinks.apk")
            self.assertEqual(selected.stat().st_size, len(primary))
            self.assertEqual(len(members), 2)
            selected_member = next(item for item in members if item["name"] == name)
            self.assertEqual(selected_member["container_crc_status"], "PASS")
            self.assertEqual(obbs, ["Android/obb/main.obb"])
            with zipfile.ZipFile(selected, "r") as apk:
                self.assertIn("classes.dex", apk.namelist())

    def test_xapk_with_bad_outer_member_crc_is_reported_but_inner_apk_is_readable(self) -> None:
        primary = fake_apk_bytes({
            "AndroidManifest.xml": b"test-manifest",
            "classes.dex": b"dex-bytes",
        })
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            container = root / "bad-crc.xapk"
            with zipfile.ZipFile(container, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("jp.konami.duellinks.apk", primary)
                archive.writestr("config.arm64_v8a.apk", fake_apk_bytes({"AndroidManifest.xml": b"split"}))
            damaged = bytearray(container.read_bytes())
            marker = b"PK\x01\x02"
            index = 0
            changed = False
            while True:
                index = damaged.find(marker, index)
                if index < 0:
                    break
                name_length = struct.unpack_from("<H", damaged, index + 28)[0]
                name_start = index + 46
                member_name = bytes(damaged[name_start:name_start + name_length]).decode("utf-8")
                if member_name == "jp.konami.duellinks.apk":
                    damaged[index + 16] ^= 0x01
                    changed = True
                    break
                index += 4
            self.assertTrue(changed, "test fixture must contain the primary APK central-directory entry")
            container.write_bytes(damaged)
            selected, name, members, _ = resolve_primary_apk(
                container, "bad-crc.xapk", root / "selected.apk"
            )
            status = next(item for item in members if item["name"] == name)["container_crc_status"]
            self.assertEqual(status, "FAIL")
            with zipfile.ZipFile(selected, "r") as apk:
                self.assertIn("classes.dex", apk.namelist())
                self.assertIsNone(apk.testzip())

    def test_extract_xapk_split_reports_outer_crc(self) -> None:
        primary = fake_apk_bytes({"AndroidManifest.xml": b"base"})
        config = fake_apk_bytes({
            "AndroidManifest.xml": b"config",
            "lib/arm64-v8a/libgame.so": b"native-library",
        })
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            container = root / "package.xapk"
            with zipfile.ZipFile(container, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("jp.konami.duellinks.apk", primary)
                archive.writestr("config.arm64_v8a.apk", config)
            extracted = extract_xapk_member(container, "config.arm64_v8a.apk", root / "config.apk")
            self.assertEqual(extracted["container_crc_status"], "PASS")
            self.assertEqual(extracted["size"], len(config))
            with zipfile.ZipFile(root / "config.apk", "r") as apk:
                self.assertIn("lib/arm64-v8a/libgame.so", apk.namelist())

    def test_plain_apk_is_passed_through_without_extraction(self) -> None:
        payload = fake_apk_bytes({"AndroidManifest.xml": b"manifest"})
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            original = root / "original.apk"
            original.write_bytes(payload)
            selected, name, members, obbs = resolve_primary_apk(
                original, "original.apk", root / "unused.apk"
            )
            self.assertEqual(selected, original)
            self.assertEqual(name, "original.apk")
            self.assertEqual(members, [])
            self.assertEqual(obbs, [])


if __name__ == "__main__":
    unittest.main()
