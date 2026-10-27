# APK Static Analysis Report

**Status:** INVENTORY_COMPLETE
**Generated:** 2026-10-27 05:08:07 UTC
**Method:** static archive inspection only; the APK was not executed or installed.

## Source Release
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Release title: APKPure Original
- Release tag: APKPure_Latest
- Release page: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest
- Asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- Asset download URL: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/download/APKPure_Latest/Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- GitHub-reported size: 92726986 bytes
- Actual downloaded size: 92726986 bytes (88.43 MiB)
- Expected GitHub SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb
- Calculated SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb
- SHA-256 comparison: PASS

## Selected APK and XAPK container
- Input type: XAPK container with embedded APK
- APK analyzed: jp.konami.duellinks.apk
- Analyzed APK size: 55854706 bytes
- Embedded APK members: 2
- Embedded APK member: config.arm64_v8a.apk (36869159 bytes); outer CRC: PASS
- Embedded APK member: jp.konami.duellinks.apk (55854706 bytes); outer CRC: PASS
- OBB members in container: 0
- No .obb member found in the XAPK container.

- Selected APK member CRC in the XAPK container: PASS
## Selected APK archive integrity
- ZIP/APK opened: PASS
- Central-directory entry count: 3368
- Total uncompressed size: 98705262 bytes (94.13 MiB)
- CRC scan: PASS

## Embedded config/split APK inventory
### config.arm64_v8a.apk
- Extracted/inventoried: PASS
- Extracted size: 36869159 bytes
- SHA-256: d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4
- Outer XAPK member CRC: PASS
- Inner ZIP opened: PASS
- AndroidManifest.xml present: YES
- Entry count: 14
- DEX file count: 0
- Native library count: 9
- Inner CRC scan: PASS
- Native library: lib/arm64-v8a/libFirebaseCppAnalytics.so
- Native library: lib/arm64-v8a/libFirebaseCppApp-13_4_0.so
- Native library: lib/arm64-v8a/libFirebaseCppMessaging.so
- Native library: lib/arm64-v8a/lib_burst_generated.so
- Native library: lib/arm64-v8a/libdatastore_shared_counter.so
- Native library: lib/arm64-v8a/libduel.so
- Native library: lib/arm64-v8a/libil2cpp.so
- Native library: lib/arm64-v8a/libmain.so
- Native library: lib/arm64-v8a/libunity.so

## Structural inventory (selected primary APK only)
- AndroidManifest.xml present: YES
- DEX file count: 3
- classes.dex: 7574408 bytes (7.22 MiB)
- classes2.dex: 7094488 bytes (6.77 MiB)
- classes3.dex: 2076 bytes (2.03 KiB)

- Native library count (.so) in primary APK only: 0
- No native libraries under lib/<ABI>/ were detected in the primary APK; inspect the split APK inventory above.

## Common engine indicators
- **Unity:** assets/bin/Data/00000000000000000000000000000000, assets/bin/Data/0000000000000000f000000000000000, assets/bin/Data/0050f757a0d6b344291b18d9875bda03, assets/bin/Data/0056c8597feb97b419ba279270d2544f, assets/bin/Data/008bf88483f7bd74da1d04c69ac3b73f, assets/bin/Data/0096ea1dea4724b4180e0ec56e07b496, assets/bin/Data/00a8799b609025540a6d2e274686562d, assets/bin/Data/00d3c66b9071da144bafe96ff68f8592

## Signature-related ZIP entries
- META-INF/BNDLTOOL.SF
- META-INF/BNDLTOOL.RSA

## Largest entries by uncompressed size
- assets/bin/Data/Managed/Metadata/global-metadata.dat: 10.67 MiB uncompressed
- assets/bin/Data/b4e21b74ae1bbec4d8ab06b0fcf33931: 8.49 MiB uncompressed
- classes.dex: 7.22 MiB uncompressed
- classes2.dex: 6.77 MiB uncompressed
- assets/bin/Data/0e40a9f80e2a8bc40b907430e4211c4f: 5.73 MiB uncompressed
- assets/bin/Data/2f726907927ecf944ad1e9079e224cb3: 5.22 MiB uncompressed
- assets/bin/Data/7e6005c43f0013644897cdda3d2d5316: 5.22 MiB uncompressed
- assets/bin/Data/18f5f4a961f791f49a450c7464cf6774: 3.66 MiB uncompressed
- assets/bin/Data/Resources/unity default resources: 3.57 MiB uncompressed
- assets/bin/Data/e1f73dc34613ec042897cc46749d448c: 3.46 MiB uncompressed
- assets/bin/Data/globalgamemanagers: 2.93 MiB uncompressed
- assets/bin/Data/00000000000000000000000000000000: 2.89 MiB uncompressed
- assets/bin/Data/f92efd86ba1e5ac4e91e816e0187b39a: 2.36 MiB uncompressed
- assets/bin/Data/016b9be51929d334ea4e93cd70d57a4c.resource: 1.83 MiB uncompressed
- assets/bin/Data/1a1658ba5bf905442b0d847b2ebcd14a: 1.16 MiB uncompressed
- resources.arsc: 427.74 KiB uncompressed
- META-INF/BNDLTOOL.SF: 395.15 KiB uncompressed
- META-INF/MANIFEST.MF: 395.02 KiB uncompressed
- assets/bin/Data/Resources/unity_builtin_extra: 368.63 KiB uncompressed
- assets/bin/Data/globalgamemanagers.assets: 335.24 KiB uncompressed

## What this report does not prove
- This script does not decode the binary AndroidManifest.xml, so package name, versionName, minSdk, and targetSdk are not asserted.
- It does not validate Android APK signatures or identify a trusted signer.
- It does not decompile DEX/native code, trace feature callbacks, or prove that any toggle works.
- Filename indicators are heuristics only; they are not definitive engine identification.
- For XAPK input, this report inventories the selected primary APK and lists embedded APK/OBB members; it does not install the split set or prove that a single APK alone is sufficient.
- It does not execute, install, patch, or rebuild the APK.

## Recommended next step
Review the inventory and, if needed, run a separate tool-assisted static decompilation stage. Record file/class/method evidence for every candidate and keep hypotheses separate from verified findings.
