# CHATGPT MOD Build Report

**Status:** BLOCKED_FEATURE_APPROVAL_AND_END_TO_END_TESTING  
**Last updated:** 2026-10-27  
**Canonical repository:** TenzoNkz/YuGiOh-Duel-Link-MOD  
**Mod base:** APKPure Original V11.1.0 — Release tag APKPure_Latest  
**Comparison-only reference:** Platinmods V11.1.0 — Release tag Latest  
**Required in-game menu title:** CHATGPT MOD  
**Expected output:** verified modified APK (.apk)

## Current source package — integrity verified
- Asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk; size 92,726,986 bytes.
- Current expected and calculated container SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb.
- The prior digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 belonged to the previous internally corrupt upload; it is historical and superseded.
- Primary APK: jp.konami.duellinks.apk, 55,854,706 bytes; SHA-256 e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d.
- ARM64 split: config.arm64_v8a.apk, 36,869,159 bytes; SHA-256 d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4.
- Both embedded members pass outer XAPK CRC validation. Both the primary APK and ARM64 split pass their inner ZIP CRC/decompression scans. No OBB member was detected.
- Static archive inventory run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453605293 (success).
- Latest full Code Analysis with inner ZIP CRC scans and YgomMainActivity entry-point trace: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946821 (success; code report remains partial because JADX emitted 96 decompilation errors).
- Latest Checkpoint Validation after index/report updates: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40457881877 (success).
- Integration and gated patcher record: [MOD_INTEGRATION_PLAN.md](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/MOD_INTEGRATION_PLAN.md).

- Latest source/patche r validation (Java 21 workflow setup, Java-to-DEX, preflight fixtures and approval-bypass regression): https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40458144076 (success).
- Latest checkpoint validation after those code/workflow changes: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40458144071 (success).

## Actual analysis state
- APKTool exits 0 and decoded the current primary APK manifest/resources.
- JADX generated partial Java output (8,180 source files in the report) but returned exit code 3 with 96 decompilation errors. Status CODE_ANALYSIS_PARTIAL is therefore retained; this is not an APK CRC failure.
- Il2CppDumper v6.7.46 generated dump.cs, script.json and stringliteral.json, then exited -6 at its final Console.ReadKey prompt. The report generator now classifies the post-output console exception without itself crashing and records the clean archive-integrity findings.
- Metadata includes ShowMonster, card-face query declarations, the CHEATCARD enum, damage-value getters, and DuelMenu autoplay state/control names. This is static metadata only and does not prove any feature can be wired to a new menu or works at runtime.
- APKPure versus Platinmods byte comparison is available in APK_VARIANT_COMPARISON.md. Differences in manifest, DEX or resources do not independently tell us the semantic purpose of those changes.
- The decoded Activity is YgomMainActivity, extending Firebase's MessagingUnityPlayerActivity. The current APKPure base has no com.platinmods DEX classes, no SYSTEM_ALERT_WINDOW permission or Platinmods-style floating-menu service, and no direct WindowManager/addContentView menu hook in the Activity trace. An independently owned same-Activity UI is a candidate integration approach, but still needs a real patch and device test.
- Owned UI source now exists at src/mod_menu/com/chatgptmod/menu/ModMenu.java: launcher/panel, open/close, bounded dragging and a persisted local preference. It intentionally has no gameplay callbacks.
- tools/build_chatgpt_mod.py implements a gated APKPure-only patch path: require explicit approval, verify Release digest and nested APK CRCs, decode the base, inject a single Activity hook, merge required ARM64 split libraries, compile/append the menu DEX, rebuild, align, sign with an explicit keystore and verify the output.
- CI passed patcher primitive tests and compiled the helper to DEX. **The end-to-end patcher has not been run against the actual XAPK; no CHATGPT MOD APK has been produced, installed or runtime-tested.**

## Remaining blockers — not source integrity
1. Approve the bounded UI-only feature scope in MOD_CANDIDATES.md. The build gate now requires the exact standalone line `**Build approval: APPROVED_FOR_IMPLEMENTATION**`; the current checkpoint remains `**Build approval: PENDING_REVERSE_ENGINEERING**`, so the build tool/workflow must block.
2. Run the end-to-end APKPure XAPK patch build only after approval and after configuring a controlled signing key through Actions secrets. Confirm the Release digest, nested CRCs, Activity hook, helper DEX and merged ARM64 library set.
3. Inspect the signed output APK's package/version, DEX entries, libraries, signer and SHA-256. The helper-source CI is not a substitute for a real APK build.
4. Install on a dedicated test device/emulator and validate launch/crash logs, Activity lifecycle, Unity touch passthrough, drag bounds and preference persistence.
5. Do not promise that the result overwrites Platinmods; signer compatibility is unknown without its private key or valid certificate rotation chain.

## Partial reverse-engineering evidence
- ShowMonster signature: ShowMonster(bool immediate, bool showAura, Action onFinished).
- Card-face query names: GetFieldCardFace(int player, int position, int index), GetCardFace(...), DLL_DuelGetCardFace(...).
- PvP.Command.CHEATCARD = 9 is an enum constant, not proof of a callable cheat.
- IDS_CARD.PROCESS_DAMAGE variants are constants, not proof of a writable damage hook.
- DLL_DuelGetDamageValue(int) and PVP_DuelGetDamageValue(int) are getter signatures, not a demonstrated damage multiplier.
- DuelMenu metadata includes GetAutoPlay, SetAutoPlay(bool), ChangeAutoPlay, autoPlayEnable and fastAutoEnable. Their presence does not prove a third-party AutoPlay Bot callback or permitted use in a given mode.
- All findings are reported in IL2CPP_ANALYSIS_REPORT.md and MOD_CANDIDATES.md with caveats.

## Signature limitation
A public certificate is not the private signing key. Unless the required Platinmods signing key or a valid certificate rotation chain is available, an APK signed with our own key cannot be assumed to update an installed Platinmods version. A separate uninstall/reinstall may be required and could affect app-local data.

## Scope
Safe local UI/accessibility/settings, compatibility changes, independent preferences and offline simulations may be considered. A successful archive, static-analysis workflow or packaging step is not proof that a gameplay feature works.

## NEXT ACTION
Owner decision required: explicitly approve or decline the proposed UI-only scope (launcher/panel, open/close, dragging and one persisted local UI preference; no gameplay callbacks). Keep build approval pending until that decision. After approval, configure the Actions signing secrets and use Eksekusi Build App! for the gated non-release test build and dedicated-device QC.