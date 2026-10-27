# Handover — Exact Continuation Point

Checkpoint date: 2026-10-27  
Repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Branch: main

## Product direction
- APKPure Original V11.1.0, Release tag APKPure_Latest, is the sole intended mod base.
- Platinmods V11.1.0, Release tag Latest, is comparison-only.
- Intended deliverable is a real modified APK with in-game menu title CHATGPT MOD.
- Current proposal is a bounded UI-only first stage; no gameplay cheat callbacks are approved or implemented.
- Do not run the APK build until the explicit feature-approval marker is updated by the owner.

## Latest verified source package
- Current XAPK asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk, size 92,726,986 bytes.
- Current expected/calculated XAPK SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb.
- Primary APK: jp.konami.duellinks.apk, 55,854,706 bytes, SHA-256 e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d.
- ARM64 split: config.arm64_v8a.apk, 36,869,159 bytes, SHA-256 d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4.
- Both embedded APK members pass outer XAPK CRC; primary and ARM64 split pass inner ZIP CRC/decompression scans. No OBB member was found.
- The former digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 belongs to the prior corrupt upload and is superseded.
- Latest code analysis with full inner CRC checks and Activity trace: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454946821 (success).
- Latest checkpoint validation after the current index/report updates: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40457881877 (success).
- Latest menu helper validation including Java-to-DEX compilation, complete preflight fixture and approval-bypass regression: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40457542823 (success).

## Current code and test artifacts
- Owned UI helper source: src/mod_menu/com/chatgptmod/menu/ModMenu.java. It displays a CHATGPT MOD launcher/panel, supports open/close and bounded dragging, and persists a local “keep panel open after restart” preference. It contains no gameplay action hooks.
- APK patch tool: tools/build_chatgpt_mod.py. It requires the owner-approved marker, downloads only APKPure_Latest, validates digest/CRCs, decodes the primary APK, injects one Activity hook after super.onCreate, merges validated ARM64 libraries, compiles/appends the helper DEX, rebuilds, aligns, signs with an explicit key and verifies output integrity/signature.
- Build workflow: .github/workflows/build-chatgpt-mod.yml. It is gated by source reports, the explicit approval marker, and repository Actions signing secrets.
- Source validation workflow: .github/workflows/menu-source-validation.yml. It compiles the helper Java source to DEX and runs patcher primitive tests; it does not package or run the game.
- Integration decision record: MOD_INTEGRATION_PLAN.md.
- Build approval currently remains PENDING_REVERSE_ENGINEERING in MOD_CANDIDATES.md.

## Reverse-engineering findings
- APKTool exits 0; JADX exits 3 with 96 decompilation errors and partial Java output. Keep CODE_ANALYSIS_PARTIAL; source CRC integrity is nevertheless PASS.
- Static Activity trace locates jp/konami/duellinks/plugins/YgomMainActivity.java (581 lines), extending Firebase MessagingUnityPlayerActivity. Its onCreate configures a fullscreen theme, initializes a logger and processes launch intent/URI. Lifecycle methods delegate to super and billing cleanup.
- UnityPlayer.UnitySendMessage references are in billing/purchase paths, not a mod-menu callback. APKPure DEX output contains no com.platinmods classes; no SYSTEM_ALERT_WINDOW permission or Platinmods-style menu service is declared. There is no existing ready-made floating menu to enable.
- IL2CPP dump files are generated but the dumper returns -6 at its final Console.ReadKey prompt. Recovered ShowMonster, card-face query, CHEATCARD enum, damage getter and AutoPlay names are metadata evidence only. No working cheat callback is proven.

## Current blockers
1. The menu helper and patcher passed source/primitive validation, but the end-to-end APKPure XAPK download/decode/inject/rebuild/align/sign pipeline has not been run.
2. The bounded UI-only feature scope has not been approved. No gameplay callbacks are to be added.
3. The actual test APK has not been generated, installed, or runtime-tested. Touch passthrough, Unity z-order, lifecycle, screen rotation and preference behavior remain unknown.
4. The build requires explicit repository Actions secrets: MOD_SIGNING_KEYSTORE_B64, MOD_SIGNING_KEY_ALIAS, MOD_SIGNING_STORE_PASSWORD and MOD_SIGNING_KEY_PASSWORD. Never commit secret material.
5. No promise that the independently signed APK can overwrite Platinmods; without its private signing key/valid rotation chain, uninstall/reinstall may be necessary.

## NEXT ACTION
Owner decision required: explicitly approve or decline the bounded UI-only scope in MOD_CANDIDATES.md. Approval must be represented by the exact standalone line `**Build approval: APPROVED_FOR_IMPLEMENTATION**` plus configuration of the four signing Actions secrets. Only then switch to Eksekusi Build App! for a non-release test APK and device QC. Do not represent the UI as integrated until runtime testing succeeds.