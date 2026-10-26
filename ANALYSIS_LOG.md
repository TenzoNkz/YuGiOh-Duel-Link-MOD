# Analysis Log

This is the durable chronological record of verified findings, decisions, workflow runs, failures, and next steps. Avoid recording hypotheses as facts.

## 2026-10-26 — Release and archive integrity
- Confirmed public repo TenzoNkz/YuGiOh-Duel-Link-MOD and Release Platinmods Original, tag Platinmods_V11.0.0.
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk; size 127,424,878 bytes.
- GitHub API digest: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.
- Successful archive inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450. Downloaded size matched, SHA-256 matched, ZIP CRC scan passed.
- Archive contains 3,397 entries, three DEX files, 20 native libraries, Unity/IL2CPP indicators, libduel.so, and libplatinmods.so.

## 2026-10-26 — Durable GitHub recovery system
- Added CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, MOD_CANDIDATES.md, and README.md.
- Added GitHub Actions for APK static inventory, code analysis, and checkpoint validation.
- Transfer prompts instruct future chats to reload live repository, reports, Release metadata, and Actions status rather than relying on the old chat transcript.

## 2026-10-26 — Deep static-analysis findings
- Apktool 3.0.3 decoded package jp.konami.duellinks and 18,765 output entries.
- JADX 1.5.6 generated 8,194 Java sources, but exited with code 3 and reported 96 decompilation errors. Report remains partial.
- Latest successful code-analysis run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274382469.
- FloatingModMenuService.java contains generic UI widget/callback code; boolean toggles call Preferences.changeFeatureBoolean(...) and localChanges(...).
- Preferences.java declares native Changes(Context, int, int, boolean, String) and saves settings; PMLauncher.java loads platinmods.
- libplatinmods.so string evidence includes getFeatureList, settingsList, and Preferences_Changes.
- libduel.so/IL2CPP metadata include DLL_DuelGetDamageValue, DLL_DuelComCheatCard, PROCESS_DAMAGE variants, and ShowMonster/showMonster.
- The native strings are leads only; exact UI-label-to-feature-ID mapping, native call flow, runtime effects, and server authority are not yet verified.

## 2026-10-26 — Workflow reliability refinements
- Fixed report push conflicts by rebasing generated report commits onto the latest main branch.
- Added report-only conflict handling to APK Code Analysis.
- Refined the code scan to produce a concise trace for each of the key com/platinmods classes.
- Latest report was committed by code-analysis run 40274382469; the workflow succeeded while the report status remains partial.

## Next
Check Checkpoint Validation triggered after the latest report commit, then trace the native menu feature-list/dispatch path and update candidates one by one with clear evidence and limitations.
