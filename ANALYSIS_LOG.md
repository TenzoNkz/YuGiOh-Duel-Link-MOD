# Analysis Log

This is the durable chronological record of verified findings, decisions, workflow runs, failures, and next steps. Do not record hypotheses as facts.

## 2026-10-26 — Historical Platinmods V11.0.0 inventory
- Confirmed public repo TenzoNkz/YuGiOh-Duel-Link-MOD and Release Platinmods Original, tag Platinmods_V11.0.0.
- Historical asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk; size 127,424,878 bytes.
- SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.
- Successful archive inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450. Downloaded size and SHA-256 matched; ZIP CRC scan passed.
- Historical archive contained 3,397 entries, three DEX files, 20 native libraries, Unity/IL2CPP indicators, libduel.so, and libplatinmods.so.
- Historical Apktool/JADX report was partial: JADX generated 8,194 Java source files but reported 96 decompilation errors. This evidence is V11.0.0 only.

## 2026-10-27 — Source direction locked
- APKPure Original V11.1.0 (tag APKPure_Latest) is the sole intended mod base.
- Platinmods V11.1.0 (tag Latest) is comparison-only. Do not use its binary as the mod base.
- Intended result is a modified APK with in-game menu title CHATGPT MOD; a renamed XAPK or independent Gradle demo is not an acceptable deliverable.

## 2026-10-27 — APKPure V11.1.0 static inventory and comparison
- GitHub Release asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk, 92,726,986 bytes.
- Downloaded container SHA-256 exactly matches GitHub metadata: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16.
- XAPK contains jp.konami.duellinks.apk (55,854,706 bytes) and config.arm64_v8a.apk (36,869,159 bytes); no OBB member found.
- Both embedded APK members report an outer-container CRC mismatch.
- The primary APK lists 3,368 entries and three DEX files, but its ZIP CRC/decompression scan fails at assets/bin/Data/e1f73dc34613ec042897cc46749d448c with “invalid literal/length code”.
- The ARM64 split lists nine native libraries; lib/arm64-v8a/libduel.so fails CRC on read. The other readable ARM64 libraries include libil2cpp.so and libunity.so.
- Aggregate package comparison (main + split payloads) reported 2,874 identical readable paths, 205 different readable shared paths, 296 APKPure-only paths, 317 Platinmods-only paths, and two shared paths with unreadable APKPure content.
- ARM64 libil2cpp.so and global-metadata.dat have identical SHA-256 values between APKPure and Platinmods. AndroidManifest.xml and all three DEX files differ by bytes. This is structural evidence only, not an explanation of their code changes.
- The current APKPure upload must not be patched/built until replaced with a clean source package. The container hash match only means it matches the bytes uploaded to GitHub.

## 2026-10-27 — Analysis tooling improvements
- Added tools/apk_inputs.py for safe APK/XAPK asset handling and outer CRC reporting.
- Updated tools/analyze_release_apk.py to inventory primary plus embedded split APKs and report integrity warnings.
- Updated tools/analyze_apk_code.py to run Apktool/JADX on APKPure's primary APK and scan native/metadata entries across readable splits. The report is partial because the package is malformed and JADX reports decompilation errors.
- Added tools/compare_apk_variants.py to combine primary payload with unique split entries and compare APKPure against Platinmods reference.
- Added tools/analyze_il2cpp.py and a pinned Perfare Il2CppDumper v6.7.46 workflow stage for additional method/type metadata recovery. Its latest result must be read before feature conclusions.
- Added tests for asset selection, main/config split selection, OBB inventory, and malformed outer XAPK CRC handling. Checkpoint Validation passed on the earlier revisions; current IL2CPP report/workflow must still be checked.
- No CHATGPT MOD APK was built.

## NEXT
Verify the latest APK Code Analysis and Checkpoint Validation outcomes, inspect IL2CPP_ANALYSIS_REPORT.md, and request a clean APKPure Original re-upload. Rerun static/deep analysis with a clean package before approving a feature or starting final packaging.

## 2026-10-27 — APKPure IL2CPP metadata recovery (partial)
- Perfare Il2CppDumper v6.7.46 generated `dump.cs`, `script.json` and `stringliteral.json` using the APKPure ARM64 library and global metadata. It then exited with -6 in its final `Console.ReadKey` because stdin was redirected; report status explicitly records generated outputs with a post-dump console error.
- Recovered static declarations include `ShowMonster(bool immediate, bool showAura, Action onFinished)`; `GetFieldCardFace(int player, int position, int index)`, `GetCardFace(...)`, `DLL_DuelGetCardFace(...)`; `PvP.Command.CHEATCARD = 9`; `IDS_CARD.PROCESS_DAMAGE` through variants 1–3; and `DLL_DuelGetDamageValue` / `PVP_DuelGetDamageValue`.
- `DuelMenu` includes `GetAutoPlay`, `SetAutoPlay(bool)`, `ChangeAutoPlay`, `autoPlayEnable` and `fastAutoEnable`; `DuelClient` exposes autoplay-related state. These are not proof of a third-party AutoPlay Bot menu callback.
- Static symbols do not prove runtime behavior or a mod-menu call path. No implementation candidate is upgraded to proven-working from these names alone.
- APKPure XAPK still has failing outer member CRCs, an unreadable/decompression-failing primary asset, and a CRC-failing ARM64 `libduel.so`; final patch/build remains blocked until a clean original package replaces the upload.

