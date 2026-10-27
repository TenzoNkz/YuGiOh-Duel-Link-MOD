# Analysis Log

This is the durable chronological record of verified findings, decisions, workflow runs, failures, and next steps. Do not record hypotheses as facts.

## 2026-10-26 — Historical Platinmods V11.0.0 inventory
- Confirmed public repo TenzoNkz/YuGiOh-Duel-Link-MOD and Release Platinmods Original, tag Platinmods_V11.0.0.
- Historical asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk; size 127,424,878 bytes.
- SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.
- Successful archive inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450. Downloaded size and SHA-256 matched; ZIP CRC scan passed.
- Historical archive contained 3,397 entries, three DEX files, 20 native libraries, Unity/IL2CPP indicators, libduel.so, and libplatinmods.so.
- Historical Apktool/JADX report was partial: JADX generated 8,194 Java source files but reported 96 decompilation errors. This evidence is V11.0.0 only.

## 2026-10-27 — Source direction locked
- APKPure Original V11.1.0 (tag APKPure_Latest) is the sole intended mod base.
- Platinmods V11.1.0 (tag Latest) is comparison-only. Do not use its binary as the mod base.
- Intended result is a modified APK with in-game menu title CHATGPT MOD; a renamed XAPK or independent Gradle demo is not an acceptable deliverable.

## 2026-10-27 — APKPure V11.1.0 static inventory and comparison
- GitHub Release asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk, 92,726,986 bytes.
- Downloaded container SHA-256 exactly matches GitHub metadata: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16.
- XAPK contains jp.konami.duellinks.apk (55,854,706 bytes) and config.arm64_v8a.apk (36,869,159 bytes); no OBB member found.
- Both embedded APK members report an outer-container CRC mismatch.
- The primary APK lists 3,368 entries and three DEX files, but its ZIP CRC/decompression scan fails at assets/bin/Data/e1f73dc34613ec042897cc46749d448c with “invalid literal/length code”.
- The ARM64 split lists nine native libraries; lib/arm64-v8a/libduel.so fails CRC on read. The other readable ARM64 libraries include libil2cpp.so and libunity.so.
- Aggregate package comparison (main + split payloads) reported 2,874 identical readable paths, 205 different readable shared paths, 296 APKPure-only paths, 317 Platinmods-only paths, and two shared paths with unreadable APKPure content.
- ARM64 libil2cpp.so and global-metadata.dat have identical SHA-256 values between APKPure and Platinmods. AndroidManifest.xml and all three DEX files differ by bytes. This is structural evidence only, not an explanation of their code changes.
- The current APKPure upload must not be patched/built until replaced with a clean source package. The container hash match only means it matches the bytes uploaded to GitHub.

## 2026-10-27 — Analysis tooling improvements
- Added tools/apk_inputs.py for safe APK/XAPK asset handling and outer CRC reporting.
- Updated tools/analyze_release_apk.py to inventory primary plus embedded split APKs and report integrity warnings.
- Updated tools/analyze_apk_code.py to run Apktool/JADX on APKPure's primary APK and scan native/metadata entries across readable splits. The report is partial because the package is malformed and JADX reports decompilation errors.
- Added tools/compare_apk_variants.py to combine primary payload with unique split entries and compare APKPure against Platinmods reference.
- Added tools/analyze_il2cpp.py and a pinned Perfare Il2CppDumper v6.7.46 workflow stage for additional method/type metadata recovery. Its latest result must be read before feature conclusions.
- Added tests for asset selection, main/config split selection, OBB inventory, and malformed outer XAPK CRC handling. Checkpoint Validation passed on the earlier revisions; current IL2CPP report/workflow must still be checked.
- No CHATGPT MOD APK was built.

## NEXT
Verify the latest APK Code Analysis and Checkpoint Validation outcomes, inspect IL2CPP_ANALYSIS_REPORT.md, and request a clean APKPure Original re-upload. Rerun static/deep analysis with a clean package before approving a feature or starting final packaging.

## 2026-10-27 — APKPure IL2CPP metadata recovery (partial)
- Perfare Il2CppDumper v6.7.46 generated `dump.cs`, `script.json` and `stringliteral.json` using the APKPure ARM64 library and global metadata. It then exited with -6 in its final `Console.ReadKey` because stdin was redirected; report status explicitly records generated outputs with a post-dump console error.
- Recovered static declarations include `ShowMonster(bool immediate, bool showAura, Action onFinished)`; `GetFieldCardFace(int player, int position, int index)`, `GetCardFace(...)`, `DLL_DuelGetCardFace(...)`; `PvP.Command.CHEATCARD = 9`; `IDS_CARD.PROCESS_DAMAGE` through variants 1–3; and `DLL_DuelGetDamageValue` / `PVP_DuelGetDamageValue`.
- `DuelMenu` includes `GetAutoPlay`, `SetAutoPlay(bool)`, `ChangeAutoPlay`, `autoPlayEnable` and `fastAutoEnable`; `DuelClient` exposes autoplay-related state. These are not proof of a third-party AutoPlay Bot menu callback.
- Static symbols do not prove runtime behavior or a mod-menu call path. No implementation candidate is upgraded to proven-working from these names alone.
- APKPure XAPK still has failing outer member CRCs, an unreadable/decompression-failing primary asset, and a CRC-failing ARM64 `libduel.so`; final patch/build remains blocked until a clean original package replaces the upload.

