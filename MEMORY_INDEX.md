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
11. MOD_INTEGRATION_PLAN.md
12. ANALYSIS_LOG.md
13. README.md

## GitHub workflows
- APK Static Analysis: .github/workflows/apk-static-analysis.yml — defaults to APKPure_Latest; inventories primary APK and embedded split APKs.
- APK Code Analysis (APKPure Base): .github/workflows/apk-code-analysis.yml — runs Apktool/JADX on the primary APK, inventories native libraries in readable splits, compares aggregate package entries against Platinmods, and attempts pinned IL2CPP metadata recovery.
- Checkpoint Validation: .github/workflows/checkpoint-validation.yml — compiles tools and runs local unit tests.
- CHATGPT MOD Build: .github/workflows/build-chatgpt-mod.yml — gated on clean integrity reports, exact standalone scope approval, explicit signing secrets, and a non-release test workflow.
- CHATGPT MOD Menu Source Validation: .github/workflows/menu-source-validation.yml — compiles owned menu Java source to DEX and tests patcher primitives without packaging the game APK.

## Scripts and reports
- tools/apk_inputs.py — Release API, asset download, safe primary/split member extraction and CRC reporting.
- tools/analyze_release_apk.py — static integrity and structural inventory for APK/XAPK, including embedded config/split APK details.
- tools/analyze_apk_code.py — Apktool/JADX, inner APK CRC scans, native/IL2CPP strings and YgomMainActivity lifecycle/native/window trace.
- tools/analyze_il2cpp.py — pinned Il2CppDumper attempt using the APKPure ARM64 library and metadata.
- tools/compare_apk_variants.py — aggregate primary + split APK payload comparison: APKPure base versus Platinmods reference.
- tests/test_apk_inputs.py — APK/XAPK selection, split extraction, OBB inventory, CRC mismatch handling and GitHub API token headers.
- tests/test_analyze_apk_code.py — full inner APK CRC scan and YgomMainActivity lifecycle/native/window trace.
- tests/test_analyze_il2cpp.py — archive integrity and Il2CppDumper output/status classification.
- tests/test_compare_apk_variants.py — dynamic APKPure source integrity assessment.
- tools/build_chatgpt_mod.py — gated APKPure-only patcher; verifies Release digest and nested APK CRCs, patches the Activity entry, merges ARM64 split libraries, adds helper DEX, aligns, signs and verifies when all gates pass.
- src/mod_menu/com/chatgptmod/menu/ModMenu.java — owned UI-only launcher/panel, bounded dragging and saved local preference; no gameplay callbacks.
- tests/test_build_chatgpt_mod.py — Activity-smali injection, explicit approval gate, archive CRC, multidex naming and split-library copy tests.
- APP_ANALYSIS_REPORT.md — archive, checksum and split-integrity inventory.
- APK_CODE_ANALYSIS.md — manifest, DEX/Java, split-native and string-analysis report.
- IL2CPP_ANALYSIS_REPORT.md — type/method metadata recovery attempt and focused symbols.
- APK_VARIANT_COMPARISON.md — byte-level package comparison and integrity warnings.
- MOD_CANDIDATES.md — candidate evidence and feasibility status.
- MOD_INTEGRATION_PLAN.md — Activity entry point, menu integration options and build gates.
- CHATGPT_MOD_BUILD_REPORT.md — true build state and blockers.

## Current source integrity and build status
The current APKPure XAPK (92,726,986 bytes) has SHA-256 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb. Its embedded primary APK and ARM64 split both pass outer CRC checks and full inner ZIP CRC/decompression scans. The former digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 refers to the previous corrupt upload and is superseded. Code analysis remains partial due 96 JADX errors, while APKTool exits 0. The owned UI helper and gated patcher now exist, and CI validates helper Java-to-DEX compilation plus patcher primitives. No end-to-end APK has been built or runtime-tested; explicit feature-scope approval, controlled signing configuration and device-level validation remain blockers.

## Latest workflow checkpoints
- Static archive integrity: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453605293 — success.
- Full code-analysis report, full inner ZIP CRC scans and Activity entry-point trace: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946821 — success.
- Menu helper validation (Java-to-DEX compilation, preflight and approval-bypass regression): https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40457542823 — success.
- MOD_INTEGRATION_PLAN.md records the Activity evidence, UI-only helper, gated patcher and remaining gates.

- Latest menu helper validation (Java-to-DEX, report preflight, approval-bypass regression): https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40457542823 — success.
- Latest checkpoint validation after index/report updates: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40457881877 — success.
- Exact next action: owner explicitly approves or declines the UI-only scope; keep approval pending until then.

## Persistence contract
Committed GitHub records, Release metadata and verified Actions outputs are durable project state. New chats must reload live main, latest reports and Actions outcomes, then continue from HANDOVER.md. Never report a test/build as successful without checking its real output.
