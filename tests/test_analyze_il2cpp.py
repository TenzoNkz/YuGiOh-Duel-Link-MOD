import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from analyze_il2cpp import archive_integrity, classify_dumper_result


class Il2CppDumperClassificationTests(unittest.TestCase):
    def test_clean_dump_is_complete(self) -> None:
        log = "Dumping...\nDone!\nGenerate dummy dll\nDone!"
        marker, console_error, status = classify_dumper_result(0, True, log)
        self.assertTrue(marker)
        self.assertFalse(console_error)
        self.assertEqual(status, "IL2CPP_DUMP_COMPLETE")

    def test_console_prompt_error_after_outputs_is_recorded_without_crashing(self) -> None:
        log = (
            "Dumping...\nDone!\nGenerate dummy dll\nDone!\n"
            "Press any key to exit\nUnhandled exception: Console.ReadKey"
        )
        marker, console_error, status = classify_dumper_result(-6, True, log)
        self.assertTrue(marker)
        self.assertTrue(console_error)
        self.assertEqual(status, "IL2CPP_OUTPUTS_GENERATED_WITH_POST_DUMP_CONSOLE_ERROR")

    def test_nonzero_exit_without_all_outputs_is_partial(self) -> None:
        marker, console_error, status = classify_dumper_result(1, False, "Dumping...")
        self.assertFalse(marker)
        self.assertFalse(console_error)
        self.assertEqual(status, "IL2CPP_DUMP_PARTIAL")

    def test_nonzero_exit_with_generated_outputs_but_no_console_error_is_warning(self) -> None:
        log = "Dumping...\nGenerate dummy dll\nwarning: recoverable metadata issue"
        marker, console_error, status = classify_dumper_result(1, True, log)
        self.assertTrue(marker)
        self.assertFalse(console_error)
        self.assertEqual(status, "IL2CPP_OUTPUTS_GENERATED_WITH_TOOL_WARNING")


class ArchiveIntegrityTests(unittest.TestCase):
    def test_valid_zip_archive_passes_crc_scan(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "valid.apk"
            with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("assets/test.bin", b"verified test payload")
            status, detail = archive_integrity(archive_path)
        self.assertEqual(status, "PASS")
        self.assertEqual(detail, "all archive entries passed")

    def test_invalid_zip_archive_fails_cleanly(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "invalid.apk"
            archive_path.write_bytes(b"not a ZIP archive")
            status, detail = archive_integrity(archive_path)
        self.assertEqual(status, "FAIL")
        self.assertIn("BadZipFile", detail)


if __name__ == "__main__":
    unittest.main()
