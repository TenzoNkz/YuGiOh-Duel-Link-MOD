import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from build_chatgpt_mod import (
    BuildError,
    check_reports,
    copy_split_libraries,
    next_dex_name,
    patch_activity_smali,
    require_approval,
    verify_zip,
)


class SmaliInjectionTests(unittest.TestCase):
    def test_inserts_menu_call_after_super_on_create(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "YgomMainActivity.smali"
            path.write_text(
                ".class public Ljp/konami/duellinks/plugins/YgomMainActivity;\n"
                ".super Lcom/google/firebase/MessagingUnityPlayerActivity;\n"
                "\n"
                ".method protected onCreate(Landroid/os/Bundle;)V\n"
                "    .locals 2\n"
                "    invoke-super {p0, p1}, Lcom/google/firebase/MessagingUnityPlayerActivity;->onCreate(Landroid/os/Bundle;)V\n"
                "    return-void\n"
                ".end method\n",
                encoding="utf-8",
            )
            changed = patch_activity_smali(path)
            patched = path.read_text(encoding="utf-8")
        self.assertTrue(changed)
        super_call = "invoke-super {p0, p1}, Lcom/google/firebase/MessagingUnityPlayerActivity;->onCreate(Landroid/os/Bundle;)V"
        self.assertIn(super_call + "\n    invoke-static {p0}, Lcom/chatgptmod/menu/ModMenu;->install(Landroid/app/Activity;)V", patched)
        self.assertEqual(patched.count("Lcom/chatgptmod/menu/ModMenu;->install("), 1)

    def test_refuses_duplicate_injection(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "YgomMainActivity.smali"
            path.write_text(
                ".method protected onCreate(Landroid/os/Bundle;)V\n"
                "    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V\n"
                "    invoke-static {p0}, Lcom/chatgptmod/menu/ModMenu;->install(Landroid/app/Activity;)V\n"
                ".end method\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(BuildError, "already present"):
                patch_activity_smali(path)

    def test_refuses_unexpected_on_create_structure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "YgomMainActivity.smali"
            path.write_text(
                ".method protected onCreate(Landroid/os/Bundle;)V\n"
                "    return-void\n"
                ".end method\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(BuildError, "superclass onCreate"):
                patch_activity_smali(path)


class BuildPreconditionTests(unittest.TestCase):
    def test_build_approval_fails_closed_even_if_marker_is_mentioned_in_prose(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "MOD_CANDIDATES.md"
            path.write_text(
                "**Build approval: PENDING_REVERSE_ENGINEERING**\n\n"
                "The build tool requires the exact marker "
                "Build approval: APPROVED_FOR_IMPLEMENTATION before a build.\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(BuildError, "still pending"):
                require_approval(path)
            path.write_text(
                "**Build approval: APPROVED_FOR_IMPLEMENTATION**\n",
                encoding="utf-8",
            )
            require_approval(path)

    def test_crc_check_accepts_clean_zip_and_rejects_bad_container(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            good = Path(temporary) / "good.apk"
            with zipfile.ZipFile(good, "w") as archive:
                archive.writestr("AndroidManifest.xml", b"manifest")
            verify_zip(good, "fixture", require_manifest=True)

            bad = Path(temporary) / "bad.apk"
            bad.write_bytes(b"not a zip")
            with self.assertRaisesRegex(BuildError, "valid readable ZIP"):
                verify_zip(bad, "fixture")

    def test_report_gate_accepts_only_clean_reports_and_explicit_approval(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "APP_ANALYSIS_REPORT.md").write_text(
                "**Status:** INVENTORY_COMPLETE\n- CRC scan: PASS\n", encoding="utf-8"
            )
            (root / "APK_CODE_ANALYSIS.md").write_text(
                "**Status:** CODE_ANALYSIS_PARTIAL\n"
                "- Apktool exit code: 0\n"
                "- Full inner ZIP CRC/decompression scans passed for every extracted APK member.\n"
                "## Android Activity entry-point trace\n",
                encoding="utf-8",
            )
            (root / "IL2CPP_ANALYSIS_REPORT.md").write_text(
                "- Primary APK outer CRC: PASS\n"
                "- ARM64 split outer CRC: PASS\n"
                "- Primary APK inner CRC scan: PASS\n"
                "- ARM64 split inner CRC scan: PASS\n",
                encoding="utf-8",
            )
            (root / "APK_VARIANT_COMPARISON.md").write_text(
                "- APKPure source-integrity assessment: PASS: Release digest matched; "
                "embedded APK outer CRCs and per-entry reads passed.\n",
                encoding="utf-8",
            )
            (root / "MOD_INTEGRATION_PLAN.md").write_text(
                "**Status:** STATIC_ENTRYPOINT_MAPPED; RUNTIME_INTEGRATION_NOT_TESTED\n",
                encoding="utf-8",
            )
            candidates = root / "MOD_CANDIDATES.md"
            candidates.write_text(
                "**Build approval: APPROVED_FOR_IMPLEMENTATION**\n",
                encoding="utf-8",
            )
            check_reports(root)

            # Even with otherwise clean reports, explanatory prose is not approval.
            candidates.write_text(
                "**Build approval: PENDING_REVERSE_ENGINEERING**\n"
                "Required marker: Build approval: APPROVED_FOR_IMPLEMENTATION\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(BuildError, "still pending"):
                check_reports(root)

    def test_next_dex_name_uses_next_available_index(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "base.apk"
            with zipfile.ZipFile(path, "w") as archive:
                for name in ("classes.dex", "classes2.dex", "classes3.dex"):
                    archive.writestr(name, b"fixture")
            self.assertEqual(next_dex_name(path), "classes4.dex")

    def test_split_libraries_are_copied_only_from_arm64_layout(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            split = Path(temporary) / "config.arm64_v8a.apk"
            with zipfile.ZipFile(split, "w") as archive:
                for name in (
                    "lib/arm64-v8a/libduel.so",
                    "lib/arm64-v8a/libil2cpp.so",
                    "lib/arm64-v8a/libunity.so",
                ):
                    archive.writestr(name, name.encode("ascii"))
            decoded = Path(temporary) / "decoded"
            count = copy_split_libraries([split], decoded)
            self.assertEqual(count, 3)
            self.assertEqual(
                (decoded / "lib" / "arm64-v8a" / "libduel.so").read_bytes(),
                b"lib/arm64-v8a/libduel.so",
            )


if __name__ == "__main__":
    unittest.main()
