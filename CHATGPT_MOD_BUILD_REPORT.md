# CHATGPT MOD Build Report

**Status:** BLOCKED_REVERSE_ENGINEERING_AND_PATCH_PIPELINE  
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
- Code analysis and IL2CPP report refresh: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453733126 (success; code report remains partial because JADX emitted decompilation errors).
- Enhanced inner-CRC code analysis: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454023712 (verify its final result before considering all latest tooling checks done).

## Actual analysis state
- APKTool exits 0 and decoded the current primary APK manifest/resources.
- JADX generated partial Java output (8,180 source files in the report) but returned exit code 3 with 96 decompilation errors. Status CODE_ANALYSIS_PARTIAL is therefore retained; this is not an APK CRC failure.
- Il2CppDumper v6.7.46 generated dump.cs, script.json and stringliteral.json, then exited -6 at its final Console.ReadKey prompt. The report generator now classifies the post-output console exception without itself crashing and records the clean archive-integrity findings.
- Metadata includes ShowMonster, card-face query declarations, the CHEATCARD enum, damage-value getters, and DuelMenu autoplay state/control names. This is static metadata only and does not prove any feature can be wired to a new menu or works at runtime.
- APKPure versus Platinmods byte comparison is available in APK_VARIANT_COMPARISON.md. Differences in manifest, DEX or resources do not independently tell us the semantic purpose of those changes.
- No CHATGPT MOD APK has been built, signed, installed or runtime-tested.

## Remaining blockers — not source integrity
1. Complete source-grounded call-flow analysis for the Android Activity/DEX entry points and relevant IL2CPP declarations. Trace exact enclosing types and callers; do not infer functionality from method names alone.
2. Approve a bounded safe feature scope. Local UI/preferences and offline simulation can be considered; live-online-duel outcome manipulation and hidden-opponent-information features are excluded.
3. Implement and review a genuine APKPure-based patch/build tool. A standalone Gradle demo, renamed XAPK, copied Platinmods binary, or repackaged unmodified source APK is not an acceptable deliverable.
4. Resolve XAPK/split packaging: the source includes a primary APK plus an ARM64 configuration split. Do not assume the primary APK alone is complete or that blindly merging splits creates an installable output.
5. Validate package ID, version, Android signing identity and installation/update behavior. Without the relevant private signing key or a valid signing-certificate rotation chain, an independently signed APK cannot be assumed to overwrite an installed Platinmods build.
6. Build only after the above points and the feature plan are reviewed. Verify artifact bytes, SHA-256, signer, install behavior and the in-game menu title.

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
Trace the current clean primary APK's manifest and jp.konami.duellinks.plugins.YgomMainActivity DEX entry points, then map any proposed menu integration point against verified call paths. Keep final packaging blocked until a real APKPure-based patcher and approved feature scope exist.
