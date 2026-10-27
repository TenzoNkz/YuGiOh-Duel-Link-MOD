# Project State

Last update: 2026-10-27  
Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main

## Locked product direction
- APKPure Original V11.1.0, Release tag APKPure_Latest, is the sole intended mod base.
- Platinmods V11.1.0, Release tag Latest, is comparison-only reference.
- Intended output is a real modified APK (.apk), with in-game menu title CHATGPT MOD.
- No APK has been built. Reverse engineering and input integrity must be resolved before feature approval/build.

## Actual V11.1.0 evidence from GitHub Actions
- The downloaded XAPK is 92,726,986 bytes and its calculated SHA-256 matches GitHub metadata: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16.
- XAPK contains jp.konami.duellinks.apk (55,854,706 bytes) plus config.arm64_v8a.apk (36,869,159 bytes); no OBB was detected.
- Outer XAPK CRC checks fail for both embedded APK members.
- The primary APK ZIP opens and lists 3,368 entries/three DEX files, but its CRC/decompression scan fails at assets/bin/Data/e1f73dc34613ec042897cc46749d448c with “invalid literal/length code”.
- The ARM64 split has nine native libraries, but lib/arm64-v8a/libduel.so fails its CRC check. Treat that native file and any conclusions depending on it as unverified.
- APKPure primary APK and Platinmods have 2,874 identical readable package paths, 205 different readable shared paths, 296 APKPure-only paths, 317 Platinmods-only paths, and two shared paths with unreadable APKPure content.
- The ARM64 libil2cpp.so and global-metadata.dat entries are byte-identical between APKPure and Platinmods in the comparison; AndroidManifest.xml and all three DEX files differ. Byte differences alone do not explain what code changed.
- The old Platinmods V11.0.0 JADX report had 96 errors; current APKPure V11.1.0 Apktool/JADX analysis is also partial due to the malformed assets and decompiler errors. This is not full reverse engineering.
- A pinned Il2CppDumper v6.7.46 analysis stage has been added. Its current report and latest Action result must be checked before drawing method-level conclusions.

## Critical blocker
The XAPK container digest matching GitHub metadata only proves the retrieved bytes match the uploaded asset; it does not mean those bytes contain valid embedded APKs. Do not patch/build from the present APKPure upload. Replace it with a clean original package and rerun all analyses. Preserve the existing Release for audit until the replacement is verified.

## Analysis tooling
- tools/apk_inputs.py: Release APIs, digesting and safe APK/XAPK primary/split extraction with outer CRC reporting.
- tools/analyze_release_apk.py: static archive inventory including split APKs.
- tools/analyze_apk_code.py: Apktool/JADX and readable DEX/native/IL2CPP strings across APKPure members.
- tools/analyze_il2cpp.py: pinned Il2CppDumper attempt using APKPure's ARM64 library and metadata.
- tools/compare_apk_variants.py: aggregate primary+split payload comparison with Platinmods as reference.
- tests/test_apk_inputs.py: XAPK selection, split extraction and CRC failure tests.

## Feature feasibility — current assessment
- Highest feasibility after a clean package: custom CHATGPT MOD UI, menu navigation, drag/minimize/restore, size/opacity/theme and independent preference persistence. Integration into the original game's activity/window lifecycle still needs a patch strategy.
- Mid/low confidence: Show Monster/status display; metadata strings are clues only and the relevant call path/data source has not been verified.
- Unknown: Reveal Card Face, AutoPlay Bot and visual/performance toggles that alter game-engine settings. No working callback is confirmed.
- Offline damage-rule simulator is feasible as a separate sandbox.
- Live-online-duel outcome manipulation is not an implementation target.

## Build status
- CHATGPT MOD APK not produced, signed, installed or runtime-tested.
- The former Gradle-only scaffold did not represent the intended product; it would build a standalone application, not modify Duel Links.
- Final build remains blocked until a clean APKPure package, reviewed feature plan, XAPK/split strategy, signer/update compatibility review, and real APKPure-based patch/build tool exist.

## NEXT ACTION
Review the latest IL2CPP analysis and Checkpoint Validation outcomes. Then ask for a clean re-upload of APKPure Original because the current asset fails CRC/decompression, replace the Release asset without losing the audit record, and rerun the full analysis before approving features.