## 2026-10-27 — APKPure Release refresh, integrity recovery, and tool fixes
- User updated the APKPure Original V11.1.0 Release asset. The current XAPK is 92,726,986 bytes and the expected and calculated SHA-256 now match at 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb. The prior 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 hash was the previous internally corrupt upload and is superseded.
- The current primary APK is jp.konami.duellinks.apk (55,854,706 bytes; SHA-256 e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d). The ARM64 split is config.arm64_v8a.apk (36,869,159 bytes; SHA-256 d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4). No OBB was found.
- Fresh checks pass: the container digest matches the Release digest, both embedded APKs pass outer XAPK CRC validation, and both the primary APK and ARM64 split pass inner ZIP CRC/decompression scans. Static archive inventory succeeded at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453605293.
- Successful current Release code/IL2CPP analysis completed at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453733126. APKTool exit code is 0; JADX returns 3 with 96 decompilation errors and partial source. Keep status CODE_ANALYSIS_PARTIAL, but do not mislabel that as an archive-integrity failure.
- Current IL2CPP report records that dump.cs, script.json, and stringliteral.json were produced. Il2CppDumper then exits -6 at a final Console.ReadKey prompt; tools/analyze_il2cpp.py now calculates this state before report rendering and verifies the inner CRCs instead of emitting a stale corruption warning.
- The comparison report now calculates APKPure integrity from the current source rather than hard-coding old CRC/decompression failures. Current recorded comparison reported 2,876 identical shared paths and 205 differing shared paths; hash differences are structural evidence only, not proof of feature semantics.
- Added GitHub API token support to Release API callers and passed GITHUB_TOKEN to both static and code-analysis workflows after earlier anonymous GitHub API requests hit HTTP 403 rate limits.
- Added tests for authentication headers, archive CRC scans, IL2CPP dump-result classification, and dynamic APKPure integrity assessment. Fixed a ZIP-signature test fixture after the first test run exposed its incorrectly escaped signature. Checkpoint Validation subsequently passed at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454118233.
- Added full inner ZIP CRC scans to APK code analysis and replaced the obsolete fallback message that implied a corrupt primary APK when no read errors existed. A follow-up analysis run is tracked at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454023712.
- The source-integrity blocker is now resolved. Final build remains blocked by incomplete source-grounded call-flow analysis, no approved feature scope, no real APKPure-based patch/build tool, XAPK/split packaging, and signer/update compatibility.
- No CHATGPT MOD APK has been built, signed, installed, or runtime-tested.

## NEXT
Inspect the final outcome and refreshed reports from https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454023712. Then map the clean primary APK manifest and jp.konami.duellinks.plugins.YgomMainActivity DEX entry points to a safe menu integration plan. Do not start final packaging during Eksekusi Full.

## 2026-10-27 — YgomMainActivity entry-point trace and integration plan
- APK Code Analysis with inner ZIP CRC scans and the new Android Activity trace passed: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946821.
- Checkpoint Validation with Activity-trace and archive-integrity tests passed: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946814.
- Current report locates jp/konami/duellinks/plugins/YgomMainActivity.java (581 lines). It extends com.google.firebase.MessagingUnityPlayerActivity and implements BillingClientStateListener/PurchasesUpdatedListener.
- onCreate(Bundle) sets a fullscreen no-action-bar theme, calls super.onCreate, initializes a Logger, reads the launch Intent, reports re-engagement and updates URI state. onResume/onPause delegate to super, onDestroy tears down the billing client, and onNewIntent updates Intent/URI.
- UnityPlayer.UnitySendMessage hits in this class belong to purchase/billing callback paths (e.g. PurchaseBehaviour), not evidence of an existing mod menu callback.
- APKPure's decompiled DEX output contains zero com.platinmods classes. The manifest has no SYSTEM_ALERT_WINDOW permission or Platinmods-style floating menu service, and the Activity trace shows no direct WindowManager overlay hook or addContentView call. Therefore no ready-made Platinmods floating menu can simply be enabled in APKPure.
- Created MOD_INTEGRATION_PLAN.md. Option A—attach an independently owned View to the existing Activity after super.onCreate—is a candidate to prototype, not a proven solution. Unity fullscreen z-order, touch handling, lifecycle, screen scaling, split packaging and signer behavior still require an actual patch and device/runtime test.
- Recommended first safe scope for review: menu shell/presentation controls plus local preference persistence, with no gameplay callbacks yet. No gameplay cheat has been proven functional.
- Current source integrity is PASS with XAPK SHA-256 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb. The older 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 hash belongs to the previous corrupt asset.
- Current remaining blockers: bounded safe feature scope not approved, no genuine APKPure-based patch/build tool, no validated XAPK/split-to-output strategy, no signer/update compatibility proof, and no mod APK built or runtime-tested.

