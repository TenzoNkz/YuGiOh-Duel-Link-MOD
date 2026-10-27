import io
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from apk_inputs import resolve_primary_apk, select_release_asset


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
            self.assertEqual(obbs, ["Android/obb/main.obb"])
            with zipfile.ZipFile(selected, "r") as apk:
                self.assertIn("classes.dex", apk.namelist())

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
