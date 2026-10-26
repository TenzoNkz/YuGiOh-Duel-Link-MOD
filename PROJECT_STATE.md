# Project State

Last checkpoint: 2026-10-26  
Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Project status: first-stage APK inventory passed; deeper code-analysis workflow has been added and is queued/running.

## Verified repository and Release facts
- Repository is public and the default branch is main.
- Release URL: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Release title: Platinmods Original
- Release tag: Platinmods_V11.0.0
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- Asset size reported by GitHub: 127,424,878 bytes (about 121.52 MiB).
- GitHub asset digest and downloaded SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Successful inventory run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450
- Checkpoint validation passed: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272812594

## First-stage APK inventory — verified findings
- Downloaded asset size matched GitHub's size: 127,424,878 bytes.
- Calculated SHA-256 matched GitHub's reported digest.
- APK opened as ZIP; CRC scan passed.
- Archive has 3,397 entries and about 307.33 MiB total uncompressed size.
- Three DEX files found: classes.dex, classes2.dex, and classes3.dex.
- Twenty native .so files found: ten under arm64-v8a and ten under armeabi-v7a.
- Strong Unity/IL2CPP filename indicators found: assets/bin/Data/, libunity.so, libil2cpp.so, and global-metadata.dat.
- Other notable native files include libduel.so and libplatinmods.so.
- META-INF/BNDLTOOL.SF and META-INF/BNDLTOOL.RSA exist. These entries alone do not validate APK signing or identify a trusted signer.

## Current analysis stage
- The first report is committed to APP_ANALYSIS_REPORT.md.
- APK Code Analysis workflow was added at .github/workflows/apk-code-analysis.yml and its first run has been observed as queued: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40273104014
- It uses pinned JADX 1.5.6 and Apktool 3.0.3 to decode the manifest, decompile DEX, scan decoded text/resources, and search selected native/IL2CPP printable strings.
- Do not call the deeper analysis complete until that run concludes and APK_CODE_ANALYSIS.md is reviewed.

## User's objective
Perform a thorough, evidence-based investigation of the uploaded APK; inspect its structure and existing Platinmods menu toggles; evaluate candidate features one by one; determine what is technically supported without pretending untested features work. The requested idea includes a Damage Multiplier toggle intended to affect the user's own cards.

## Current evidence boundary
- Structural ZIP inventory and SHA/CRC verification are completed.
- JADX/Apktool code-level scan is pending.
- No runtime testing or APK modification has been performed.
- A file listing or string hit alone does not establish that a mod feature works. Dynamic validation is a separate step and must not be implied.

## Next action
Inspect APK Code Analysis run 40273104014. Verify its conclusion and report commit, then review APK_CODE_ANALYSIS.md. Use concrete class/resource/native string evidence to update MOD_CANDIDATES.md one feature at a time. If the run fails, read the GitHub Actions job logs, fix the cause in the workflow/script, and rerun.

## Known boundaries
- No APK patch or rebuilt APK has been produced by these workflows.
- No live match, game account, or server behavior has been tested.
- Do not label any candidate as working until there is specific evidence and a reproducible test.
