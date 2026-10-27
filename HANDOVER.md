# Handover — Exact Continuation Point

Checkpoint date: 2026-10-27  
Repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Branch: main

## Product direction
- APKPure Original V11.1.0, Release tag APKPure_Latest, remains the sole intended mod base.
- Platinmods V11.1.0, Release tag Latest, is comparison-only reference.
- Target output is a genuine modified APK with in-game menu title CHATGPT MOD.
- Do not package the final APK until the safe feature scope and a genuine APKPure-based patch/build tool are in place.

## Latest verified source package
- Current XAPK asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk, size 92,726,986 bytes.
- Current expected/calculated XAPK SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb.
- Primary APK: jp.konami.duellinks.apk, 55,854,706 bytes, SHA-256 e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d.
- ARM64 split: config.arm64_v8a.apk, 36,869,159 bytes, SHA-256 d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4.
- Both embedded APK members pass outer XAPK CRC, and the primary APK and ARM64 split pass inner ZIP CRC/decompression scans. No OBB member is present.
- The older digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 belongs to the previous corrupt upload and is superseded.
- Static archive workflow succeeded: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453605293.
- Full code/IL2CPP report refresh completed successfully: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40453733126.
- A follow-up code-analysis run adds complete inner ZIP CRC checking to each APK member and is being verified here: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454023712.
- Checkpoint validation with the new tests has passed: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454118233.

## Analysis state
- APKTool exit code 0; JADX partial output with exit code 3 and 96 decompilation errors. Keep CODE_ANALYSIS_PARTIAL rather than claiming complete reverse engineering.
- Il2CppDumper v6.7.46 creates dump.cs, script.json and stringliteral.json, then returns -6 at the final Console.ReadKey prompt. The report generator has been fixed to classify this accurately before rendering the report, and archive-integrity results now state the actual clean CRC scans.
- Static metadata includes ShowMonster, card-face query APIs, PvP.Command.CHEATCARD = 9, PROCESS_DAMAGE enum constants, damage-value getters, and DuelMenu autoplay state/control names. No call path from a CHATGPT MOD overlay to these declarations is proven. The getters do not establish writable damage modification; face-query names do not prove hidden-opponent-card access.
- APKPure and Platinmods differ in shared manifest/DEX/resources and entry counts; byte differences alone do not explain feature behavior.

## Engineering changes in the current execution
- Added GitHub API token support to release API requests and passed the Actions token into APK static/code-analysis jobs to reduce anonymous API rate-limit failures.
- Fixed IL2CPP report-generation ordering that previously caused UnboundLocalError after dumping. Added result-classification and archive-integrity unit tests.
- Added full inner ZIP CRC/decompression checking to APK code analysis and removed the inaccurate old fallback warning.
- Updated variant comparison to derive APKPure integrity conclusions from actual findings rather than hard-coded stale corruption statements.
- Added unit tests for XAPK/APK CRCs, authenticated API headers, IL2CPP report classification, and source-integrity assessment.
- Latest Checkpoint Validation link above confirms the suite passed after correcting the ZIP-signature fixture.

## Remaining blockers
1. Complete the current follow-up analysis run and check the refreshed APK_CODE_ANALYSIS.md, APK_VARIANT_COMPARISON.md, and IL2CPP_ANALYSIS_REPORT.md.
2. Trace the clean primary APK's AndroidManifest.xml and jp.konami.duellinks.plugins.YgomMainActivity DEX entry points; map any proposed menu integration route against the IL2CPP/native architecture.
3. Select and approve a bounded safe feature scope. No gameplay feature is proven working merely from a method name.
4. Implement and review a real APKPure-based patch/build tool and XAPK/split packaging strategy.
5. Confirm signing/install/update compatibility. Do not promise that an independently signed package will overwrite Platinmods.
6. Keep final APK packaging blocked until the patcher and feature plan are reviewed.

## NEXT ACTION
Inspect the final result of https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40454023712, then trace the Activity/DEX entry point and define an evidence-based integration plan for the safe CHATGPT MOD menu. Do not run final APK packaging in Eksekusi Full mode.
