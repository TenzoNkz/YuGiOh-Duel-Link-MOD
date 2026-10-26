# Mod Candidate Register

Status labels: NOT_INSPECTED, INDICATED_BY_STATIC_EVIDENCE, NEEDS_DEEPER_ANALYSIS, TESTED_IN_ISOLATED_ENVIRONMENT, NOT_SUPPORTED.

The source APK's archive integrity and inventory are now verified. Feature-by-feature logic analysis is still pending the JADX/Apktool report. Do not promote any candidate to working status based only on menu labels or string hits.

## Structural evidence already verified
- Three DEX files are present: classes.dex, classes2.dex, classes3.dex.
- Twenty native shared libraries are present across arm64-v8a and armeabi-v7a.
- Unity/IL2CPP indicators are present: assets/bin/Data/, libunity.so, libil2cpp.so, and global-metadata.dat.
- libduel.so and libplatinmods.so are present in the APK.
- The exact role of those libraries has not yet been established by code tracing.

## Candidate register

| Candidate | Current status | Evidence needed | Scope |
|---|---|---|---|
| Existing AutoPlay Bot toggle | NOT_INSPECTED | Trace menu label, callback, native/Dex implementation, prerequisites, and effects; do not infer function from label alone | Audit existing behavior |
| Show Monster & Status Details | NOT_INSPECTED | Find code/resource hits and trace where displayed values come from | Prefer local visual analysis |
| Reveal Card Face | NOT_INSPECTED | Trace the feature and determine the source/availability of card information | Analyze visibility and data flow |
| Add a new menu toggle | NEEDS_DEEPER_ANALYSIS | Identify existing menu implementation, event wiring, and safe extension point | UI-only prototype may be possible |
| Visual/accessibility adjustments | NEEDS_DEEPER_ANALYSIS | Find UI/resources and verify changes remain local and compatible | Candidate for isolated testing |
| Offline damage-multiplier simulation | NOT_INSPECTED | Build a separate deterministic test model and verify its arithmetic with test cases | Offline simulation, not a live duel patch |
| Damage Multiplier affecting only the user's cards in online duels | NOT_INSPECTED | Determine where damage is calculated and whether the game is server-authoritative; static search alone will not prove feasibility | Do not implement a live-match cheat or claim it works |

## Per-candidate evidence template
For each candidate, record:
1. Exact APK and Release tag analyzed.
2. Exact APK path, source class/method/resource, native string, or symbol evidence with context.
3. What the evidence proves and what remains uncertain.
4. Dependencies, compatibility/crash risks, and whether behavior appears local or server-authoritative.
5. Reproducible test and outcome, if one is safely possible.
6. Final status label and reason.

No candidate may be marked as working based only on decompiled strings, menu labels, a successful build, or a speculative code path.
