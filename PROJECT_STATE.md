# Project State

Last checkpoint: 2026-10-26  
Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Status: APK archive inventory passed; the latest deeper static-analysis job succeeded, but its report remains partial because JADX reported 96 decompilation errors.

## Verified Release
- Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Release title: Platinmods Original
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- Size: 127,424,878 bytes (about 121.52 MiB)
- GitHub-reported and independently calculated SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Successful archive inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450

## Verified archive inventory
- Downloaded size matched Release metadata; SHA-256 matched; ZIP/APK CRC scan passed.
- 3,397 archive entries and about 307.33 MiB uncompressed.
- Three DEX files; 20 native .so libraries (10 per ABI).
- Unity/IL2CPP indicators include assets/bin/Data/, libunity.so, libil2cpp.so, and global-metadata.dat.
- Relevant native library names include libduel.so and libplatinmods.so.
- META-INF signature-related entries exist, but their presence alone does not validate the APK signature or signer trust.

## Latest code-analysis findings
- Latest successful run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274382469
- Report: APK_CODE_ANALYSIS.md. Its status is CODE_ANALYSIS_PARTIAL despite the workflow job succeeding.
- Apktool 3.0.3 decoded the manifest to package jp.konami.duellinks and generated 18,765 output entries.
- JADX 1.5.6 generated 8,194 Java sources but exited with code 3 and reported 96 decompilation errors.
- com/platinmods/FloatingModMenuService.java contains generic menu widgets and toggle callbacks that invoke Preferences.changeFeatureBoolean(...) and localChanges(...).
- com/platinmods/Preferences.java declares native Changes(Context, int, int, boolean, String), routes changes to it, and stores preferences.
- com/platinmods/PMLauncher.java declares native initialize(Context) and loads the platinmods library.
- libplatinmods.so contains JNI string names including getFeatureList, settingsList, and Preferences_Changes.
- libduel.so / IL2CPP metadata strings include DLL_DuelGetDamageValue, DLL_DuelGetDamageSrcPosition, DLL_DuelGetDamageDstPosition, DLL_DuelComCheatCard, CHEATCARD, PROCESS_DAMAGE variants, and ShowMonster/showMonster.
- These are source/symbol/string clues only. They do not prove an in-game effect, exact mapping from overlay labels to feature IDs, native call flow, ownership filtering, or server behavior.

## Current evidence boundary
- APK integrity and archive inventory are verified.
- Generic Platinmods overlay and native callback architecture are visible in static output.
- Feature-specific native dispatch and full Unity/IL2CPP control flow remain untraced.
- APK has not been installed or executed; no runtime, live-match, or server-authority behavior has been tested.

## User objective
Use GitHub as the durable source of truth for the APK, analysis reports, candidate register, workflow status, and copy-ready chat recovery prompts. Evaluate existing Platinmods toggles and candidate modifications one by one. The original requested idea was a Damage Multiplier affecting only the user's own cards.

## Next action
Inspect the newest Checkpoint Validation run triggered by report commit 9215f3d8e28713b76753f169fc96c00654194128. Then continue static tracing of the native menu dispatch: relate getFeatureList/settingsList to Preferences.Changes and the displayed feature IDs. Update MOD_CANDIDATES.md only with evidence-backed conclusions. Do not implement a live online damage-changing cheat; an isolated offline simulation is a separate possible task.

## Known boundaries
- No APK patch/rebuilt APK has been produced.
- No live match, game account, or server behavior has been tested.
- Do not mark any candidate as working until a safe, reproducible test supports it.
