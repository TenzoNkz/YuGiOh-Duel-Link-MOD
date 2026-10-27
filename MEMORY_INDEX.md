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
- CHATGPT MOD Build: .github/workflows/build-chatgpt-mod.yml — source integrity now passes; final build remains blocked until call-flow review, approved safe feature scope, XAPK/split plan and a genuine APKPure-based patch/build tool are present.

## Scripts and reports
- tools/apk_inputs.py — Release API, asset download, safe primary/split member extraction and CRC reporting.
- tools/analyze_release_apk.py — static integrity and structural inventory for APK/XAPK, including embedded config/split APK details.
- tools/analyze_apk_code.py — Apktool/JADX and native/IL2CPP string analysis for the APKPure primary APK and readable splits.
- tools/analyze_il2cpp.py — pinned Il2CppDumper attempt using the APKPure ARM64 library and metadata.
- tools/compare_apk_variants.py — aggregate primary + split APK payload comparison: APKPure base versus Platinmods reference.
- tests/test_apk_inputs.py — APK/XAPK selection, split extraction, OBB inventory, CRC mismatch handling and GitHub API token headers.
- tests/test_analyze_apk_code.py — full inner APK CRC scan and YgomMainActivity lifecycle/native/window trace.
- tests/test_analyze_il2cpp.py — archive integrity and Il2CppDumper output/status classification.
- tests/test_compare_apk_variants.py — dynamic APKPure source integrity assessment.
- APP_ANALYSIS_REPORT.md — archive, checksum and split-integrity inventory.
- APK_CODE_ANALYSIS.md — manifest, DEX/Java, split-native and string-analysis report.
- IL2CPP_ANALYSIS_REPORT.md — type/method metadata recovery attempt and focused symbols.
- APK_VARIANT_COMPARISON.md — byte-level package comparison and integrity warnings.
- MOD_CANDIDATES.md — candidate evidence and feasibility status.
- CHATGPT_MOD_BUILD_REPORT.md — true build state and blockers.

## Current source integrity and build status
The current APKPure XAPK (92,726,986 bytes) has SHA-256 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb. Its embedded primary APK and ARM64 split both pass outer CRC checks and full inner ZIP CRC/decompression scans. The former digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 refers to the previous corrupt upload and is superseded. Current report status is CODE_ANALYSIS_PARTIAL because JADX returns partial output with 96 decompilation errors; APKTool now returns exit code 0. The source-integrity blocker is resolved, but build remains blocked by incomplete call-flow validation, no approved safe feature scope, no genuine APKPure-based patcher, split/install strategy and signer/update compatibility.

## Latest workflow checkpoints
- Static archive integrity: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453605293 — success.
- Full code-analysis report and metadata recovery: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453733126 — success, with the corrected current Release digest and inner archive CRC checks in the IL2CPP report.
- Checkpoint/unit validation: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454118233 — success after the ZIP-signature regression-test correction.
- The enhanced APK Code Analysis run at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454023712 refreshes the report with full inner ZIP CRC checks and should be checked for its final result before the next checkpoint is declared complete.

## Persistence contract
Committed GitHub records, Release metadata and verified Actions outputs are durable project state. New chats must reload live main, latest reports and Actions outcomes, then continue from HANDOVER.md. Never report a test/build as successful without checking its real output.
