# Memory Index

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main

## Locked source direction
- APKPure Original V11.1.0: sole intended modification base (Release tag APKPure_Latest).
- Platinmods V11.1.0: comparison-only reference (Release tag Latest).
- Intended deliverable: modified APK, with in-game menu title CHATGPT MOD.
- Reverse engineering must be reviewed before feature selection or final build.

## Read in this order
1. CHAT_TRANSFER.md
2. CHAT_RULES.md
3. PROJECT_STATE.md
4. HANDOVER.md
5. CHATGPT_MOD_BUILD_REPORT.md
6. APP_ANALYSIS_REPORT.md
7. APK_CODE_ANALYSIS.md
8. APK_VARIANT_COMPARISON.md
9. MOD_CANDIDATES.md
10. ANALYSIS_LOG.md
11. README.md

## GitHub workflows
- APK Static Analysis: .github/workflows/apk-static-analysis.yml — defaults to APKPure_Latest.
- APK Code Analysis (APKPure Base): .github/workflows/apk-code-analysis.yml — decompiles APKPure primary APK, then compares it against Platinmods.
- Checkpoint Validation: .github/workflows/checkpoint-validation.yml — compiles tools and runs local unit tests.
- CHATGPT Mod Build: .github/workflows/build-chatgpt-mod.yml — must remain blocked until approved APKPure-based patch/build tooling is present.

## Scripts and reports
- tools/apk_inputs.py — Release API, asset download, primary APK selection from APK/XAPK, and member hashing.
- tools/analyze_release_apk.py — archive integrity and primary-APK inventory.
- tools/analyze_apk_code.py — Apktool/JADX and native/IL2CPP string scan on the selected APKPure primary APK.
- tools/compare_apk_variants.py — per-entry SHA-256 comparison: APKPure base versus Platinmods reference.
- tests/test_apk_inputs.py — local test coverage for input selection and XAPK primary member handling.
- APP_ANALYSIS_REPORT.md — static package inventory.
- APK_CODE_ANALYSIS.md — code-level static analysis with explicit tool limitations.
- APK_VARIANT_COMPARISON.md — file-level comparison between base and reference.
- MOD_CANDIDATES.md — feature evidence/status.
- CHATGPT_MOD_BUILD_REPORT.md — build status/blockers.

## Persistence contract
Committed GitHub records, Release metadata and verified Actions outputs are durable project state. New chats must reload the live main branch, latest reports and Actions outcomes, then continue from HANDOVER.md. Never report a build/test as successful without verifying its real output.
