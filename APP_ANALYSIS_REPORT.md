# APK Static Analysis Report

**Status:** INVENTORY_COMPLETE
**Generated:** 2026-10-26 05:11:18 UTC
**Method:** static archive inspection only; the APK was not executed or installed.

## Source Release
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Release title: Platinmods Original
- Release tag: Platinmods_V11.0.0
- Release page: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- Asset download URL: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/download/Platinmods_V11.0.0/Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- GitHub-reported size: 127424878 bytes
- Actual downloaded size: 127424878 bytes (121.52 MiB)
- Expected GitHub SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Calculated SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- SHA-256 comparison: PASS

## Archive integrity
- ZIP/APK opened: PASS
- Central-directory entry count: 3397
- Total uncompressed size: 322259890 bytes (307.33 MiB)
- CRC scan: PASS

## Structural inventory
- AndroidManifest.xml present: YES
- DEX file count: 3
- classes.dex: 7301956 bytes (6.96 MiB)
- classes2.dex: 6866208 bytes (6.55 MiB)
- classes3.dex: 82324 bytes (80.39 KiB)

- Native library count (.so): 20
- arm64-v8a: 10 shared library file(s)
- armeabi-v7a: 10 shared library file(s)

## Common engine indicators
- **Unity:** assets/bin/Data/00000000000000000000000000000000, assets/bin/Data/0000000000000000f000000000000000, assets/bin/Data/0050f757a0d6b344291b18d9875bda03, assets/bin/Data/0056c8597feb97b419ba279270d2544f, assets/bin/Data/008bf88483f7bd74da1d04c69ac3b73f, assets/bin/Data/0096ea1dea4724b4180e0ec56e07b496, assets/bin/Data/00a8799b609025540a6d2e274686562d, assets/bin/Data/00d3c66b9071da144bafe96ff68f8592

## Signature-related ZIP entries
- META-INF/BNDLTOOL.SF
- META-INF/BNDLTOOL.RSA

## Largest entries by uncompressed size
- lib/arm64-v8a/libil2cpp.so: 61.35 MiB uncompressed
- lib/armeabi-v7a/libil2cpp.so: 52.09 MiB uncompressed
- lib/arm64-v8a/libduel.so: 21.16 MiB uncompressed
- lib/arm64-v8a/libunity.so: 20.86 MiB uncompressed
- lib/armeabi-v7a/libduel.so: 18.09 MiB uncompressed
- lib/armeabi-v7a/libunity.so: 15.48 MiB uncompressed
- assets/bin/Data/Managed/Metadata/global-metadata.dat: 10.66 MiB uncompressed
- lib/arm64-v8a/libplatinmods.so: 8.86 MiB uncompressed
- assets/bin/Data/b4e21b74ae1bbec4d8ab06b0fcf33931: 8.49 MiB uncompressed
- lib/armeabi-v7a/libplatinmods.so: 8.34 MiB uncompressed
- classes.dex: 6.96 MiB uncompressed
- classes2.dex: 6.55 MiB uncompressed
- assets/bin/Data/0e40a9f80e2a8bc40b907430e4211c4f: 5.73 MiB uncompressed
- assets/bin/Data/2f726907927ecf944ad1e9079e224cb3: 5.22 MiB uncompressed
- assets/bin/Data/7e6005c43f0013644897cdda3d2d5316: 5.22 MiB uncompressed
- lib/arm64-v8a/libFirebaseCppApp-13_4_0.so: 3.95 MiB uncompressed
- assets/bin/Data/18f5f4a961f791f49a450c7464cf6774: 3.66 MiB uncompressed
- assets/bin/Data/Resources/unity default resources: 3.57 MiB uncompressed
- assets/bin/Data/e1f73dc34613ec042897cc46749d448c: 3.46 MiB uncompressed
- lib/armeabi-v7a/libFirebaseCppApp-13_4_0.so: 3.15 MiB uncompressed

## What this report does not prove
- This script does not decode the binary AndroidManifest.xml, so package name, versionName, minSdk, and targetSdk are not asserted.
- It does not validate Android APK signatures or identify a trusted signer.
- It does not decompile DEX/native code, trace feature callbacks, or prove that any toggle works.
- Filename indicators are heuristics only; they are not definitive engine identification.
- It does not execute, install, patch, or rebuild the APK.

## Recommended next step
Review the inventory and, if needed, run a separate tool-assisted static decompilation stage. Record file/class/method evidence for every candidate and keep hypotheses separate from verified findings.
