# YuGiOh-Duel-Link-MOD — GitHub Source of Truth

This repository follows the JE X FYZ-style recovery workflow. **APKPure Original V11.1.0 is the sole intended mod base. Platinmods V11.1.0 is a comparison reference only.** The project is still in reverse-engineering and feasibility analysis; no CHATGPT MOD APK has been built.

## Canonical inputs

- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Branch: main
- Intended base: [APKPure Original Release — APKPure_Latest](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest)
- APKPure asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- Reference only: [Platinmods Original Release — Latest](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Latest)
- Platinmods asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.1.0.apk

The XAPK is not renamed to APK. The analysis tools inventory the container, select a likely primary APK, list other embedded APKs/OBB payloads, and keep the container SHA-256 separate from the selected APK SHA-256. A final single-APK output is not assumed possible until split/OBB compatibility is assessed.

## Three primary modes

### Diskusi!
Review the current repository, reports, release metadata, relevant code and workflow outcomes. This mode does not edit files, commit, trigger workflows, patch APKs, or build.

### Eksekusi Full!
Implement the agreed engineering work, run code checks and tests, update durable reports/checkpoints, and verify Actions results. Current task: build a reliable APKPure-XAPK analysis and variant comparison pipeline before selecting CHATGPT MOD features.

### Eksekusi Build App!
Build/QC the agreed mod based on APKPure Original only. Platinmods must remain comparison-only. The final user-facing menu title is CHATGPT MOD. Do not run a build until the reverse-engineering evidence identifies an approved patch plan and a real APK patch/build pipeline exists.

## GitHub Actions

- APK Static Analysis — downloads the selected Release APK/XAPK as data, validates the reported container digest, inventories the selected APK, and reports embedded XAPK members.
- APK Code Analysis (APKPure Base) — runs Apktool/JADX against the selected APKPure primary APK and creates APK_CODE_ANALYSIS.md.
- APK variant comparison — tools/compare_apk_variants.py creates APK_VARIANT_COMPARISON.md by comparing APKPure entry paths and hashes against Platinmods. It does not patch either package.
- Checkpoint Validation — compiles Python tools and runs local unit tests for APK/XAPK input handling.
- CHATGPT Mod Build — must remain blocked until the approved APKPure-based patch/build tooling is implemented. The previous Gradle-demo approach is not the intended product and must not be reported as a modified Duel Links APK.

## Durable project records

- CHAT_TRANSFER.md — copy-ready prompts for Diskusi!, Eksekusi Full!, and Eksekusi Build App!.
- CHAT_RULES.md — operating rules and scope boundaries.
- MEMORY_INDEX.md — authoritative reading order and tool index.
- PROJECT_STATE.md — verified current state and next step.
- HANDOVER.md — exact continuation point.
- APP_ANALYSIS_REPORT.md — static archive inventory.
- APK_CODE_ANALYSIS.md — Apktool/JADX/DEX/native static findings.
- APK_VARIANT_COMPARISON.md — APKPure-versus-Platinmods path/hash comparison.
- MOD_CANDIDATES.md — feature candidates, evidence, unknowns and status.
- CHATGPT_MOD_BUILD_REPORT.md — build status and blockers.
- ANALYSIS_LOG.md — chronological verified milestones.

## Interpretation and scope

A string or native symbol is a lead, not proof that an option works. Reports must separate directly observed facts, hypotheses, and runtime-tested behavior. Static analysis must not execute or install the APKs. Safe local UI/accessibility, settings, compatibility and offline simulations may be considered. Live-online-duel modifications intended to unfairly alter outcomes are out of scope.

Do not claim signer identity from ordinary META-INF entries alone: APK v2/v3 signing blocks are not normal ZIP entries. Before promising installation over an existing Platinmods installation, verify package identity and signer certificate compatibility. Keep generated APK binaries out of Git history and never overwrite the original Release assets.

## Chat-limit recovery

1. Open CHAT_TRANSFER.md.
2. Copy the prompt for the required mode.
3. Paste it into the new chat.
4. Reload the live main branch, current Release metadata, reports and latest Actions results. Continue from HANDOVER.md without asking for the same public Release files again.
