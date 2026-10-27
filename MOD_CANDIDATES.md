# CHATGPT MOD Candidate Register

**Canonical mod base:** APKPure Original V11.1.0, Release tag APKPure_Latest.  
**Comparison-only reference:** Platinmods V11.1.0, Release tag Latest.  
**Do not build from Platinmods.** All mod implementation must start from APKPure Original and use independently reviewed changes.

Status meanings:
- NOT_INSPECTED — no meaningful code evidence yet.
- INDICATED_BY_STATIC_EVIDENCE — a relevant string/class/resource exists, but feature behavior is not proven.
- NEEDS_DEEPER_ANALYSIS — evidence or call-flow mapping is incomplete.
- TESTED_IN_ISOLATED_ENVIRONMENT — behavior was demonstrated in an isolated test and the test evidence is recorded.
- NOT_SUPPORTED — no viable implementation path was established.
- APPROVED_FOR_IMPLEMENTATION — the user accepted the scope after the evidence review. This does not itself mean implemented.

## Evidence baseline

### Old Platinmods V11.0.0 evidence (historical only; not yet verified on V11.1.0)
- Decoded package name: jp.konami.duellinks.
- Unity/IL2CPP indicators, 3 DEX files, and 20 native shared libraries were inventoried.
- Decompiled com/platinmods/FloatingModMenuService.java contains generic menu-control construction and callbacks.
- com/platinmods/Preferences.java uses native Changes(...) callbacks and SharedPreferences-based preference loading/saving.
- com/platinmods/PMLauncher.java loads the platinmods native library.
- Strings in global-metadata.dat include ShowMonster/showMonster, CHEATCARD, PROCESS_DAMAGE variants; libduel.so includes DLL_DuelGetDamageValue and DLL_DuelComCheatCard.
- JADX reported 96 decompilation errors; code analysis was PARTIAL.
- None of these old reference findings proves a specific option works in APKPure V11.1.0.

### New APKPure V11.1.0 evidence
- APK/XAPK-aware tools have been added: tools/apk_inputs.py, tools/analyze_release_apk.py, tools/analyze_apk_code.py, and tools/compare_apk_variants.py.
- The actual V11.1.0 analysis results must be taken from APP_ANALYSIS_REPORT.md, APK_CODE_ANALYSIS.md, APK_VARIANT_COMPARISON.md and the corresponding current Actions runs.
- Until those reports are updated and reviewed, APKPure feature candidates below remain preliminary.

## Candidate register

| Candidate | Preliminary feasibility | Evidence now | Next validation | Implementation boundary |
|---|---|---|---|---|
| Original CHATGPT MOD floating menu, title exactly CHATGPT MOD | High for designing the UI; integration risk unknown | Our intended design is clear; old Platinmods reference shows a floating menu architecture, not reusable source code | Inspect APKPure entry/activity/service structure and determine a safe integration path | Custom implementation from APKPure base; do not copy Platinmods binaries blindly |
| Menu drag/minimize/restore, size, opacity, theme | High for UI implementation | General Android UI capabilities; actual game-window integration not tested | Confirm window/lifecycle constraints on target Android versions | Local presentation/accessibility only |
| Toggle, slider, dropdown, text-input controls | High for menu UI; unknown for game effect | Generic controls appeared in old Platinmods V11.0.0 decompilation | Implement owned menu controls and test state handling | UI control may exist without a gameplay callback |
| Persist menu settings | High for app-owned settings | Old reference exposed SharedPreferences reads/writes | Design own preference namespace, migration, reset and persistence tests | Store CHATGPT MOD settings independently |
| Show Monster & Status Details | Unknown to medium | ShowMonster/showMonster strings exist in old Platinmods V11.0.0 metadata only | Find the equivalent path in APKPure V11.1.0, identify source fields and rendering context | Prefer information already available to the local client; no opponent-secret reveal |
| Reveal Card Face | Unknown | No verified base callback or mapping | Search base resources/DEX/native metadata, establish data-visibility path | Do not expose hidden opponent information in online duels |
| AutoPlay Bot | Unknown | An old reference screenshot reportedly showed this label; code mapping not established | Locate exact feature declaration/callback in reference, then check whether APKPure has a legitimate local automation path | No automation that abuses online matches or bypasses fair-play controls |
| FPS/performance/display/accessibility settings | Medium | No V11.1.0 evidence yet | Inspect Unity config and Android display behavior; test changes in isolated conditions | Prefer settings that improve presentation/performance without changing duel outcomes |
| Offline damage-rule simulator | High as a separate deterministic test model | Can be implemented independently of the proprietary game binary | Define test vectors and verify calculations with unit tests | Offline sandbox only; not a live-game patch |
| Damage multiplier / Cheat Card behavior in live online duels | Not an implementation target | Old reference strings are clues only; call flow and server authority are unverified | No live-match outcome implementation | Excluded because it unfairly changes competitive results |

## Evidence required before feature approval

1. Exact input Release tag, asset filename, container SHA-256, selected APK SHA-256 and archive/package details.
2. Exact class, method, resource, native symbol or IL2CPP metadata reference with surrounding context.
3. A clear separation of verified fact, hypothesis and unknown behavior.
4. Impact on package compatibility, split/OBB payloads, crash risk and signer/update behavior.
5. Reproducible isolated test and result for anything claimed to work.
6. User-approved scope and status transition before implementation.

## Current decision

Start by completing APKPure V11.1.0 reverse engineering and archive comparison. The first candidate should be the custom CHATGPT MOD menu and its own persisted UI preferences. Do not claim any game-function toggle is possible until base-code evidence supports it. Do not start final APK packaging yet.
