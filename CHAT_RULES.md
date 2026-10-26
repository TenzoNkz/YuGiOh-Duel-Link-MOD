# Chat Rules — Yu-Gi-Oh! Duel Links MOD

## Source of truth
- Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Canonical branch: main
- Use current GitHub repository, Release metadata, Actions runs, and committed reports as durable evidence. Chat history is not the source of truth.
- Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, and MOD_CANDIDATES.md before continuing substantial work.

## Evidence and reporting
- Clearly distinguish verified facts, analysis findings, hypotheses, and unknowns.
- Do not claim APK contents were inspected until the relevant report or direct analysis proves it.
- A successful Release upload only proves that GitHub stores an asset; it does not prove the APK is valid, safe, compatible, or understood.
- Record exact release tag, asset filename, byte size, SHA-256, workflow run URL/status, and report path where available.
- Do not overwrite or delete the source Release asset during analysis.
- Do not treat strings, names, or UI labels as proof that a feature works.

## Modes
- Diskusi! — discussion, explanation, requirements, and planning only. Do not edit repository files, run analysis, or build anything unless explicitly asked to switch modes.
- Eksekusi Analisa APK! — operate the GitHub-based static-analysis workflows, inspect run evidence, update findings and checkpoint records. Do not execute the APK.
- Eksekusi Full! — carry out the agreed repository/documentation/workflow task end-to-end, run relevant checks, verify the resulting GitHub state, and update durable records. Stay within the stated task scope.
- Chat Stuck! — stop new feature work; update HANDOVER.md, PROJECT_STATE.md, MEMORY_INDEX.md, and ANALYSIS_LOG.md with verified state and the exact next action.

## GitHub workflows
- APK Static Analysis produces APP_ANALYSIS_REPORT.md: checksum, archive integrity, DEX/native file inventory, and engine filename indicators.
- APK Code Analysis produces APK_CODE_ANALYSIS.md: Apktool manifest decoding, JADX decompilation of DEX, text/resource matches, and selected native/IL2CPP strings.
- Checkpoint Validation checks memory-file presence and required transfer-prompt markers.
- Verify actual run conclusion and report commit before recording a workflow as successful.
- If a report commit loses a race with another push, inspect the run log and fix the workflow; do not silently ignore the failure.

## Safety and scope
- Static analysis must inspect files as data; never execute or install the APK in the analysis runner.
- Keep the original APK and all evidence intact.
- Do not claim that a candidate mod works without reproducible evidence.
- Changes that alter live online match outcomes or provide an unfair advantage are out of scope for implementation. Analysis can instead document architecture at a high level and propose isolated/offline simulations or visual/accessibility-only experiments.
- Do not publish or redistribute modified proprietary game binaries without the necessary rights.

## Definition of done
1. The requested repository/workflow change exists on GitHub.
2. Relevant Actions checks have a verified result or are explicitly marked pending.
3. Reports and checkpoint documents agree.
4. HANDOVER.md states the exact last verified step and one next action.
