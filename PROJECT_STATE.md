# Project State

Last checkpoint: 2026-10-26  
Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Project status: initial APK inventory passed; deep static analysis has produced useful partial findings; the most recent refinement of the source-trace filter is queued in GitHub Actions.

## Verified repository and Release facts
- Repository is public and the default branch is main.
- Release URL: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Release title: Platinmods Original
- Release tag: Platinmods_V11.0.0
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- Asset size: 127,424,878 bytes (about 121.52 MiB).
- GitHub asset digest and independently calculated SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.
- Successful archive inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450
- Most recent checkpoint validation pass: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274001348

## First-stage APK inventory — verified findings
- Downloaded asset size matched GitHub's size.
- Calculated SHA-256 matched GitHub's reported digest.
- APK opened as ZIP; CRC scan passed.
- Archive has 3,397 entries and about 307.33 MiB total uncompressed size.
- Three DEX files found: classes.dex, classes2.dex, and classes3.dex.
- Twenty native .so files found: ten under arm64-v8a and ten under armeabi-v7a.
- Strong Unity/IL2CPP filename indicators found: assets/bin/Data/, libunity.so, libil2cpp.so, and global-metadata.dat.
- Additional native files include libduel.so and libplatinmods.so.
- META-INF/BNDLTOOL.SF and META-INF/BNDLTOOL.RSA exist; those entries do not validate APK signatures or establish signer trust.

## Deep static analysis — verified partial findings
- Apktool 3.0.3 successfully decoded the Android manifest; package name is jp.konami.duellinks.
- Apktool decoded 18,765 output entries.
- JADX 1.5.6 produced 8,194 Java source files but exited with code 3 and reported 96 decompilation errors. The report must remain labelled partial.
- Decompiled output includes com.platinmods.FloatingModMenuService.java, PMLauncher.java, Preferences.java; PMLauncher loads the native library platinmods.
- Native JNI strings include Java_com_platinmods_FloatingModMenuService_getFeatureList, settingsList, and Java_com_platinmods_Preferences_Changes.
- libduel.so contains strings DLL_DuelGetDamageValue, DLL_DuelGetDamageSrcPosition, DLL_DuelGetDamageDstPosition, and DLL_DuelComCheatCard. These are symbol/string leads only, not proof of call sites, hookability, card-ownership filtering, server acceptance, or working damage modification.
- The APK has not been executed or installed; no runtime or online duel behavior has been tested.

## Current code-analysis workflow state
- Report path: APK_CODE_ANALYSIS.md.
- Workflow: .github/workflows/apk-code-analysis.yml, script: tools/analyze_apk_code.py.
- Prior successful partial report run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40273870551.
- A more focused menu/native-string scan run was queued: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274001397.
- This latest script version restricts framework traces to com/platinmods classes and reports focused strings around menu/native damage symbols. Inspect the actual run conclusion and committed report before accepting findings.

## User's objective
Use GitHub as the durable source of truth for the full analysis workflow and recovery prompts. Investigate the existing Platinmods menu toggles and evaluate possible mods one by one using evidence. The initial requested idea was a Damage Multiplier that affects only the user's own cards.

## Current evidence boundary
- APK checksum/archive integrity and structural inventory are verified.
- DEX/manifest/native-string analysis is partial. No full IL2CPP control-flow trace has been completed.
- A file listing or string hit alone does not establish that a mod feature works. Static decompilation cannot prove server-authoritative behavior.

## Next action
Open the latest APK Code Analysis run (starting with 40274001397). Confirm that it completes and commits APK_CODE_ANALYSIS.md. Review the focused source/native evidence, then trace the feature-list/preferences flow and update MOD_CANDIDATES.md one item at a time. If the latest run fails, inspect job logs and fix the smallest blocking issue.

## Known boundaries
- No APK patch or rebuilt APK has been produced.
- No live match, game account, or server behavior has been tested.
- Do not label any candidate as working until there is specific evidence and a reproducible safe test.
