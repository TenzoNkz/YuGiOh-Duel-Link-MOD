# YuGiOh-Duel-Link-MOD — GitHub Analysis Workspace

This repository is the durable source of truth for static APK analysis, candidate evaluation, and chat-limit recovery. The APK stays on GitHub Releases rather than in Git history.

## Canonical source
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Branch: main
- Release: [Platinmods Original — Platinmods_V11.0.0](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0)
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- Verified SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb

## Durable records
- [CHAT_TRANSFER.md](CHAT_TRANSFER.md) — prompts for Diskusi!, Eksekusi Analisa APK!, Eksekusi Full!, and Chat Stuck!.
- [CHAT_RULES.md](CHAT_RULES.md) — modes, evidence standards, boundaries.
- [MEMORY_INDEX.md](MEMORY_INDEX.md) — read order and file index.
- [PROJECT_STATE.md](PROJECT_STATE.md) — current verified state and next step.
- [HANDOVER.md](HANDOVER.md) — exact checkpoint and next action.
- [APP_ANALYSIS_REPORT.md](APP_ANALYSIS_REPORT.md) — measured archive inventory.
- [APK_CODE_ANALYSIS.md](APK_CODE_ANALYSIS.md) — manifest/JADX/native-string findings; status is partial.
- [MOD_CANDIDATES.md](MOD_CANDIDATES.md) — evidence-based candidate register.
- [ANALYSIS_LOG.md](ANALYSIS_LOG.md) — verified chronological record.

## GitHub Actions
- [APK Static Analysis](../../actions/workflows/apk-static-analysis.yml) downloads the APK from the public Release, computes SHA-256, checks archive integrity, inventories DEX/native libraries, and commits APP_ANALYSIS_REPORT.md. Successful run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450.
- [APK Code Analysis](../../actions/workflows/apk-code-analysis.yml) downloads the same Release asset as data, decodes its manifest, decompiles DEX with JADX, captures key Platinmods UI source lines, scans selected native/IL2CPP strings, and commits APK_CODE_ANALYSIS.md. It never executes or installs the APK. Latest successful run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274382469. The report remains CODE_ANALYSIS_PARTIAL because JADX emitted 96 errors.
- [Checkpoint Validation](../../actions/workflows/checkpoint-validation.yml) checks that required durable records and recovery markers exist. It does not prove feature behavior.

## Chat-limit recovery
1. Open [CHAT_TRANSFER.md](CHAT_TRANSFER.md).
2. Copy the prompt matching the work mode.
3. Paste it into a new ChatGPT chat.
4. The new chat must reload live GitHub reports, Release metadata, and current Actions state. Do not re-upload the same APK if the public Release is available.

## Current analysis boundary
Checksum and archive integrity are verified. Generic menu callbacks are visible in decompiled Java. Exact native feature dispatch and full IL2CPP control flow remain untraced; runtime behavior and server authority are untested.

## Scope
The workflow treats APK as data. Candidates must be evidence-based and tested separately. No online-match damage-changing cheat is being implemented; offline simulation and UI-only experiments can be assessed separately.
