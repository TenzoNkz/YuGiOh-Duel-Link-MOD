import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from analyze_apk_code import archive_crc_status, summarize_android_entrypoint


class ApkCodeArchiveIntegrityTests(unittest.TestCase):
    def test_activity_entrypoint_summary_finds_lifecycle_and_native_calls(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            source_root = Path(temporary) / "sources"
            package_dir = source_root / "jp" / "konami" / "duellinks" / "plugins"
            package_dir.mkdir(parents=True)
            (package_dir / "YgomMainActivity.java").write_text(
                "\n".join([
                    "package jp.konami.duellinks.plugins;",
                    "public class YgomMainActivity extends Activity {",
                    "  protected void onCreate(Bundle state) {",
                    "    super.onCreate(state);",
                    "    System.loadLibrary(\"duel\");",
                    "    setContentView(new View(this));",
                    "  }",
                    "  public void onResume() { super.onResume(); }",
                    "}",
                ]) + "\n",
                encoding="utf-8",
            )
            summary = summarize_android_entrypoint(source_root)
        joined = "\\n".join(summary)
        self.assertIn("YgomMainActivity.java", joined)
        self.assertIn("onCreate", joined)
        self.assertIn("loadLibrary", joined)
        self.assertIn("setContentView", joined)

    def test_missing_activity_entrypoint_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            summary = summarize_android_entrypoint(Path(temporary))
        self.assertTrue(any("not present" in line for line in summary))

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
