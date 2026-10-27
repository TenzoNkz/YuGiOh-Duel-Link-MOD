# Chat Rules — Yu-Gi-Oh! Duel Links CHATGPT MOD

## Canonical source of truth
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Branch: main
- Intended mod base: APKPure Original V11.1.0, Release tag APKPure_Latest.
- Comparison-only reference: Platinmods V11.1.0, Release tag Latest.
- Eventual output: a tested modified APK (.apk) with an in-game menu titled CHATGPT MOD.
- Do not use Platinmods as the build base or copy its binary components without separate evidence/review.

## Mode behavior
- **Diskusi!** — inspect the live repository, Releases, reports, code, and Actions; explain facts and unknowns; do not edit, commit, trigger workflows, patch binaries, or build.
- **Eksekusi Full!** — implement agreed scripts, tests, analysis workflow, docs, and safe feature work; run checks; update durable reports and handover. Current engineering priority is complete APKPure XAPK analysis and comparison with Platinmods before selecting features.
- **Eksekusi Build App!** — package/QC only after the chosen safe feature plan and an actual APKPure-based patch/build pipeline exist. It must not build a separate Gradle demo and describe it as modified Duel Links.
- **Chat Stuck!** — auxiliary checkpoint-only command.

## Analysis input rules
- Treat APK/XAPK as data only in static analysis; do not install or execute them in analysis workflows.
- Verify the Release's reported digest, calculate the downloaded container SHA-256, and calculate the selected primary APK SHA-256 separately.
- APKPure XAPK handling must list all embedded APKs and OBB payloads. Do not assume the primary APK alone represents a complete installable game.
- Compare APKPure and Platinmods at the archive-member level. File hashes indicate byte differences only; trace code/resources/symbols to understand semantics.
- Retain original Release files. Do not silently overwrite or republish them.
- Static reports must state exactly which version/tag was analyzed. Old Platinmods V11.0.0 findings must not be presented as confirmed V11.1.0 facts.
- A string, JNI name, symbol, resource label, or successful workflow does not prove feature behavior. Distinguish facts, hypotheses, and isolated test results.

## Build rules
- APKPure Original is the sole base for all CHATGPT MOD implementation.
- Final output should be a real modified .apk, not a renamed .xapk or independent demo application.
- The build remains blocked until reverse-engineering reports support an approved patch plan and an APK-based patch/build tool exists.
- Never claim the Platinmods signing identity can be reused without the required private signing key or a valid signing-certificate rotation chain. Check package ID, signer, versionCode, and split/OBB compatibility before promising in-place installation.
- Keep generated APK binaries/artifacts out of Git history; store deliverables as workflow artifacts unless publishing is explicitly agreed.

## Scope boundaries
- Safe local UI, accessibility, appearance, compatibility and settings persistence may be considered.
- Offline/sandbox simulations may be implemented and unit-tested.
- Do not implement features intended to unfairly manipulate outcomes in live online duels or expose hidden opponent information.

## Durable checkpoint contract
- CHAT_TRANSFER.md contains copy-ready prompts for the three primary modes.
- MEMORY_INDEX.md defines the read order.
- PROJECT_STATE.md records verified state and one next action.
- HANDOVER.md records the exact continuation point.
- ANALYSIS_LOG.md is chronological and must add only verified findings.
- APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, IL2CPP_ANALYSIS_REPORT.md and APK_VARIANT_COMPARISON.md must identify their exact input assets, tool results and limitations.
- MOD_CANDIDATES.md tracks each candidate's evidence and status.
- CHATGPT_MOD_BUILD_REPORT.md records the true build outcome and blockers.

## Definition of done
1. Correct repository files/workflow/scripts exist on main.
2. Python syntax checks and unit tests pass.
3. Current GitHub Actions runs and generated reports are inspected.
4. APKPure stays the source base; Platinmods stays comparison-only.
5. Build is never called successful without a confirmed modified APK artifact and documented tests.
6. HANDOVER.md contains one precise NEXT ACTION.
