import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from analyze_apk_code import archive_crc_status


class ApkCodeArchiveIntegrityTests(unittest.TestCase):
    def test_valid_apk_zip_passes_full_crc_scan(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "valid.apk"
            with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("AndroidManifest.xml", b"manifest-test")
                archive.writestr("assets/data.bin", b"payload" * 100)
            with zipfile.ZipFile(archive_path, "r") as archive:
                status, detail = archive_crc_status(archive)
        self.assertEqual(status, "PASS")
        self.assertEqual(detail, "all archive entries passed")

    def test_member_crc_mismatch_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "bad-crc.apk"
            with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("assets/data.bin", b"original payload")
            damaged = bytearray(archive_path.read_bytes())
            central = damaged.find(b"PK\x01\x02")
            self.assertGreaterEqual(central, 0)
            damaged[central + 16] ^= 0x01
            archive_path.write_bytes(damaged)
            with zipfile.ZipFile(archive_path, "r") as archive:
                status, detail = archive_crc_status(archive)
        self.assertEqual(status, "FAIL")
        self.assertIn("assets/data.bin", detail)


if __name__ == "__main__":
    unittest.main()
