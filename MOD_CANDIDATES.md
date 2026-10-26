# Mod Candidate Register

Status labels: NOT_INSPECTED, INDICATED_BY_STATIC_EVIDENCE, NEEDS_DEEPER_ANALYSIS, TESTED_IN_ISOLATED_ENVIRONMENT, NOT_SUPPORTED.

The APK archive integrity is verified. Initial decompilation found Platinmods menu-framework classes and damage-related native string names, but JADX reported 96 errors. No feature is currently confirmed as working from the code report alone.

## Verified structural/code clues
- Three DEX files and 20 native shared libraries across arm64-v8a and armeabi-v7a.
- Unity/IL2CPP indicators: assets/bin/Data/, libunity.so, libil2cpp.so, and global-metadata.dat.
- Apktool-decoded package: jp.konami.duellinks.
- Decompiled classes include com.platinmods.FloatingModMenuService and PMLauncher; PMLauncher loads native library platinmods.
- Native JNI strings include getFeatureList, settingsList, and Preferences_Changes callbacks.
- libduel.so printable strings include DLL_DuelGetDamageValue and DLL_DuelComCheatCard.
- These strings do not prove invocation/call flow, parameters, card ownership filters, server authority, or that any feature works.

## Candidate register

| Candidate | Current status | What evidence is next | Scope |
|---|---|---|---|
| Existing AutoPlay Bot toggle | NEEDS_DEEPER_ANALYSIS | Locate the exact feature ID/label and trace its native callback; a menu label is not proof of effect | Audit existing behavior |
| Show Monster & Status Details | NEEDS_DEEPER_ANALYSIS | Locate feature label/ID and determine what values are read and displayed | Prefer local visual analysis |
| Reveal Card Face | NEEDS_DEEPER_ANALYSIS | Locate feature label/ID and determine the source of card-face information | Analyze visibility/data flow |
| Add another menu toggle | INDICATED_BY_STATIC_EVIDENCE | Generic menu framework and JNI callbacks exist; trace how feature strings/IDs are parsed and dispatched | UI architecture study only |
| Visual/accessibility adjustments | NEEDS_DEEPER_ANALYSIS | Inspect relevant layout/resources and test local-only display changes in isolation | Potential isolated test |
| Offline damage-multiplier simulation | NOT_INSPECTED | Create a separate deterministic test model with unit tests for selected entities | Offline simulation only |
| Damage multiplier affecting only the user's cards in online duels | NEEDS_DEEPER_ANALYSIS | Damage-related symbols were found, but call sites, ownership checks, and server-authoritative behavior are unknown | Do not implement or provide instructions for live-match cheating |

## Per-candidate evidence template
1. Exact APK Release/tag and checksum.
2. File/class/method/resource/symbol evidence with context.
3. What is proven and what remains a hypothesis.
4. Dependencies, compatibility/crash risks, and local-vs-server behavior if known.
5. Reproducible isolated test result if applicable.
6. Status label with justification.

Do not label a mod as working based only on strings, menu labels, successful decompilation, or a successful build.
