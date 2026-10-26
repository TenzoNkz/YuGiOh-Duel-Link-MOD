# Project State

Last checkpoint: 2026-10-26  
Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Project status: first-stage inventory passed; initial deep decompilation produced partial results; a refined code-analysis run is active.

## Verified repository and Release facts
- Repository is public and the default branch is main.
- Release URL: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Release title: Platinmods Original
- Release tag: Platinmods_V11.0.0
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- Asset size: 127,424,878 bytes (about 121.52 MiB).
- GitHub asset digest and independently calculated SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Successful archive inventory run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450
- Checkpoint validation succeeded on the latest code/script checkpoint: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40273558822

## First-stage APK inventory — verified findings
- Downloaded asset size matched GitHub's size.
- Calculated SHA-256 matched GitHub's reported digest.
- APK opened as ZIP; CRC scan passed.
- Archive has 3,397 entries and about 307.33 MiB total uncompressed size.
- Three DEX files found: classes.dex, classes2.dex, and classes3.dex.
- Twenty native .so files found: ten under arm64-v8a and ten under armeabi-v7a.
- Strong Unity/IL2CPP filename indicators found: assets/bin/Data/, libunity.so, libil2cpp.so, and global-metadata.dat.
- Additional native files include libduel.so and libplatinmods.so.
- META-INF/BNDLTOOL.SF and META-INF/BNDLTOOL.RSA exist; these entries do not validate APK signatures or establish signer trust.

## Initial deeper code findings — partial
- Apktool 3.0.3 successfully decoded the manifest; package name is jp.konami.duellinks.
- Apktool decoded 18,765 output entries.
- JADX 1.5.6 produced 8,194 Java source files but exited with code 3 and reported 96 decompilation errors. Treat the code report as partial, not complete.
- Decompiled source includes com.platinmods.FloatingModMenuService.java, PMLauncher.java, and Preferences.java.
- The PMLauncher class loads the native library platinmods.
- Native strings include JNI menu-framework exports such as Java_com_platinmods_FloatingModMenuService_getFeatureList, settingsList, and Java_com_platinmods_Preferences_Changes.
- libduel.so contains strings including DLL_DuelGetDamageValue and DLL_DuelComCheatCard. These names are leads only; they do not prove how the functions are called, whether they are hookable, or whether damage is server-authoritative.

## Current analysis stage
- APP_ANALYSIS_REPORT.md contains the verified inventory.
- APK_CODE_ANALYSIS.md has partial decompilation findings and is being regenerated after search/report refinements.
- Current refined APK Code Analysis run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40273558853
- Do not mark feature-level findings complete until this run and its report have been reviewed.

## User's objective
Perform a thorough, evidence-based investigation of the uploaded APK; inspect its structure and existing Platinmods menu toggles; evaluate candidate features one by one; determine what is technically supported without pretending untested features work. The requested idea includes a Damage Multiplier toggle intended to affect the user's own cards.

## Current evidence boundary
- Archive integrity and SHA-256 verification are complete.
- Initial DEX/manifest/native-string analysis is partial; JADX reported 96 decompilation errors.
- No live runtime testing or APK modification has been performed.
- A file listing or string hit alone does not establish that a mod feature works.

## Next action
Inspect refined run 40273558853 and its report commit. Review the corrected Java/resource/native-string hits. Then trace the existing menu's feature-list and preference-change flow at the class/method level and update MOD_CANDIDATES.md one item at a time. If the run fails, read job logs and fix the smallest blocking issue.

## Known boundaries
- No APK patch or rebuilt APK has been produced.
- No live match, game account, or server behavior has been tested.
- Do not label any candidate as working until there is specific evidence and a reproducible test.
