# Memory Index

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Project: static APK analysis and evidence-based evaluation of possible Duel Links modifications.

## Read in this order
1. CHAT_TRANSFER.md — copy-ready load-and-continue prompts.
2. CHAT_RULES.md — modes, evidence standards, and scope.
3. PROJECT_STATE.md — current verified state and immediate next action.
4. HANDOVER.md — exact last checkpoint and next action.
5. APP_ANALYSIS_REPORT.md — first-stage checksum/archive/DEX/native inventory.
6. APK_CODE_ANALYSIS.md — Apktool/JADX code scan; check its status and limitations.
7. MOD_CANDIDATES.md — candidate-by-candidate evidence status.
8. ANALYSIS_LOG.md — dated record of verified findings, workflow runs, failures, and decisions.
9. README.md — project entry point and GitHub workflow guide.

## GitHub locations
- Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- APK Static Analysis: .github/workflows/apk-static-analysis.yml
- APK Code Analysis: .github/workflows/apk-code-analysis.yml
- Checkpoint Validation: .github/workflows/checkpoint-validation.yml
- Static inventory script: tools/analyze_release_apk.py
- Deep static analysis script: tools/analyze_apk_code.py
- Structural report: APP_ANALYSIS_REPORT.md
- Code report: APK_CODE_ANALYSIS.md
- Latest refined code run at checkpoint: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274001397

## Persistence rule
Committed GitHub files and verified Release/Actions evidence are the durable project memory. After meaningful progress, update the reports and checkpoint docs. Never treat chat-only context as saved, and never infer success from a workflow merely existing.
