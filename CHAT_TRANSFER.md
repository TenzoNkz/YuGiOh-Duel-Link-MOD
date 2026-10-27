# Chat Transfer — JE X FYZ-Style Load + Continue

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Canonical mod base: APKPure Original — https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest  
Comparison-only reference: Platinmods — https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Latest

This file has the three primary modes. Copy the full prompt under the mode you need and paste it into a new chat. The new chat must reload live GitHub evidence first; the old transcript is not the source of truth.

## Mode 1 — Diskusi!

Diskusi!
GITHUB LOAD + CONTINUE — DISCUSSION / ALL-CODE REVIEW ONLY

PROJECT: Yu-Gi-Oh! Duel Links MOD
REPOSITORY: TenzoNkz/YuGiOh-Duel-Link-MOD
BRANCH: main

MANDATORY LOAD
Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, IL2CPP_ANALYSIS_REPORT.md, APK_VARIANT_COMPARISON.md, CHATGPT_MOD_BUILD_REPORT.md, MOD_CANDIDATES.md, MOD_INTEGRATION_PLAN.md, and ANALYSIS_LOG.md from the current main branch. Check current GitHub Actions, Release metadata, repository tree, and code/report evidence relevant to the discussion.

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
5. Update APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, IL2CPP_ANALYSIS_REPORT.md, APK_VARIANT_COMPARISON.md, MOD_CANDIDATES.md, PROJECT_STATE.md, HANDOVER.md, MEMORY_INDEX.md, and append ANALYSIS_LOG.md when applicable. Record exact test results and run URLs.
6. Keep generated binaries/artifacts out of Git history. Preserve the original Release APK and its digest.
7. APKPure Original V11.1.0 is the only intended mod base. The APKPure Release is currently XAPK; analyze its embedded APK/split/OBB structure and do not assume renaming or selecting one member yields a working single APK. Do not create a standalone Gradle demo and claim it is the modified game.
8. Do not implement live online-duel cheats or code designed to unfairly alter real-match outcomes. Safe UI/accessibility changes, defensive/compatibility fixes, and offline simulations can be implemented.
9. Current state: APKPure XAPK integrity passes. The owned UI-only helper is in src/mod_menu/com/chatgptmod/menu/ModMenu.java; the gated APKPure patcher is tools/build_chatgpt_mod.py. CI has compiled Java to DEX and passed patcher primitive tests, but no APK has been built/installed/runtime-tested. The first-stage UI scope remains awaiting explicit owner approval in MOD_CANDIDATES.md.

DONE CRITERIA
- Code changes are committed to main and verified.
- Relevant tests/Actions results are checked, not assumed.
- Durable project state and one exact NEXT ACTION are recorded.
- Build work is handed to Eksekusi Build App! when ready.

## Mode 3 — Eksekusi Build App!

Eksekusi Build App!
GITHUB LOAD + CONTINUE — APKPURE-BASED CHATGPT MOD BUILD / QC ONLY

PROJECT: Yu-Gi-Oh! Duel Links MOD workspace
REPOSITORY: TenzoNkz/YuGiOh-Duel-Link-MOD
BRANCH: main
REQUIRED ANDROID APPLICATION LABEL: CHATGPT Mod
BUILD WORKFLOW: .github/workflows/build-chatgpt-mod.yml
BUILD REPORT: CHATGPT_MOD_BUILD_REPORT.md
BASE RELEASE: APKPure_Latest (APKPure Original V11.1.0)  
REFERENCE ONLY: Latest (Platinmods V11.1.0)  
EXPECTED OUTPUT: a verified modified .apk  
MENU TITLE: CHATGPT MOD

MANDATORY LOAD
1. Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, CHATGPT_MOD_BUILD_REPORT.md, APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, IL2CPP_ANALYSIS_REPORT.md, APK_VARIANT_COMPARISON.md, MOD_CANDIDATES.md, MOD_INTEGRATION_PLAN.md, and ANALYSIS_LOG.md from live GitHub.
2. Inspect latest main, current source tree, last code commit, build workflow, and Actions status.
3. Confirm APKPure remains the sole base, Platinmods is reference-only, the latest analysis reports are complete enough for the agreed feature plan, and the custom menu title is CHATGPT MOD.

BUILD / QC
1. This mode is for packaging and build-quality control, not new feature development.
2. The APKPure patcher source and UI-only helper now exist. Use the GitHub Actions workflow "CHATGPT MOD APK Build / QC" only after MOD_CANDIDATES.md explicitly marks Build approval: APPROVED_FOR_IMPLEMENTATION and the required signing secrets have been configured. The output must be the modified game APK, not a standalone Gradle app.
3. Review build logs, the generated APK artifact, file size, SHA-256, and report. Do not report success unless the run and artifact are confirmed.
4. Fix only build/configuration blockers required to build the already-agreed safe code. New feature work must return to Eksekusi Full!.
5. The workflow uploads the APK as a temporary GitHub Actions artifact and records CHATGPT_MOD_BUILD_REPORT.md. Do not commit APK binaries, overwrite the source Release, or publish a new Release by default.
6. If explicit feature approval or signing secrets are missing, or if the end-to-end patcher fails any source, hook, split, signing or integrity checks, mark the build BLOCKED and do not claim an APK exists. Never rename the XAPK or copy Platinmods binaries. The patcher primitive tests and Java-to-DEX compilation are not proof that the actual game APK builds or runs.
7. Verify the in-game menu title is exactly "CHATGPT MOD". Record base asset/container digest, selected APK digest, output APK size/SHA-256, signer verification, run URL, artifact name, test result, and limitations.

SCOPE
The build must start from APKPure Original; keep the original Release unchanged and treat Platinmods as comparison-only. The current patcher merges validated ARM64 native libraries into a single-APK test candidate, but the result is not yet built or runtime-tested and is ARM64-only. Safe local UI/accessibility, compatibility and offline simulations may be considered; live-online-duel outcome cheating is out of scope.

DONE CRITERIA
- APKPure base and reference-only Release identified.
- Reverse-engineering/patch plan approved before build.
- In-game menu title verified as "CHATGPT MOD".
- GitHub Actions run result and APK artifact checked.
- CHATGPT_MOD_BUILD_REPORT.md committed with exact status, size, digest, and run URL, or a truthful blocker.
- HANDOVER.md contains one exact next action.

## Auxiliary recovery — Chat Stuck!

Chat Stuck!
GITHUB CHECKPOINT ONLY — DO NOT START NEW FEATURES

Inspect current main, reports, source Release, and Actions runs. Update HANDOVER.md, PROJECT_STATE.md, MEMORY_INDEX.md, and append ANALYSIS_LOG.md with only verified state, active jobs, blockers, relevant URLs, and one exact NEXT ACTION. Commit the checkpoint if tools permit. Do not claim unsaved chat context is durable.
