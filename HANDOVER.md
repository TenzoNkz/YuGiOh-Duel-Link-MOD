# Handover — Exact Continuation Point

Checkpoint date: 2026-10-27  
Repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Branch: main

## Product direction
- APKPure Original V11.1.0 (Release tag APKPure_Latest) is the sole intended mod base.
- Platinmods V11.1.0 (Release tag Latest) is comparison-only reference.
- Target output is a genuine modified APK with the in-game menu title CHATGPT MOD.
- Do not build until the source package is clean and the first feature plan is approved.

## Verified V11.1.0 findings
1. The XAPK outer container is 92,726,986 bytes and its SHA-256 matches GitHub metadata.
2. It contains jp.konami.duellinks.apk (55,854,706 bytes) and config.arm64_v8a.apk (36,869,159 bytes), with no OBB member found.
3. The outer member CRC fails for both embedded APKs.
4. The primary APK's decompression/CRC scan fails in assets/bin/Data/e1f73dc34613ec042897cc46749d448c with invalid literal/length code.
5. The ARM64 split contains nine native libraries; lib/arm64-v8a/libduel.so fails its ZIP CRC check.
6. The comparison found 2,874 identical readable package paths, 205 different readable shared paths, 296 APKPure-only paths, 317 Platinmods-only paths and two shared unreadable APKPure entries.
7. ARM64 libil2cpp.so and global-metadata.dat are byte-identical between APKPure and Platinmods; the primary manifest and three DEX files differ byte-for-byte. The corrupted libduel.so prevents a reliable comparison for that file.
8. Apktool/JADX output remains partial. A new pinned IL2CPP dump is in progress/needs its current report checked. No mod feature is confirmed working.

## Engineering changes already made
- Added APK/XAPK-aware input handling and split-member CRC inspection.
- Updated static inventory and JADX/Apktool workflow to use APKPure by default.
- Added aggregate APKPure-versus-Platinmods byte-level comparison.
- Added a pinned Il2CppDumper v6.7.46 analysis stage and report.
- Added unit tests for plain APK passthrough, XAPK primary/split selection and malformed outer CRC reporting.
- Reworked durable docs to keep APKPure as base and Platinmods as reference only.
- Replaced the Gradle demo build workflow with a gated APKPure-based build scaffold. No actual APK patcher exists, so build stays blocked.

## Current known blocker
The APKPure Release asset's outer digest matches GitHub, but embedded package contents are internally corrupt. Do not use it for patch/build. Its current analysis output is useful for partial static findings only. A clean APKPure upload is required for full reverse engineering and reliable implementation.

## NEXT ACTION
Check the latest APK Code Analysis and Checkpoint Validation runs plus IL2CPP_ANALYSIS_REPORT.md. Then replace the corrupted APKPure XAPK with a clean original and rerun static/deep analysis. Update MOD_CANDIDATES.md only with evidence from the clean version, then approve the first safe feature.
