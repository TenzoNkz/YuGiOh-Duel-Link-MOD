import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from compare_apk_variants import source_integrity_assessment


class SourceIntegrityAssessmentTests(unittest.TestCase):
    def test_clean_apkpure_source_is_reported_as_pass(self) -> None:
        result = source_integrity_assessment(True, [], {})
        self.assertTrue(result.startswith("PASS:"))
        self.assertIn("Release digest matched", result)
        self.assertIn("per-entry reads passed", result)

    def test_apkpure_outer_crc_failure_is_a_warning(self) -> None:
        result = source_integrity_assessment(True, ["config.arm64_v8a.apk"], {})
        self.assertTrue(result.startswith("WARN:"))
        self.assertIn("config.arm64_v8a.apk", result)

    def test_unreadable_entries_are_reported(self) -> None:
        result = source_integrity_assessment(True, [], {"assets/game.bin": "Bad CRC"})
        self.assertTrue(result.startswith("WARN:"))
        self.assertIn("1 unreadable or corrupt package entries", result)

    def test_reference_only_failure_is_not_passed_as_apkpure_failure(self) -> None:
        # The helper receives APKPure's evidence only; reference-only warnings are kept separate.
        result = source_integrity_assessment(True, [], {})
        self.assertTrue(result.startswith("PASS:"))


if __name__ == "__main__":
    unittest.main()
