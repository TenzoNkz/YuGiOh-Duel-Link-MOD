# Memory Index

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main

## Locked source direction
- APKPure Original V11.1.0 is the sole intended modification base (Release tag APKPure_Latest).
- Platinmods V11.1.0 is comparison-only reference (Release tag Latest).
- Intended deliverable: a real modified APK, with in-game menu title CHATGPT MOD.
- Reverse engineering and source integrity must be reviewed before feature selection or final build.

## Read in this order
1. CHAT_TRANSFER.md
2. CHAT_RULES.md
3. PROJECT_STATE.md
4. HANDOVER.md
5. CHATGPT_MOD_BUILD_REPORT.md
6. APP_ANALYSIS_REPORT.md
7. APK_CODE_ANALYSIS.md
8. IL2CPP_ANALYSIS_REPORT.md
9. APK_VARIANT_COMPARISON.md
10. MOD_CANDIDATES.md
11. ANALYSIS_LOG.md
12. README.md

## GitHub workflows
- APK Static Analysis: .github/workflows/apk-static-analysis.yml — defaults to APKPure_Latest; inventories primary APK and embedded split APKs.
- APK Code Analysis (APKPure Base): .github/workflows/apk-code-analysis.yml — runs Apktool/JADX on the primary APK, inventories native libraries in readable splits, compares aggregate package entries against Platinmods, and attempts pinned IL2CPP metadata recovery.
- Checkpoint Validation: .github/workflows/checkpoint-validation.yml — compiles tools and runs local unit tests.
- CHATGPT MOD Build: .github/workflows/build-chatgpt-mod.yml — remains blocked until a clean base package, approved feature plan and actual APKPure-based patch/build tool are present.

## Scripts and reports
- tools/apk_inputs.py — Release API, asset download, safe primary/split member extraction and CRC reporting.
- tools/analyze_release_apk.py — static integrity and structural inventory for APK/XAPK, including embedded config/split APK details.
- tools/analyze_apk_code.py — Apktool/JADX and native/IL2CPP string analysis for the APKPure primary APK and readable splits.
- tools/analyze_il2cpp.py — pinned Il2CppDumper attempt using the APKPure ARM64 library and metadata.
- tools/compare_apk_variants.py — aggregate primary + split APK payload comparison: APKPure base versus Platinmods reference.
- tests/test_apk_inputs.py — APK/XAPK selection, split extraction, OBB inventory, and CRC mismatch handling.
- APP_ANALYSIS_REPORT.md — archive, checksum and split-integrity inventory.
- APK_CODE_ANALYSIS.md — manifest, DEX/Java, split-native and string-analysis report.
- IL2CPP_ANALYSIS_REPORT.md — type/method metadata recovery attempt and focused symbols.
- APK_VARIANT_COMPARISON.md — byte-level package comparison and integrity warnings.
- MOD_CANDIDATES.md — candidate evidence and feasibility status.
- CHATGPT_MOD_BUILD_REPORT.md — true build state and blockers.

## Current integrity warning
The currently uploaded APKPure XAPK container digest matches GitHub metadata, but embedded APK member CRCs fail. The primary APK has an invalid compressed asset entry and the ARM64 config split has an unreadable libduel.so entry. Do not patch/build from this upload until a clean original package replaces it and the analysis passes.

## Persistence contract
Committed GitHub records, Release metadata and verified Actions outputs are durable project state. New chats must reload live main, latest reports and Actions outcomes, then continue from HANDOVER.md. Never report a test/build as successful without checking its real output.
