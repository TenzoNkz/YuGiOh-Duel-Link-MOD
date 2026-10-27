# YuGiOh-Duel-Link-MOD — GitHub Source of Truth

This repository follows the JE X FYZ-style recovery workflow. **APKPure Original V11.1.0 is the sole intended mod base. Platinmods V11.1.0 is comparison-only reference.** The intended output is a real modified APK with an in-game menu titled CHATGPT MOD. No modified APK has been built.

## Canonical inputs

- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Branch: main
- Intended base: [APKPure Original Release — APKPure_Latest](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest)
- APKPure asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- Reference only: [Platinmods Original Release — Latest](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Latest)
- Platinmods asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.1.0.apk

## Current source-integrity status — PASS

The APKPure XAPK was updated and the current asset passes verification. Current XAPK size is 92,726,986 bytes; expected and calculated SHA-256 match at 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb. Both embedded APK members pass outer CRC checks, and the primary APK plus ARM64 split pass inner ZIP CRC/decompression scans. The old digest 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 belonged to the previous corrupt upload and is superseded.

Source integrity is verified. An owned UI-only menu helper and a gated APKPure patcher are now in the repository; CI compiles the helper to DEX and passes patcher primitive tests. **No APK has been built or runtime-tested yet.** The feature scope is still awaiting explicit approval, and the end-to-end XAPK/split rebuild, signing, installation and Unity touch behavior remain unverified. Review PROJECT_STATE.md, HANDOVER.md and MOD_INTEGRATION_PLAN.md for the current checkpoint.

## Three primary modes

### Diskusi!
Review the live repository, reports, Release metadata, relevant code and Actions outcomes. No edits, commits, workflow triggers, patches or builds.

### Eksekusi Full!
Implement the agreed engineering work, run code checks/tests, update durable reports, and verify actual Actions. The current task is APKPure-first reverse engineering and feature feasibility—not APK packaging.

### Eksekusi Build App!
Build/QC only after the owner approves the bounded UI-only scope in MOD_CANDIDATES.md and configures the required signing secrets. The real patcher is implemented but gated; its end-to-end output still needs validation. Do not build a separate Gradle demo or call an unmodified APK a mod.

## GitHub Actions

- [APK Static Analysis](../../actions/workflows/apk-static-analysis.yml) — container digest, XAPK primary/split inventory and CRC checks.
- [APK Code Analysis (APKPure Base)](../../actions/workflows/apk-code-analysis.yml) — Apktool/JADX, split-native inventory, package comparison, and pinned Il2CppDumper metadata recovery.
- [Checkpoint Validation](../../actions/workflows/checkpoint-validation.yml) — Python syntax and unit tests.
- [CHATGPT MOD Build](../../actions/workflows/build-chatgpt-mod.yml) — gated on clean source reports, explicit feature approval, and repository signing secrets.
- [CHATGPT MOD Menu Source Validation](../../actions/workflows/menu-source-validation.yml) — compiles the helper Java source to DEX and tests patcher primitives without building the game APK.

## Durable project records

- [CHAT_TRANSFER.md](CHAT_TRANSFER.md) — copy-ready prompts for the three primary modes.
- [CHAT_RULES.md](CHAT_RULES.md) — mode behavior and scope boundaries.
- [MEMORY_INDEX.md](MEMORY_INDEX.md) — authoritative read order and tools.
- [PROJECT_STATE.md](PROJECT_STATE.md) — verified state and next step.
- [HANDOVER.md](HANDOVER.md) — exact continuation point.
- [APP_ANALYSIS_REPORT.md](APP_ANALYSIS_REPORT.md) — container, member and structural inventory.
- [APK_CODE_ANALYSIS.md](APK_CODE_ANALYSIS.md) — manifest, DEX/JADX, native split and string analysis.
- [IL2CPP_ANALYSIS_REPORT.md](IL2CPP_ANALYSIS_REPORT.md) — type/method recovery attempt from the APKPure ARM64 library and metadata.
- [APK_VARIANT_COMPARISON.md](APK_VARIANT_COMPARISON.md) — byte-level comparison of APKPure payloads with Platinmods reference.
- [MOD_CANDIDATES.md](MOD_CANDIDATES.md) — feature candidates with explicit evidence/status and the current build-approval marker.
- [MOD_INTEGRATION_PLAN.md](MOD_INTEGRATION_PLAN.md) — clean Activity entry point, owned UI helper, patcher flow and remaining gates.
- [tools/build_chatgpt_mod.py](tools/build_chatgpt_mod.py) — gated APKPure-based patch/build implementation.
- [src/mod_menu/com/chatgptmod/menu/ModMenu.java](src/mod_menu/com/chatgptmod/menu/ModMenu.java) — owned UI-only menu source; no gameplay callbacks.
- [CHATGPT_MOD_BUILD_REPORT.md](CHATGPT_MOD_BUILD_REPORT.md) — verified build state/blockers.
- [ANALYSIS_LOG.md](ANALYSIS_LOG.md) — chronological verified milestones.

## Current comparison findings

- APKPure XAPK contains a primary package plus config.arm64_v8a.apk; no OBB member was detected.
- The APKPure primary package has three DEX files and no native libraries; the ARM64 config split contains nine native libraries.
- APKPure and Platinmods have byte-identical ARM64 libil2cpp.so and global-metadata.dat entries in the current comparison. The native inputs in the current APKPure package pass CRC checks; byte identity or difference does not prove feature behavior.
- AndroidManifest.xml and all three DEX files differ at the byte level. These differences do not, by themselves, explain semantic changes.
- The current analysis is partial, not full. APKTool decoded the primary APK; JADX reports 96 errors but produced partial source. The Activity trace maps YgomMainActivity and its Unity lifecycle/purchase bridge, but no ready-made floating-menu service or overlay hook was found in the Activity/manifest.
- Review MOD_INTEGRATION_PLAN.md before implementing an owned menu. Source integrity is verified; remaining blockers are approved feature scope, call-flow/feature validation, packaging strategy and the genuine patch/build pipeline.

## Scope and interpretation

A string or native symbol is a lead, not proof that a feature works. Static reports separate observed bytes, hypotheses and runtime-tested behavior. Safe local UI/accessibility/settings and compatibility changes, plus offline simulations, may be considered. Do not implement live-online-duel outcome manipulation. Verify the signer before promising in-place installation; a signing certificate is not the private key.

## Chat-limit recovery

1. Open CHAT_TRANSFER.md.
2. Copy the prompt for the required mode.
3. Paste it into the new chat.
4. Reload the live main branch, current reports and latest Actions results. Continue from HANDOVER.md without asking for the same public Release files again.
