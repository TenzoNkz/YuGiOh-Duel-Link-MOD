# Memory Index

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Project: static APK analysis and evidence-based evaluation of possible Duel Links modifications.

## Read in this order
1. CHAT_TRANSFER.md — reusable load-and-continue prompts for new chats.
2. CHAT_RULES.md — modes, source-of-truth rules, evidence standard, and scope.
3. PROJECT_STATE.md — current verified state and immediate next step.
4. HANDOVER.md — exact last checkpoint and next action.
5. APP_ANALYSIS_REPORT.md — first-stage APK inventory.
6. APK_CODE_ANALYSIS.md — Apktool/JADX output; check its status and decompiler limitations.
7. MOD_CANDIDATES.md — candidates, evidence status, and unknowns.
8. ANALYSIS_LOG.md — dated history of durable decisions, workflow runs, failures, and findings.
9. README.md — project entry point and GitHub workflow instructions.

## GitHub locations
- Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- APK Static Analysis: .github/workflows/apk-static-analysis.yml
- APK Code Analysis: .github/workflows/apk-code-analysis.yml
- Checkpoint Validation: .github/workflows/checkpoint-validation.yml
- Static inventory script: tools/analyze_release_apk.py
- Deep static analysis script: tools/analyze_apk_code.py
- Initial inventory report: APP_ANALYSIS_REPORT.md
- Deep code report: APK_CODE_ANALYSIS.md
- Latest refined code-analysis run observed: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40273558853

## Persistence rule
Only committed GitHub files and verified Release/Actions evidence survive chat transitions reliably. Update reports and checkpoint notes after meaningful progress. Never infer a completed analysis from the existence of a workflow alone.
