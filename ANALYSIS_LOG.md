# Analysis Log

This is the durable chronological record of decisions, evidence, workflow runs, failures, and next steps. Append dated entries after each meaningful verified milestone; avoid recording guesses as facts.

## 2026-10-26 — GitHub Release verified
- Confirmed public repository TenzoNkz/YuGiOh-Duel-Link-MOD, default branch main.
- Confirmed Release Platinmods Original with tag Platinmods_V11.0.0.
- Release API lists Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk, size 127,424,878 bytes.
- Release API reports SHA-256 d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.

## 2026-10-26 — Durable recovery files and first-stage inventory
- Added chat recovery records and GitHub Actions for archive inventory and checkpoint validation.
- First APK Static Analysis attempt downloaded and inspected the asset but its report push lost a race with a concurrent commit.
- Fixed the inventory workflow to rebase its report commit before pushing.
- Successful archive inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450
- Verified downloaded size, matching SHA-256, ZIP open, and CRC scan. Found 3 DEX files, 20 native libraries, Unity/IL2CPP indicators, libduel.so, and libplatinmods.so.

## 2026-10-26 — Initial deep static analysis
- Added APK Code Analysis using pinned JADX 1.5.6 and Apktool 3.0.3.
- Apktool decoded the manifest and returned package jp.konami.duellinks. It decoded 18,765 output entries.
- JADX produced 8,194 Java source files, but the run reported 96 decompilation errors and exit code 3; findings are partial.
- Observed Platinmods menu framework class names and native JNI string exports, plus native strings DLL_DuelGetDamageValue and DLL_DuelComCheatCard in libduel.so. These are leads, not proof of feature behavior.
- The initial report search included overly broad matches from common Android resource names. The script was refined to separate Java, resource, and native search terms and to report the decompiler error count.
- Current refined run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40273558853

## Next
Inspect the refined run conclusion and its committed APK_CODE_ANALYSIS.md. Then trace the menu feature-list/preferences path and update MOD_CANDIDATES.md with exact evidence. Keep any online damage-changing behavior out of implementation scope; use offline simulation for arithmetic experiments.
