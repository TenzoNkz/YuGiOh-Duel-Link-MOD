# YuGiOh-Duel-Link-MOD — GitHub Source of Truth

This repository uses GitHub for durable engineering state and chat-limit recovery. Three primary modes follow the JE X FYZ-style workflow: discussion, code execution, and app build/QC.

## Canonical source APK
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Branch: main
- Release: [Platinmods Original — Platinmods_V11.0.0](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0)
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- Verified SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb

## Three primary modes

### Diskusi!
Discuss and review all relevant code, dependencies, architecture, risks, and next steps. No source edits, commits, builds, or workflow runs. Copy the prompt from [CHAT_TRANSFER.md](CHAT_TRANSFER.md).

### Eksekusi Full!
Execute the agreed code task: edit source, implement scoped changes, run relevant tests/checks, fix regressions, verify GitHub Actions, and update project checkpoints. APK packaging is kept separate. Copy the prompt from [CHAT_TRANSFER.md](CHAT_TRANSFER.md).

### Eksekusi Build App!
Build/QC only for the latest agreed source and require the user-visible Android application label **CHATGPT Mod**. The build workflow validates chatgpt-mod/, produces a Debug APK artifact, records size/SHA-256/run URL, and commits [CHATGPT_MOD_BUILD_REPORT.md](CHATGPT_MOD_BUILD_REPORT.md).

**Current build blocker:** at this checkpoint the tracked repository has no Android Gradle source project under chatgpt-mod/. Consequently, no new CHATGPT Mod APK has yet been built. The build workflow will report this blocker instead of relabeling the original Release binary and claiming it was rebuilt. Use Eksekusi Full! to establish an authorized, safe source project first.

## GitHub Actions
- [APK Static Analysis](../../actions/workflows/apk-static-analysis.yml) — checksum, ZIP integrity, archive/DEX/native inventory. [Successful inventory run](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450).
- [APK Code Analysis](../../actions/workflows/apk-code-analysis.yml) — manifest, DEX/JADX, menu framework, and selected native/IL2CPP strings. [Latest successful job](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274382469); its report is still CODE_ANALYSIS_PARTIAL due to 96 JADX errors.
- [Checkpoint Validation](../../actions/workflows/checkpoint-validation.yml) — validates persistent files and prompt markers.
- [CHATGPT Mod Build](../../actions/workflows/build-chatgpt-mod.yml) — manually validates source/label, builds Debug APK, uploads an artifact, and updates the build report. It does not run automatically on doc changes.

## Durable records
- [CHAT_TRANSFER.md](CHAT_TRANSFER.md) — copy-ready prompts for the three modes and auxiliary Chat Stuck! recovery.
- [CHAT_RULES.md](CHAT_RULES.md) — mode behavior and boundaries.
- [MEMORY_INDEX.md](MEMORY_INDEX.md) — read order.
- [PROJECT_STATE.md](PROJECT_STATE.md) — verified state and next task.
- [HANDOVER.md](HANDOVER.md) — last verified step and one NEXT ACTION.
- [APP_ANALYSIS_REPORT.md](APP_ANALYSIS_REPORT.md) — measured APK inventory.
- [APK_CODE_ANALYSIS.md](APK_CODE_ANALYSIS.md) — partial code-level static findings.
- [CHATGPT_MOD_BUILD_REPORT.md](CHATGPT_MOD_BUILD_REPORT.md) — build status, artifact metadata, and blockers.
- [MOD_CANDIDATES.md](MOD_CANDIDATES.md) — candidate evidence/status.
- [ANALYSIS_LOG.md](ANALYSIS_LOG.md) — chronological record.

## Chat-limit recovery
1. Open [CHAT_TRANSFER.md](CHAT_TRANSFER.md).
2. Copy the prompt for the desired mode.
3. Paste it into the new chat.
4. The new chat must reload live main, current reports, Release metadata, and latest Actions status before continuing. Do not upload the same APK again if its canonical public Release is available.

## Build and scope limitations
The source Release is a binary analysis input, not a buildable Gradle project. An authorized Android source project must exist under chatgpt-mod/ for the build workflow to produce an APK. The build artifact is not published as a new Release by default. Safe local UI/accessibility and offline/sandbox work may be considered; live online-duel cheats intended to alter match outcomes are out of scope.
