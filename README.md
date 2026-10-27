# YuGiOh-Duel-Link-MOD — GitHub Source of Truth

This repository follows the JE X FYZ-style recovery workflow. **APKPure Original V11.1.0 is the sole intended mod base. Platinmods V11.1.0 is comparison-only reference.** The intended output is a real modified APK with an in-game menu titled CHATGPT MOD. No modified APK has been built.

## Canonical inputs

- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Branch: main
- Intended base: [APKPure Original Release — APKPure_Latest](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest)
- APKPure asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- Reference only: [Platinmods Original Release — Latest](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Latest)
- Platinmods asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.1.0.apk

## Critical source-integrity finding

The APKPure XAPK container SHA-256 matches the digest declared by GitHub, but both embedded APK member CRC checks fail. Static inventory also reports a compressed asset decompression error in the primary APK at assets/bin/Data/e1f73dc34613ec042897cc46749d448c, and a bad CRC for lib/arm64-v8a/libduel.so in the ARM64 split. This means the uploaded file bytes match GitHub metadata, but the package contents are not internally clean. **Do not patch or build from this upload. Replace it with a clean original APKPure package and rerun analysis.**

## Three primary modes

### Diskusi!
Review the live repository, reports, Release metadata, relevant code and Actions outcomes. No edits, commits, workflow triggers, patches or builds.

### Eksekusi Full!
Implement the agreed engineering work, run code checks/tests, update durable reports, and verify actual Actions. The current task is APKPure-first reverse engineering and feature feasibility—not APK packaging.

### Eksekusi Build App!
Build/QC only after the source package is clean, the feature plan is reviewed, and a real APKPure-based patch/build tool exists. Do not build a separate Gradle demo and call it a modified Duel Links APK.

## GitHub Actions

- [APK Static Analysis](../../actions/workflows/apk-static-analysis.yml) — container digest, XAPK primary/split inventory and CRC checks.
- [APK Code Analysis (APKPure Base)](../../actions/workflows/apk-code-analysis.yml) — Apktool/JADX, split-native inventory, package comparison, and pinned Il2CppDumper metadata recovery.
- [Checkpoint Validation](../../actions/workflows/checkpoint-validation.yml) — Python syntax and unit tests.
- [CHATGPT MOD Build](../../actions/workflows/build-chatgpt-mod.yml) — gated until a clean APKPure base and real patch/build tool exist.

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
- [MOD_CANDIDATES.md](MOD_CANDIDATES.md) — feature candidates with explicit evidence/status.
- [CHATGPT_MOD_BUILD_REPORT.md](CHATGPT_MOD_BUILD_REPORT.md) — verified build state/blockers.
- [ANALYSIS_LOG.md](ANALYSIS_LOG.md) — chronological verified milestones.

## Current comparison findings

- APKPure XAPK contains a primary package plus config.arm64_v8a.apk; no OBB member was detected.
- The APKPure primary package has three DEX files and no native libraries; the ARM64 config split contains nine native libraries.
- APKPure and Platinmods have byte-identical ARM64 libil2cpp.so and global-metadata.dat entries in the current comparison. The ARM64 libduel.so entry is unreadable/corrupt in APKPure, so it cannot be compared reliably.
- AndroidManifest.xml and all three DEX files differ at the byte level. These differences do not, by themselves, explain the semantic changes.
- The current analysis is partial, not full; tool results and source integrity remain blockers.

## Scope and interpretation

A string or native symbol is a lead, not proof that a feature works. Static reports separate observed bytes, hypotheses and runtime-tested behavior. Safe local UI/accessibility/settings and compatibility changes, plus offline simulations, may be considered. Do not implement live-online-duel outcome manipulation. Verify the signer before promising in-place installation; a signing certificate is not the private key.

## Chat-limit recovery

1. Open CHAT_TRANSFER.md.
2. Copy the prompt for the required mode.
3. Paste it into the new chat.
4. Reload the live main branch, current reports and latest Actions results. Continue from HANDOVER.md without asking for the same public Release files again.
