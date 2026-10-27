# Project State

Last update: 2026-10-27  
Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main

## Locked product direction
- APKPure Original V11.1.0, Release tag APKPure_Latest, is the sole intended mod base.
- Platinmods V11.1.0, Release tag Latest, is comparison-only reference.
- Intended output is a real modified APK with in-game menu title CHATGPT MOD.
- Do not run final packaging until a safe feature scope is reviewed and a genuine APKPure-based patch/build pipeline exists.

## Current APKPure source identity — verified clean
- Release asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk, size 92,726,986 bytes.
- Current GitHub Release digest and calculated XAPK SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb.
- The previous digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 belongs to the prior, internally corrupt upload and is superseded. Keep it only as historical evidence.
- Embedded primary APK: jp.konami.duellinks.apk, 55,854,706 bytes, SHA-256 e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d.
- Embedded ARM64 split: config.arm64_v8a.apk, 36,869,159 bytes, SHA-256 d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4.
- Both embedded APK members passed their XAPK outer CRC checks. The primary APK and ARM64 split passed full inner ZIP CRC/decompression scans. No OBB member was identified.
- Static source inventory passed: 3,368 primary APK entries, three DEX files, nine ARM64 native libraries across the split. This validates archive integrity, not runtime correctness or mod feasibility.
- Verified static archive workflow: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453605293.
- Latest APK Code Analysis, with full inner ZIP CRC scans and YgomMainActivity lifecycle/native/window trace: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946821 (success).
- Latest Checkpoint Validation, including Activity-trace and archive-integrity tests: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946814 (success).

## Reverse-engineering findings — static only
- APKTool successfully decoded the current primary APK (exit code 0). JADX produced partial Java output but reported 96 decompilation errors and returned exit code 3; the report status is CODE_ANALYSIS_PARTIAL. This is a decompiler limitation, not evidence that the current APK archive is corrupt.
- Perfare Il2CppDumper v6.7.46 generated dump.cs, script.json and stringliteral.json. It returned -6 at its final Console.ReadKey prompt after output generation. The report now computes this status before rendering and explicitly scans both inner APK archives.
- Metadata contains ShowMonster(bool immediate, bool showAura, Action onFinished); GetFieldCardFace(int player, int position, int index), GetCardFace(...) and DLL_DuelGetCardFace(...); PvP.Command.CHEATCARD = 9; IDS_CARD.PROCESS_DAMAGE and variants; DLL_DuelGetDamageValue(int) and PVP_DuelGetDamageValue(int); DuelMenu.GetAutoPlay, SetAutoPlay(bool), ChangeAutoPlay, autoPlayEnable and fastAutoEnable.
- These names are declarations/static metadata, not proof of feature behavior, hook availability, an external menu callback, hidden-card access, damage modification or an effective AutoPlay Bot. Damage getter signatures are read-only evidence unless a separate writable path is demonstrated.
- Current IL2CPP report: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/IL2CPP_ANALYSIS_REPORT.md.
- Current APKPure-versus-Platinmods comparison report: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/APK_VARIANT_COMPARISON.md. The two releases are compared at entry level; byte differences do not establish semantic changes.
- Android entry-point and UI integration analysis: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/MOD_INTEGRATION_PLAN.md.

## Analysis tooling and validation
- tools/apk_inputs.py: authenticated GitHub Release API headers, digesting, safe APK/XAPK extraction and outer CRC reporting.
- tools/analyze_release_apk.py: static archive inventory and nested APK integrity checks.
- tools/analyze_apk_code.py: Apktool/JADX, DEX/resource/native string scanning, and explicit inner ZIP CRC/decompression checks for primary and split APKs.
- tools/analyze_il2cpp.py: pinned Il2CppDumper run, result classification and primary/split archive integrity assessment.
- tools/compare_apk_variants.py: aggregate primary/split entry comparison and dynamic, package-specific integrity assessment.
- tests/test_apk_inputs.py, tests/test_analyze_apk_code.py, tests/test_analyze_il2cpp.py and tests/test_compare_apk_variants.py cover input selection, CRC behavior, API authentication, dumper classification and source-integrity reporting.
- Latest Checkpoint Validation with Activity-trace and archive-integrity tests passed at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946814.

## Android integration evidence
- The current decoded primary manifest identifies jp.konami.duellinks.plugins.YgomMainActivity as the exported Activity. JADX recovered a 581-line class extending com.google.firebase.MessagingUnityPlayerActivity and implementing BillingClientStateListener and PurchasesUpdatedListener.
- onCreate(Bundle) sets a fullscreen no-action-bar theme, calls super.onCreate, initializes a Logger, then processes the launch Intent/re-engagement URI. onResume/onPause delegate to super; onDestroy tears down the billing client; onNewIntent updates Intent/URI state.
- UnityPlayer.UnitySendMessage appears in purchase/billing callback flows (e.g. PurchaseBehaviour), not as a mod-menu callback. The APKPure DEX output contains no com.platinmods classes. The manifest does not declare SYSTEM_ALERT_WINDOW or a Platinmods-style floating-menu service, and the Activity trace found no direct WindowManager overlay hook or addContentView call.
- Interpretation: there is no ready-made Platinmods overlay to enable. An independently implemented same-Activity View attached after super.onCreate is only a prototype hypothesis; Unity fullscreen rendering/touch interaction and lifecycle must be tested on a real patched app. Details: MOD_INTEGRATION_PLAN.md.

## Feature feasibility — current assessment
- Highest conceptual feasibility: an independently implemented CHATGPT MOD menu shell, controls and local preference persistence. The Android Activity entry point is mapped; same-window attachment is not yet implemented or runtime-tested.
- Unconfirmed: Show Monster/status display, card-face queries and AutoPlay control. Their types, call sites, state visibility and allowable modes still need investigation.
- Read-only damage inspection or an offline damage-rule simulator can be evaluated separately. No writable damage multiplier or working CHEATCARD invocation has been proven.
- Live-online-duel outcome manipulation and hidden-opponent-information features are not implementation targets.

## Build status
- No CHATGPT MOD APK has been built, signed, installed or runtime-tested.
- The source-integrity blocker has been resolved by the updated APKPure Release asset.
- Remaining blockers are incomplete method/call-flow validation, no approved feature scope, no genuine APKPure-based patch/build pipeline, unresolved single-APK versus XAPK/split strategy, and signer/update/install compatibility.
- Do not use a standalone Gradle demo or rename/copy an APK and claim it is the modified game. Do not promise overwriting Platinmods unless the signing/update constraints are actually satisfied.

## NEXT ACTION
Review and approve a bounded first feature scope—recommended: independently implemented CHATGPT MOD menu shell plus local preference persistence only, with no gameplay callbacks yet. Then implement a genuine APKPure-based patch/build tool and a non-release test build; verify Activity attachment, Unity touch/lifecycle behavior, XAPK/split packaging and signing before considering release packaging.
