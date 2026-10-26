# Mod Candidate Register

Status labels: NOT_INSPECTED, INDICATED_BY_STATIC_EVIDENCE, NEEDS_DEEPER_ANALYSIS, TESTED_IN_ISOLATED_ENVIRONMENT, NOT_SUPPORTED.

The archive inventory is verified. Initial deep analysis found a Platinmods menu framework and damage-related native symbol names, but JADX returned partial output. These clues guide the next trace; they do not prove any feature works.

## Structural and code evidence already observed
- Three DEX files are present; twenty native shared libraries are present across arm64-v8a and armeabi-v7a.
- Unity/IL2CPP indicators include assets/bin/Data/, libunity.so, libil2cpp.so, and global-metadata.dat.
- Android manifest package decoded by Apktool: jp.konami.duellinks.
- Decompiled framework classes include com.platinmods.FloatingModMenuService, com.platinmods.PMLauncher, and com.platinmods.Preferences.
- PMLauncher loads the native library platinmods.
- Native JNI string exports include Java_com_platinmods_FloatingModMenuService_getFeatureList, Java_com_platinmods_FloatingModMenuService_settingsList, and Java_com_platinmods_Preferences_Changes.
- libduel.so contains strings DLL_DuelGetDamageValue and DLL_DuelComCheatCard. Symbol strings alone do not prove call flow, modification feasibility, ownership filtering, or server acceptance.
- JADX 1.5.6 produced 8,194 Java source files but reported 96 decompilation errors in the initial run. Deep report status remains partial pending a refined scan.

## Candidate register

| Candidate | Current status | Evidence / next test | Scope |
|---|---|---|---|
| Existing AutoPlay Bot toggle | NEEDS_DEEPER_ANALYSIS | Trace feature-list IDs and native callbacks; screenshot proves the label is present in the overlay, not that the function works | Audit existing behavior |
| Show Monster & Status Details | NEEDS_DEEPER_ANALYSIS | Search exact feature ID/label and trace the callback plus data source | Prefer local visual analysis |
| Reveal Card Face | NEEDS_DEEPER_ANALYSIS | Search exact feature ID/label and trace the callback/data source | Analyze visibility and data flow |
| Add a new menu toggle | INDICATED_BY_STATIC_EVIDENCE | Generic menu framework and JNI methods for getFeatureList/settingsList/preferences changes exist; exact extension point is not yet traced | UI architecture study; no live-match cheat |
| Visual/accessibility adjustments | NEEDS_DEEPER_ANALYSIS | Inspect UI layout/resources and assess local-only behavior | Candidate for isolated testing |
| Offline damage-multiplier simulation | NOT_INSPECTED | Create a separate deterministic test model with tests for only the player's selected entities | Offline simulation, not a live duel patch |
| Damage Multiplier affecting only the user's cards in online duels | NEEDS_DEEPER_ANALYSIS | libduel.so contains DLL_DuelGetDamageValue and DLL_DuelComCheatCard string references; call sites, ownership checks, server authority, and feasible safe test path remain unknown | Do not implement a live-match cheat or claim it works |

## Per-candidate evidence template
For each candidate, record:
1. Exact APK and Release tag analyzed.
2. Exact APK path, source class/method/resource, native string, or symbol evidence with context.
3. What the evidence proves and what remains uncertain.
4. Dependencies, compatibility/crash risks, and whether behavior appears local or server-authoritative.
5. Reproducible test and outcome, if one is safely possible.
6. Final status label and reason.

No candidate may be marked as working based only on decompiled strings, menu labels, a successful build, or a speculative code path.
