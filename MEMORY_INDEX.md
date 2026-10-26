# Memory Index

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main  
Project: static APK analysis and evidence-based evaluation of possible Duel Links modifications.

## Read in this order
1. CHAT_TRANSFER.md — copy-ready load-and-continue prompts.
2. CHAT_RULES.md — modes, evidence standards, and boundaries.
3. PROJECT_STATE.md — current verified state and next action.
4. HANDOVER.md — exact last checkpoint and one next action.
5. APP_ANALYSIS_REPORT.md — checksum, archive integrity, DEX/native inventory.
6. APK_CODE_ANALYSIS.md — manifest/JADX/native-string findings; check report status and limitations.
7. MOD_CANDIDATES.md — per-candidate evidence and current status.
8. ANALYSIS_LOG.md — verified findings, workflow runs, failures, decisions.
9. README.md — GitHub workflow guide.

## GitHub workflow and script paths
- Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- APK Static Analysis: .github/workflows/apk-static-analysis.yml
- APK Code Analysis: .github/workflows/apk-code-analysis.yml
- Checkpoint Validation: .github/workflows/checkpoint-validation.yml
- Inventory script: tools/analyze_release_apk.py
- Code-analysis script: tools/analyze_apk_code.py
- Structural report: APP_ANALYSIS_REPORT.md
- Code report: APK_CODE_ANALYSIS.md
- Latest successful code-analysis run: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40274382469

## Persistence rule
Committed GitHub files and verified Release/Actions evidence are the durable project memory. After each substantial finding, update reports, candidate statuses, and checkpoints. Never rely on chat-only context, and never infer success from the existence of a workflow alone.
