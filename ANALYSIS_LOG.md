# Analysis Log

This is the durable chronological record of decisions, evidence, workflow runs, failures, and next steps. Append dated entries after each meaningful verified milestone; avoid recording guesses as facts.

## 2026-10-26 — GitHub Release verified
- Confirmed public repository TenzoNkz/YuGiOh-Duel-Link-MOD, default branch main.
- Confirmed Release Platinmods Original with tag Platinmods_V11.0.0.
- Release API lists Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk, size 127,424,878 bytes.
- Release API reports SHA-256 d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.
- The record above is Release metadata evidence, not a claim that the APK had already been analyzed.

## 2026-10-26 — Durable chat recovery and workflows
- Added CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, and MOD_CANDIDATES.md.
- Added a Checkpoint Validation workflow; successful run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272812594.
- First APK Static Analysis run completed the inventory but failed to push its report because main advanced while it was running.
- Fixed the report workflow to rebase the generated report onto the latest branch head before pushing.
- Successful APK Static Analysis rerun: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450.
- Verified downloaded size 127,424,878 bytes; SHA-256 matched the GitHub API digest; ZIP CRC scan passed.
- The APK contains 3 DEX files and 20 native .so files (10 per ABI), with Unity/IL2CPP indicators, libduel.so, and libplatinmods.so.
- Added APK Code Analysis with pinned JADX 1.5.6 and Apktool 3.0.3. Its run was observed queued at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40273104014; its final result has not yet been reviewed in this log.

## Next
Inspect the APK Code Analysis run and report. Then use concrete evidence to update MOD_CANDIDATES.md feature by feature, and record the run URL/conclusion and any important limitations.
