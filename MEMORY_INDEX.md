# Memory Index

Canonical repository: TenzoNkz/YuGiOh-Duel-Link-MOD  
Canonical branch: main

## Primary mode prompts
- CHAT_TRANSFER.md — copy-ready prompts for Diskusi!, Eksekusi Full!, and Eksekusi Build App!, plus auxiliary Chat Stuck! recovery.
- CHAT_RULES.md — exact behavior and boundaries of each mode.

## Read in this order
1. CHAT_TRANSFER.md
2. CHAT_RULES.md
3. PROJECT_STATE.md
4. HANDOVER.md
5. CHATGPT_MOD_BUILD_REPORT.md
6. APP_ANALYSIS_REPORT.md
7. APK_CODE_ANALYSIS.md
8. MOD_CANDIDATES.md
9. ANALYSIS_LOG.md
10. README.md

## GitHub workflows and scripts
- Source Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- APK Static Analysis: .github/workflows/apk-static-analysis.yml
- APK Code Analysis: .github/workflows/apk-code-analysis.yml
- Checkpoint Validation: .github/workflows/checkpoint-validation.yml
- CHATGPT Mod Build: .github/workflows/build-chatgpt-mod.yml
- APK inventory: tools/analyze_release_apk.py
- APK code scan: tools/analyze_apk_code.py
- Build preflight validator: tools/validate_chatgpt_mod_source.py
- Structural report: APP_ANALYSIS_REPORT.md
- Code report: APK_CODE_ANALYSIS.md
- Build report: CHATGPT_MOD_BUILD_REPORT.md

## Persistence rule
Committed GitHub records and verified Release/Actions output are durable project memory. New chats must reload the live branch and current run status, then continue from HANDOVER.md. Do not treat chat-only context as saved or call a build successful without a confirmed artifact.
