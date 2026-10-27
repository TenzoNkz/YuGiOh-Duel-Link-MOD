# Handover — Exact Continuation Point

Checkpoint date: 2026-10-27  
Repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Branch: main

## Product direction
- APKPure Original V11.1.0, Release tag APKPure_Latest, remains the sole intended mod base.
- Platinmods V11.1.0, Release tag Latest, is comparison-only reference.
- Target output is a genuine modified APK with in-game menu title CHATGPT MOD.
- Do not package the final APK until a bounded safe feature scope and a genuine APKPure-based patch/build tool exist.

## Latest verified source package
- Current XAPK asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk, size 92,726,986 bytes.
- Current expected/calculated XAPK SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb.
- Primary APK: jp.konami.duellinks.apk, 55,854,706 bytes, SHA-256 e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d.
- ARM64 split: config.arm64_v8a.apk, 36,869,159 bytes, SHA-256 d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4.
- Both embedded APK members pass outer XAPK CRC, and the primary APK and ARM64 split pass inner ZIP CRC/decompression scans. No OBB member is present.
- The older digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 belongs to the previous corrupt upload and is superseded.
- Static archive workflow succeeded: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453605293.
- Latest Code Analysis with full inner ZIP CRC scans and YgomMainActivity lifecycle/native/window trace succeeded: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946821.
- Latest Checkpoint Validation with Activity-trace and archive-integrity tests succeeded: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946814.

## Analysis state
- APKTool exit code 0; JADX produced partial Java output with exit code 3 and 96 decompilation errors. Keep CODE_ANALYSIS_PARTIAL; this is not a source CRC failure.
- Static Activity trace: jp/konami/duellinks/plugins/YgomMainActivity.java (581 lines), extending Firebase's MessagingUnityPlayerActivity and implementing BillingClientStateListener and PurchasesUpdatedListener.
- onCreate(Bundle) sets a fullscreen no-action-bar theme, calls super, initializes a Logger and handles launch-intent/re-engagement URI state. onResume/onPause delegate to super; onDestroy tears down billing; onNewIntent updates Intent/URI.
- UnityPlayer.UnitySendMessage references in this class belong to purchase/billing callback paths such as PurchaseBehaviour, not a mod-menu callback.
- APKPure DEX output has no com.platinmods classes. The manifest does not declare SYSTEM_ALERT_WINDOW or a Platinmods-style floating-menu service; the Activity trace has no direct WindowManager overlay hook or addContentView call. The APK therefore has no ready-made Platinmods overlay to enable.
- Il2CppDumper v6.7.46 generates dump.cs, script.json and stringliteral.json, then returns -6 at the final Console.ReadKey prompt. The report generator classifies this after-output exception and confirms clean inner archive scans.
- Static metadata includes ShowMonster, card-face query APIs, PvP.Command.CHEATCARD = 9, PROCESS_DAMAGE enum constants, damage-value getters and DuelMenu autoplay state/control names. No call path from a CHATGPT MOD menu to these declarations is proven. Getter signatures do not establish writable damage modification; card-face names do not prove hidden-opponent access.
- Current details: [APK_CODE_ANALYSIS.md](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/APK_CODE_ANALYSIS.md), [IL2CPP_ANALYSIS_REPORT.md](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/IL2CPP_ANALYSIS_REPORT.md), [MOD_CANDIDATES.md](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/MOD_CANDIDATES.md).

## Engineering changes in the current execution
- Added GitHub API token support to Release API requests and passed the Actions token into APK static/code-analysis jobs to reduce anonymous API rate-limit failures.
- Fixed IL2CPP report-generation ordering; added dumper-result classification and archive-integrity tests.
- Added full inner ZIP CRC/decompression checking to APK code analysis, removed obsolete hard-coded corruption warnings, and made variant comparison conclusions depend on current package evidence.
- Added tests for XAPK/APK CRCs, authenticated API headers, IL2CPP report classification, source-integrity assessment, and Android Activity tracing.
- Added [MOD_INTEGRATION_PLAN.md](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/MOD_INTEGRATION_PLAN.md), documenting the Activity entry point and safe menu integration options.
- Checkpoint Validation passed at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946814.

## Remaining blockers
1. Gameplay feature call-flow and runtime behavior are not proven; a method or enum name is not a working cheat.
2. Approve a bounded safe feature scope. Recommended first scope: independently owned CHATGPT MOD menu shell, presentation controls, and local preference persistence only—no gameplay callbacks yet.
3. Implement a genuine APKPure-based patch/build tool and preserve or correctly handle the XAPK primary/split relationship.
4. Prototype on the actual game build and test Activity lifecycle, z-order, Unity touch interaction, display scaling, preferences, stability and logs.
5. Confirm signing/install/update compatibility. Do not promise that an independently signed package will overwrite Platinmods.
6. Keep final APK release packaging blocked until the patcher, feature scope and test evidence are reviewed.

## NEXT ACTION
Review and approve the first safe scope in MOD_CANDIDATES.md and MOD_INTEGRATION_PLAN.md. Then implement the real APKPure-based patch pipeline and a non-release test prototype; do not run final APK packaging during Eksekusi Full.
