# Chat Transfer — Load + Continue

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Canonical APK Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0

This file contains reusable prompts. Copy a prompt together with its first command label. Do not use the old chat transcript as the source of truth; recover the latest verified state from GitHub.

## Prompt A — Diskusi!

Diskusi!
GITHUB LOAD + CONTINUE — DISCUSSION ONLY

PROJECT: Yu-Gi-Oh! Duel Links MOD
CANONICAL REPOSITORY: TenzoNkz/YuGiOh-Duel-Link-MOD
CANONICAL BRANCH: main
CANONICAL RELEASE: Platinmods_V11.0.0

Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, MOD_CANDIDATES.md, and ANALYSIS_LOG.md from the live GitHub repository. Then inspect current repository, Release, and Actions evidence as needed.

Resume the discussion from the exact latest verified checkpoint. Explain which facts are verified, which are hypotheses, and what the next decision is. This mode is discussion/planning only: do not edit source or docs, trigger workflows, or build/patch APKs. Do not ask for an APK upload if the canonical public Release is available.

## Prompt B — Eksekusi Analisa APK!

Eksekusi Analisa APK!
CHAT-LIMIT LOAD + CONTINUE — GITHUB APK ANALYSIS WORKFLOW

PROJECT: Yu-Gi-Oh! Duel Links MOD
CANONICAL REPOSITORY: TenzoNkz/YuGiOh-Duel-Link-MOD
CANONICAL BRANCH: main
CANONICAL RELEASE: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0

MANDATORY LOAD
1. Read CHAT_TRANSFER.md, CHAT_RULES.md, MEMORY_INDEX.md, PROJECT_STATE.md, HANDOVER.md, APP_ANALYSIS_REPORT.md, MOD_CANDIDATES.md, and ANALYSIS_LOG.md from live GitHub first.
2. Verify the current main branch, release tag/assets/digest, latest APK Static Analysis Actions run, latest Checkpoint Validation run, and current report contents.
3. Treat GitHub committed files and verified Actions output as the durable source of truth, not prior chat memories.

EXECUTION
1. Continue from HANDOVER.md's exact NEXT ACTION without recapping unnecessarily.
2. Use GitHub Actions to obtain and inspect the APK from the public Release; do not ask the user to re-upload the same APK just because the chat changed.
3. Inspect only as data. Never execute the APK. Use report evidence to guide each subsequent analysis stage.
4. Start with release asset digest, archive integrity, file inventory, DEX and native libraries, and likely engine indicators. Clearly mark what the first-stage workflow does not decode or prove.
5. Evaluate existing toggles and proposed candidates one by one. Cite concrete APK paths/classes/symbols and tool outputs whenever available. Do not state a feature works until there is reproducible test evidence.
6. If the workflow has not run, initiate the available workflow if tool permissions support it; otherwise give exact GitHub UI steps to run it. Never claim success while pending.
7. After verified progress, update APP_ANALYSIS_REPORT.md, MOD_CANDIDATES.md, PROJECT_STATE.md, HANDOVER.md, MEMORY_INDEX.md, and append ANALYSIS_LOG.md. Keep the repository consistent and commit all durable findings.
8. If a tool cannot download binary Release assets, use the repository's GitHub Actions workflow as the binary-processing path; do not falsely claim direct binary access.
9. Keep live online-match cheat implementation out of scope; safe static research and isolated/offline simulations may be considered.

DONE CRITERIA
- Exact Action run URL and conclusion are recorded.
- The generated report's measured facts and limitations are reviewed.
- Candidate statuses reflect evidence, not assumptions.
- HANDOVER.md contains one specific next action for the next chat.

## Prompt C — Eksekusi Full!

Eksekusi Full!
GITHUB FULL EXECUTION — DOCUMENTATION / WORKFLOW / VERIFIED ANALYSIS ONLY

Load all current checkpoint files and live repository/Release/Actions evidence before acting. Continue from HANDOVER.md. Carry the agreed repository, documentation, automation, or static-analysis task through to verified completion. Run relevant checks, inspect results, update all durable project records, and commit changes. Never fabricate test results or report a pending workflow as successful. Do not execute the APK or implement a live-match cheat.

## Prompt D — Chat Stuck!

Chat Stuck!
GITHUB CHECKPOINT ONLY — DO NOT START NEW FEATURES

Inspect the latest repository state, Release metadata, reports, and Actions runs. Update HANDOVER.md, PROJECT_STATE.md, MEMORY_INDEX.md, and append ANALYSIS_LOG.md with only verified progress, current blockers, links to relevant Actions runs, and one exact NEXT ACTION. Commit the checkpoint before ending if repository tools are available. Do not claim unsaved chat context is durable.
