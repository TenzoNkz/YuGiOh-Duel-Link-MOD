# Mod Candidate Register

Status labels: NOT_INSPECTED, INDICATED_BY_STATIC_EVIDENCE, NEEDS_DEEPER_ANALYSIS, TESTED_IN_ISOLATED_ENVIRONMENT, NOT_SUPPORTED.

APK checksum and archive CRC verification passed. The deeper code-analysis workflow succeeded, but the report is partial because JADX reported 96 decompilation errors. Static strings and UI labels do not prove gameplay behavior.

## Verified architecture evidence
- Decoded manifest package: jp.konami.duellinks.
- Unity/IL2CPP indicators and 20 native shared libraries; notable names include libduel.so and libplatinmods.so.
- Decompiled com/platinmods/FloatingModMenuService.java creates generic menu widgets. Toggle callbacks call Preferences.changeFeatureBoolean(...) and localChanges(...).
- com/platinmods/Preferences.java declares native Changes(Context, int, int, boolean, String) and saves preferences.
- com/platinmods/PMLauncher.java declares native initialize(Context) and calls System.loadLibrary("platinmods").
- libplatinmods.so contains JNI string names for getFeatureList, settingsList, and Preferences_Changes.
- global-metadata.dat contains ShowMonster/showMonster, CHEATCARD, PROCESS_DAMAGE variants; libduel.so includes DLL_DuelGetDamageValue and DLL_DuelComCheatCard strings.
- Evidence does not establish call flow, feature ID mapping, ownership filters, server authority, or successful in-game effects.

## Candidate register

| Candidate | Current status | Evidence / next check | Scope |
|---|---|---|---|
| Existing AutoPlay Bot toggle | NEEDS_DEEPER_ANALYSIS | Screenshot proves its label is shown, but the current static scan does not map it to a native feature ID/callback. Trace getFeatureList/native dispatch. | Audit only |
| Show Monster & Status Details | INDICATED_BY_STATIC_EVIDENCE | ShowMonster/showMonster strings exist in IL2CPP metadata, but linkage to the exact overlay label and its data source is not proven. | Trace data path; favor local display |
| Reveal Card Face | NEEDS_DEEPER_ANALYSIS | Exact label/feature ID and callback mapping remain unverified. | Analyze visibility/data flow |
| Add another menu toggle (UI only) | INDICATED_BY_STATIC_EVIDENCE | Generic toggle controls and preference/native callbacks are present; UI is supported by the existing framework, but any gameplay effect needs its own native dispatch. | UI/architecture study only |
| Visual/accessibility adjustment of overlay | INDICATED_BY_STATIC_EVIDENCE | Framework source contains menu dimensions/colors and local UI-control construction. | Test locally; no gameplay change |
| Offline damage-multiplier simulation | NOT_INSPECTED | Create a separate deterministic model with unit tests for selected entities. | Offline simulation only |
| Damage Multiplier affecting only the user's cards in online duels | NEEDS_DEEPER_ANALYSIS | Damage-related strings exist, but call sites, ownership-specific behavior, and server-authoritative acceptance are unknown. | No live-match cheat implementation |

## Required candidate evidence
1. Exact APK Release/tag and checksum.
2. Exact class/method/resource/native symbol and surrounding context.
3. What is directly proven versus hypothesized.
4. Dependencies, compatibility/crash risks, and local-versus-server behavior if known.
5. Reproducible isolated test and result if safe.
6. Status label and justification.

Do not call a mod working based only on strings, labels, decompilation, or a successful build.
