# YuGiOh-Duel-Link-MOD — GitHub Analysis Workspace

This repository keeps the durable state for static APK analysis and evidence-based evaluation of possible Duel Links modifications. The APK itself is stored as a GitHub Release asset; it is not committed into Git history.

## Canonical source
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Branch: main
- Release: [Platinmods Original — Platinmods_V11.0.0](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0)
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- GitHub-reported SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb

## Durable records
- CHAT_TRANSFER.md — copy-ready prompts for Diskusi!, Eksekusi Analisa APK!, Eksekusi Full!, and Chat Stuck!.
- CHAT_RULES.md — modes, evidence standards, and scope.
- MEMORY_INDEX.md — file index and load order.
- PROJECT_STATE.md — verified project status and next action.
- HANDOVER.md — exact last verified checkpoint and next action.
- APP_ANALYSIS_REPORT.md — measured APK archive inventory.
- APK_CODE_ANALYSIS.md — JADX/Apktool manifest, DEX, resource, and selected native-string analysis.
- MOD_CANDIDATES.md — per-feature evidence/status register.
- ANALYSIS_LOG.md — chronological log of durable findings and decisions.

## GitHub Actions workflows

### APK Static Analysis
Open Actions → APK Static Analysis. It downloads the APK from the public Release as data, calculates SHA-256, checks ZIP/APK CRC integrity, inventories DEX/native libraries, and records common engine filename indicators. The result is committed to APP_ANALYSIS_REPORT.md.

Latest successful initial inventory: [Run 40272870450](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450).

### APK Code Analysis
Open Actions → APK Code Analysis. Run manually with release tag Platinmods_V11.0.0 if no run is in progress. This workflow uses pinned JADX and Apktool releases to decode the Android manifest and inspect DEX/Java sources, resources, plus selected native/IL2CPP printable strings. It commits APK_CODE_ANALYSIS.md and keeps the decompiled source only in the temporary runner workspace.

It does not execute or install the APK. Static search hits are leads, not proof that a menu toggle works. Full IL2CPP native control-flow analysis and runtime testing remain separate tasks.

### Checkpoint Validation
Checks that required project-memory files exist and the transfer prompts preserve recovery markers. It does not validate APK feature behavior.

## Chat-limit recovery
1. Open CHAT_TRANSFER.md.
2. Copy the prompt matching the intended mode.
3. Paste it into a new ChatGPT chat.
4. The new chat must read the live checkpoint documents and verify current Actions/Release evidence before proceeding.

## Analysis status
The initial archive inventory passed: downloaded bytes matched GitHub's reported SHA-256 and the ZIP CRC scan passed. See APP_ANALYSIS_REPORT.md for measurements and APK_CODE_ANALYSIS.md for the deeper static-analysis status. Do not describe the APK as fully analyzed until all relevant reports and code-level evidence support that claim.

## Scope
The workflow treats the APK as data and never runs it. Candidate mods must be evidence-based and tested separately. No implementation should be presented as a working online-match modification without reproducible evidence.