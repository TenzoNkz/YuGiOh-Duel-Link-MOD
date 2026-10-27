# Analysis Log

This is the durable chronological record of verified findings, decisions, workflow runs, failures, and next steps. Do not record hypotheses as facts.

## 2026-10-26 — Historical Platinmods V11.0.0 inventory
- Confirmed public repo TenzoNkz/YuGiOh-Duel-Link-MOD and Release Platinmods Original, tag Platinmods_V11.0.0.
- Historical asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk; size 127,424,878 bytes.
- SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb.
- Successful archive inventory: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40272870450. Downloaded size and SHA-256 matched; ZIP CRC scan passed.
- Historical archive contained 3,397 entries, three DEX files, 20 native libraries, Unity/IL2CPP indicators, libduel.so, and libplatinmods.so.
- Historical Apktool/JADX report was partial: JADX generated 8,194 Java source files but reported 96 decompilation errors. This evidence is for V11.0.0 and must not be presented as verified V11.1.0 behavior.

## 2026-10-27 — Project source direction corrected
- Locked APKPure Original V11.1.0 (Release tag APKPure_Latest) as the sole intended mod base.
- Locked Platinmods V11.1.0 (Release tag Latest) as comparison-only reference. Do not build from Platinmods or treat its libraries as implementation source.
- Target deliverable is a modified APK, not an independent Gradle demo or a renamed XAPK. Final output package layout and split/OBB requirements need evidence.
- User-facing in-game menu title is CHATGPT MOD.

## 2026-10-27 — APKPure/XAPK analysis pipeline changes
- Added tools/apk_inputs.py for Release retrieval, digesting, and primary APK selection from XAPK containers without extracting arbitrary archive paths.
- Updated tools/analyze_release_apk.py to select an embedded APK from XAPK input and report selected primary package information alongside container integrity.
- Updated tools/analyze_apk_code.py to use the APKPure Release by default and pass the selected primary APK through Apktool/JADX.
- Added tools/compare_apk_variants.py to compare APKPure primary APK archive members with the Platinmods reference by path, size, and SHA-256. This is a byte-level comparison, not a semantic reverse-engineering conclusion.
- Added tests/test_apk_inputs.py for asset choice, XAPK main-APK selection over config splits, OBB listing, and plain APK passthrough.
- Changed analysis workflow defaults to APKPure_Latest; deep analysis uses Latest only for reference comparison.
- Added APK_VARIANT_COMPARISON.md placeholder marked PENDING_ANALYSIS; it must be overwritten by a real Actions report before drawing conclusions.
- Updated durable project prompts/docs to ensure APKPure is the source base and Platinmods remains comparison-only.

## Verification checkpoint
- At the time of this log entry, the newly updated static/deep analysis and checkpoint runs must still be inspected directly. No result is claimed here until the actual Actions conclusion and generated reports are checked.
- No CHATGPT MOD APK was built.
- Build remains blocked until APKPure V11.1.0 reports support a reviewed feature/patch plan and a genuine APK-based patch/build pipeline exists.

## NEXT
Verify current Actions for APK Static Analysis, APK Code Analysis (APKPure Base), and Checkpoint Validation. Review reports, fix failures, and only then approve a candidate for implementation.
