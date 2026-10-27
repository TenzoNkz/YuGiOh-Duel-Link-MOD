# Project State

Last update: 2026-10-27  
Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main

## Product direction — locked

- APKPure Original V11.1.0 is the sole intended input/base for CHATGPT MOD.
- Platinmods V11.1.0 is a reference used only to compare archive members and investigate architecture. It is not the build base.
- The eventual output should be a real modified APK (.apk), not a renamed XAPK and not a standalone Android demo.
- The user-visible mod-menu title is CHATGPT MOD.
- Reverse engineering and feature feasibility must be completed before choosing the patch plan or building.

## Implemented analysis pipeline

- tools/apk_inputs.py: shared Release download, digest and safe APK/XAPK primary-member handling.
- tools/analyze_release_apk.py: static archive inventory for APK or XAPK; inspects the selected primary APK and records embedded APK/OBB members.
- tools/analyze_apk_code.py: APKPure-first Apktool/JADX analysis; selects the primary APK from XAPK input and records container integrity separately.
- tools/compare_apk_variants.py: compares primary APK archive members, sizes and SHA-256 values for APKPure against Platinmods as reference only.
- .github/workflows/apk-static-analysis.yml: default source is APKPure_Latest.
- .github/workflows/apk-code-analysis.yml: default deep-analysis source is APKPure_Latest; reference comparison default is Latest.
- tests/test_apk_inputs.py: local tests for release asset selection, primary XAPK APK selection, and plain APK passthrough.
- APK_VARIANT_COMPARISON.md: comparison report target. The placeholder is explicitly marked PENDING_ANALYSIS until a real run overwrites it.

## Verification state

- Earlier completed evidence is from Platinmods V11.0.0: ZIP/CRC and inventory passed; decoded package was jp.konami.duellinks; Unity/IL2CPP architecture and Platinmods menu framework references were observed.
- Earlier JADX analysis produced 8,194 Java source files but reported 96 decompilation errors. That report was partial and is not evidence for V11.1.0 behavior.
- New APKPure V11.1.0 static/deep analysis and binary comparison must be confirmed from current GitHub Actions runs and generated reports before claiming completion.
- Unit tests, Python syntax validation, generated reports and latest workflow conclusions must be checked explicitly. Do not infer a run succeeded just because the workflow file exists.

## Build status

- No CHATGPT MOD APK has been produced.
- The former Gradle-only scaffold does not represent the intended product because it would build a standalone app rather than modify APKPure Duel Links.
- Final build stays blocked until V11.1.0 analysis determines package structure (including XAPK split/OBB requirements), feature candidates and a real APK-based patch/build path.
- APK signing compatibility must be verified separately. If Platinmods private signing key is unavailable, matching its signer cannot be assumed.

## Scope

Safe local UI/accessibility/settings and compatibility changes, plus isolated offline simulations, may be considered. Do not implement code intended to unfairly alter live online duel results. Preserve the original Release assets and do not commit generated APK binaries.

## NEXT ACTION

Verify the latest APK Static Analysis, APK Code Analysis (APKPure Base), and Checkpoint Validation runs. Inspect APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, and APK_VARIANT_COMPARISON.md; fix any new failures before updating MOD_CANDIDATES.md with V11.1.0 evidence and selecting features. Keep Build App blocked until that evidence is reviewed.
