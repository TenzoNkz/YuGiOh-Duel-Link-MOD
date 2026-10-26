# Memory Index

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Project: static APK analysis and evidence-based evaluation of possible Duel Links modifications.

## Read in this order
1. CHAT_TRANSFER.md — reusable load-and-continue prompts for new chats.
2. CHAT_RULES.md — modes, source-of-truth rules, evidence standard, and scope.
3. PROJECT_STATE.md — current verified state and immediate next step.
4. HANDOVER.md — exact last checkpoint and next action.
5. APP_ANALYSIS_REPORT.md — latest APK static-analysis report; inspect its status before relying on any findings.
6. MOD_CANDIDATES.md — candidates and evidence status, including unknowns.
7. ANALYSIS_LOG.md — dated history of durable decisions and milestones.
8. README.md — project entry point and GitHub workflow instructions.

## GitHub locations
- Source Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- APK Static Analysis workflow: .github/workflows/apk-static-analysis.yml
- Checkpoint validation workflow: .github/workflows/checkpoint-validation.yml
- Static analysis script: tools/analyze_release_apk.py
- Latest report: APP_ANALYSIS_REPORT.md

## Persistence rule
Only committed GitHub files and verified Release/Actions evidence survive chat transitions reliably. Update the reports and checkpoint notes after meaningful progress. Never infer a completed analysis from the existence of a workflow alone.
