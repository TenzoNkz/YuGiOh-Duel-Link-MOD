# Chat Transfer — JE X FYZ-Style Load + Continue

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Canonical source APK Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0

This file has the three primary modes. Copy the full prompt under the mode you need and paste it into a new chat. The new chat must reload live GitHub evidence first; the old transcript is not the source of truth.

## Mode 1 — Diskusi!

Diskusi!
GITHUB LOAD + CONTINUE — DISCUSSION / ALL-CODE REVIEW ONLY

PROJECT: Yu-Gi-Oh! Duel Links MOD
REPOSITORY: TenzoNkz/YuGiOh-Duel-Link-MOD
BRANCH: main

MANDATORY LOAD
Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, CHATGPT_MOD_BUILD_REPORT.md, MOD_CANDIDATES.md, and ANALYSIS_LOG.md from the current main branch. Check current GitHub Actions, Release metadata, repository tree, and code/report evidence relevant to the discussion.

PURPOSE
Discuss and review all relevant code: explain architecture, trace call flow, evaluate options, identify bugs and risks, propose changes, and choose the next engineering task. Continue the topic from the verified checkpoint rather than restarting the whole recap.

GUARDRAILS
- Discussion only. Do not edit files, commit, trigger workflows, build APKs, or patch binaries in this mode.
- Clearly distinguish verified facts, hypotheses, and unknowns.
- Use exact file paths, class/method names, line references, report evidence, or Actions links where available.
- Do not ask the user to upload the same APK while its canonical GitHub Release remains available.
- Keep the original Release asset unchanged.
- Live online-duel changes that unfairly alter match outcomes are not an implementation target. Safe local UI/accessibility work and offline simulations may be discussed.

END STATE
Summarize the decision and give one precise next step. Persist nothing in this mode; switch to Eksekusi Full! when code changes are authorized.

## Mode 2 — Eksekusi Full!

Eksekusi Full!
GITHUB LOAD + CONTINUE — FULL CODE EXECUTION

PROJECT: Yu-Gi-Oh! Duel Links MOD
REPOSITORY: TenzoNkz/YuGiOh-Duel-Link-MOD
BRANCH: main

MANDATORY LOAD
1. Read the durable records listed in MEMORY_INDEX.md from live GitHub.
2. Verify repository HEAD, source Release/tag/digest, current Actions runs, and the latest report/handover.
3. Continue from HANDOVER.md and the engineering decision made in Diskusi!; do not guess what task was agreed.

EXECUTION
1. Implement the agreed code changes end-to-end. This is the code-editing mode: create/edit source, scripts, tests, configuration, and docs as the task requires.
2. Inspect relevant call sites and dependencies before making changes; keep the patch focused and explain assumptions in the code/report.
3. Run relevant unit tests, static checks, validation scripts, and applicable GitHub Actions. Fix failures introduced by the change and verify the actual outcome.
4. Do not package/build the APK in this mode unless the task explicitly requires a build test; final APK packaging belongs to Eksekusi Build App!.
5. Update APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, MOD_CANDIDATES.md, PROJECT_STATE.md, HANDOVER.md, MEMORY_INDEX.md, and append ANALYSIS_LOG.md when applicable. Record exact test results and run URLs.
6. Keep generated binaries/artifacts out of Git history. Preserve the original Release APK and its digest.
7. If the repository lacks an app source project, do not claim an app was modified. Only establish an authorized, safely scoped source project when that is the agreed engineering task; do not pretend a standalone demo is the original game's patched APK.
8. Do not implement live online-duel cheats or code designed to unfairly alter real-match outcomes. Safe UI/accessibility changes, defensive/compatibility fixes, and offline simulations can be implemented.

DONE CRITERIA
- Code changes are committed to main and verified.
- Relevant tests/Actions results are checked, not assumed.
- Durable project state and one exact NEXT ACTION are recorded.
- Build work is handed to Eksekusi Build App! when ready.

## Mode 3 — Eksekusi Build App!

Eksekusi Build App!
GITHUB LOAD + CONTINUE — CHATGPT MOD APP BUILD / QC ONLY

PROJECT: Yu-Gi-Oh! Duel Links MOD workspace
REPOSITORY: TenzoNkz/YuGiOh-Duel-Link-MOD
BRANCH: main
REQUIRED ANDROID APPLICATION LABEL: CHATGPT Mod
BUILD WORKFLOW: .github/workflows/build-chatgpt-mod.yml
BUILD REPORT: CHATGPT_MOD_BUILD_REPORT.md
EXPECTED SOURCE PROJECT: chatgpt-mod/

MANDATORY LOAD
1. Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, CHATGPT_MOD_BUILD_REPORT.md, MOD_CANDIDATES.md, and ANALYSIS_LOG.md from live GitHub.
2. Inspect latest main, current source tree, last code commit, build workflow, and Actions status.
3. Confirm the latest ChatGPT-authored source changes are present and that the Android app label resolves exactly to "CHATGPT Mod".

BUILD / QC
1. This mode is for packaging and build-quality control, not new feature development.
2. Use the GitHub Actions workflow "CHATGPT Mod Build" to validate the checked-in Android Gradle source in chatgpt-mod/ and build its Debug APK.
3. Review build logs, the generated APK artifact, file size, SHA-256, and report. Do not report success unless the run and artifact are confirmed.
4. Fix only build/configuration blockers required to build the already-agreed safe code. New feature work must return to Eksekusi Full!.
5. The workflow uploads the APK as a temporary GitHub Actions artifact and records CHATGPT_MOD_BUILD_REPORT.md. Do not commit APK binaries, overwrite the source Release, or publish a new Release by default.
6. If chatgpt-mod/ does not exist or has no valid Android Gradle project, mark the build BLOCKED and report the reason. Do not rename or repackage the existing analysis APK and falsely call it a ChatGPT Mod build. Use Eksekusi Full! to create/modify authorized source before retrying.
7. Verify that the app's user-visible label is "CHATGPT Mod". Record the run URL, artifact name, SHA-256, build result, and known limitations.

SCOPE
The build path is limited to authorized app source, local UI/accessibility and compatibility changes, and offline/test simulations. Do not implement or package a feature that unfairly changes outcomes in live online duels. The source APK in Releases is an immutable analysis input, not an automatically modifiable source project.

DONE CRITERIA
- Latest source commit identified.
- Android label verified as "CHATGPT Mod".
- GitHub Actions run result and APK artifact checked.
- CHATGPT_MOD_BUILD_REPORT.md committed with exact status, size, digest, and run URL, or a truthful blocker.
- HANDOVER.md contains one exact next action.

## Auxiliary recovery — Chat Stuck!

Chat Stuck!
GITHUB CHECKPOINT ONLY — DO NOT START NEW FEATURES

Inspect current main, reports, source Release, and Actions runs. Update HANDOVER.md, PROJECT_STATE.md, MEMORY_INDEX.md, and append ANALYSIS_LOG.md with only verified state, active jobs, blockers, relevant URLs, and one exact NEXT ACTION. Commit the checkpoint if tools permit. Do not claim unsaved chat context is durable.
