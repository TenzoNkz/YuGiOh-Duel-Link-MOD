# APK Code Analysis Report

**Status:** PENDING_DEEP_STATIC_ANALYSIS  
**Source Release:** https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0

The first-stage inventory is in APP_ANALYSIS_REPORT.md. It verified the downloaded asset SHA-256 and archive CRCs, found three DEX files, Unity/IL2CPP indicators, both ARM ABIs, libduel.so, and libplatinmods.so.

This report is a bootstrap checkpoint only. It does not yet contain JADX decompilation or Apktool-decoded manifest findings.

## Next step
Run the GitHub Actions workflow named APK Code Analysis. It downloads pinned versions of JADX and Apktool, performs static decompilation/manifest decoding, scans decompiled Java/XML plus selected native/IL2CPP metadata strings, and commits the resulting report here.

## Limits
No APK is executed or installed. String hits and decompiled code references are leads, not proof that a toggle works. Runtime behavior, server-side authority, and compatibility are not validated by static analysis alone.
