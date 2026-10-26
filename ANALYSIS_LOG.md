# Analysis Log

This is the durable chronological record of decisions, evidence, workflow runs, failures, and next steps. Append entries after each meaningful verified milestone; do not record guesses as facts.

## 2026-10-26 — Source Release verified
- Confirmed public repository TenzoNkz/YuGiOh-Duel-Link-MOD, default branch main.
- Release: Platinmods Original, tag Platinmods_V11.0.0.
- Asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk, size 127,424,878 bytes.
- GitHub Release API SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.

## 2026-10-26 — Durable recovery system and structural inventory
- Added CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, MOD_CANDIDATES.md, and README.md.
- Added GitHub Actions for APK static inventory, APK code analysis, and checkpoint validation.
- Initial APK Static Analysis attempt generated a report but its push lost a race with a concurrent commit. Fixed the workflow to rebase before pushing.
- Successful static inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450.
- Verified downloaded size, matching SHA-256, ZIP open, and CRC scan. Found 3 DEX files, 20 native libraries, Unity/IL2CPP indicators, libduel.so, and libplatinmods.so.

## 2026-10-26 — Initial code-level static analysis
- Apktool 3.0.3 decoded the manifest to package jp.konami.duellinks and decoded 18,765 output entries.
- JADX 1.5.6 produced 8,194 Java files and reported 96 decompilation errors; the report status is partial.
- Decompiled Java includes Platinmods menu classes; PMLauncher loads platinmods.
- Native string evidence includes Java_com_platinmods_FloatingModMenuService_getFeatureList, settingsList, Java_com_platinmods_Preferences_Changes, and duel library names DLL_DuelGetDamageValue / DLL_DuelComCheatCard.
- These names are leads only. No call-site trace, runtime test, or online behavior verification has been completed.

## 2026-10-26 — Workflow and report refinements
- Fixed report-push concurrency by fetching and rebasing onto current main.
- Updated GitHub Actions pins to checkout v7.0.1 and setup-java v6.1.0.
- Refined the code-analysis script to separate Java/resource/native patterns, extract short context windows for key native strings, and restrict source tracing to exact com/platinmods class paths.
- Latest refined run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274001397.
- Latest checkpoint validation pass before that run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274001348.

## Next
Inspect run 40274001397 and its committed report. Trace the menu feature-list/preferences flow and update MOD_CANDIDATES.md one candidate at a time, recording exact evidence and limitations.
