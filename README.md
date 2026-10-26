# YuGiOh-Duel-Link-MOD — GitHub Analysis Workspace

This repository keeps the durable state for static APK analysis and evidence-based evaluation of possible Duel Links modifications. The APK itself is stored as a GitHub Release asset; it is not committed into the Git history.

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
- APP_ANALYSIS_REPORT.md — latest measured APK static inventory.
- MOD_CANDIDATES.md — per-feature evidence/status register.
- ANALYSIS_LOG.md — chronological log of durable findings and decisions.

## GitHub Actions workflows

### APK Static Analysis
Open the repository's Actions tab and select APK Static Analysis. The workflow also attempts to start automatically when its workflow or analysis script changes on main. For a manual run, choose Run workflow and enter the existing release tag, normally Platinmods_V11.0.0.

The workflow downloads the APK from the public Release as data, computes SHA-256, checks ZIP/APK integrity when within resource limits, inventories DEX and native libraries, and records likely engine filename indicators. It then commits APP_ANALYSIS_REPORT.md if the report changed.

The first stage does NOT execute or install the APK, decode the binary manifest, validate APK signing certificates, decompile feature logic, or prove that any toggle works. Review the report and Actions logs before drawing conclusions. If the workflow cannot push the generated report, check repository Actions permissions and the run log.

### Checkpoint Validation
This workflow checks that all durable checkpoint files exist and that CHAT_TRANSFER.md and HANDOVER.md retain required recovery markers. It does not validate APK features.

## Chat-limit recovery
1. Open CHAT_TRANSFER.md.
2. Copy the prompt matching the intended mode.
3. Paste it into a new ChatGPT chat.
4. The new chat must read the live checkpoint documents and verify current Actions/Release evidence before proceeding.

## Analysis status
The source Release metadata is confirmed. See APP_ANALYSIS_REPORT.md for the current status of binary verification. Do not describe the APK as fully analyzed until the report and subsequent code-level evidence support that claim.

## Scope
The workflow treats the APK as data and never runs it. Candidate mods must be evidence-based and tested separately. No implementation should be presented as a working online-match modification without reproducible evidence.