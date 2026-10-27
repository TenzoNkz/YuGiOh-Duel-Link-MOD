# Chat Rules — Yu-Gi-Oh! Duel Links MOD Workspace

## Source of truth
- Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Canonical branch: main
- Durable state comes from committed GitHub files, the source Release, and verified Actions runs—not from chat transcript assumptions.
- Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, CHATGPT_MOD_BUILD_REPORT.md, and MOD_CANDIDATES.md before substantial work.

## Three primary modes
- **Diskusi!** — discuss/review all relevant code and architecture, trace evidence, plan changes. No edits, commits, builds, patches, or workflow triggers.
- **Eksekusi Full!** — execute the agreed source-code task end-to-end: edit files, implement features within scope, run tests/checks, fix regressions, commit, and update durable records. APK packaging is separate.
- **Eksekusi Build App!** — build/QC only for the latest agreed source. Validate the Android project, require the app label "CHATGPT Mod", run the build workflow, verify artifact/digest, and update CHATGPT_MOD_BUILD_REPORT.md. Only minimum build fixes are allowed; new feature work returns to Eksekusi Full!.
- **Chat Stuck!** is an auxiliary checkpoint command, not a replacement for the three modes.

## Durable record contract
- CHAT_TRANSFER.md contains copy-ready load-and-continue prompts.
- MEMORY_INDEX.md defines the authoritative read order.
- PROJECT_STATE.md records verified project status.
- HANDOVER.md records the exact last verified step and one NEXT ACTION.
- ANALYSIS_LOG.md is chronological; append new verified milestones rather than rewriting history.
- APP_ANALYSIS_REPORT.md records static archive inventory.
- APK_CODE_ANALYSIS.md records Apktool/JADX/native-string findings and tooling limitations.
- CHATGPT_MOD_BUILD_REPORT.md records build state, artifact metadata, and build blockers.
- MOD_CANDIDATES.md records per-feature evidence and status.

## GitHub workflow contract
- APK Static Analysis treats the source Release APK as data and produces APP_ANALYSIS_REPORT.md.
- APK Code Analysis uses Apktool/JADX for static inspection and produces APK_CODE_ANALYSIS.md. A successful Actions job does not mean decompilation is complete if the report says PARTIAL.
- Checkpoint Validation checks required files and recovery-prompt markers.
- CHATGPT Mod Build validates a source project under chatgpt-mod/, requires Android application label "CHATGPT Mod", builds a Debug APK, uploads it as a workflow artifact, and updates CHATGPT_MOD_BUILD_REPORT.md.
- Always inspect actual job conclusion, report commit, and artifact. Never invent a successful build or test result.

## Build preconditions
- The source Release APK is a binary analysis input, not a Gradle source tree.
- A buildable Android project must exist under chatgpt-mod/ before a new app APK can be built. If it is absent, record BLOCKED_SOURCE_PROJECT_MISSING and do not relabel/re-upload the existing APK as a new build.
- Keep built APKs out of Git history. Artifact upload is the default; no public Release is created automatically.
- Any build must be tied to the exact source commit, Android label, workflow URL, file size, and SHA-256.

## Safety and scope
- Static analysis must inspect the APK as data; never execute/install it in the analysis runner.
- Preserve the original APK asset and its evidence.
- Do not claim functionality based only on labels, strings, or symbols.
- Live online-match modifications intended to unfairly alter duel outcomes are out of implementation scope. Safe UI/accessibility changes, compatibility fixes, and isolated/offline simulations may be considered.
- Do not redistribute modified proprietary game binaries without the necessary rights.

## Definition of done
1. The requested code/workflow/docs exist on GitHub.
2. Relevant checks and builds have verified outcomes or clearly marked blockers.
3. Reports and checkpoints agree with the actual latest run.
4. HANDOVER.md contains one precise next action.
