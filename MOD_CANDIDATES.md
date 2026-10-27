# CHATGPT MOD Candidate Register

**Canonical mod base:** APKPure Original V11.1.0, Release tag APKPure_Latest.  
**Comparison-only reference:** Platinmods V11.1.0, Release tag Latest.  
**Do not build from Platinmods.** All implementation must start from APKPure Original and use independently reviewed changes.

Status meanings:
- NOT_INSPECTED — no meaningful code evidence yet.
- INDICATED_BY_STATIC_EVIDENCE — a relevant string/class/resource exists, but behavior is not proven.
- NEEDS_DEEPER_ANALYSIS — evidence or call-flow mapping is incomplete.
- TESTED_IN_ISOLATED_ENVIRONMENT — behavior was demonstrated in an isolated test and the test evidence is recorded.
- NOT_SUPPORTED — no viable implementation path was established.
- APPROVED_FOR_IMPLEMENTATION — user accepted a bounded feature scope after evidence review; this does not mean it has been implemented.

## Verified APKPure V11.1.0 package findings

- Current APKPure XAPK size is 92,726,986 bytes. Its expected and calculated SHA-256 match: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb. The previous hash 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16 belongs to the previous corrupt upload and is superseded.
- It contains jp.konami.duellinks.apk (55,854,706 bytes) and config.arm64_v8a.apk (36,869,159 bytes), with no OBB member detected.
- Both embedded APK outer CRC checks pass. The primary APK and ARM64 split both pass full inner ZIP CRC/decompression scans.
- The primary APK has 3,368 entries and three DEX files; the config split has nine native libraries. Current primary SHA-256: e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d. Current ARM64 split SHA-256: d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4.
- Aggregate comparison against Platinmods reports 2,876 identical shared paths and 205 different shared paths in the current report. Byte differences do not by themselves explain what changed semantically.
- ARM64 libil2cpp.so and global-metadata.dat are byte-identical between the two package variants. AndroidManifest.xml and the three DEX files differ by bytes. APKPure has no exact libplatinmods.so path; the comparison remains informational rather than a recipe to copy its components.
- APKTool successfully decodes the primary APK (exit code 0). JADX reports 96 decompilation errors with partial source output (exit code 3). This is a code-analysis limitation, not an inner ZIP CRC failure.
- **Source integrity is now PASS.** Do not ask for another upload based on the obsolete corruption findings. Final build remains blocked by incomplete call-flow validation, no approved feature scope, and absence of a genuine APKPure-based patch/build pipeline.

## Android entry-point trace (static; current APKPure V11.1.0)

- The decoded base manifest identifies jp.konami.duellinks.plugins.YgomMainActivity as the exported main Activity. The decompiled class is 581 lines and extends com.google.firebase.MessagingUnityPlayerActivity, implementing BillingClientStateListener and PurchasesUpdatedListener.
- YgomMainActivity.onCreate(Bundle) sets a fullscreen no-action-bar theme, calls super.onCreate, initializes a Logger, reads the launching Intent, reports re-engagement data and updates URI state. onResume/onPause delegate to the Unity Activity superclass; onDestroy shuts down the billing client; onNewIntent refreshes Intent/URI state.
- UnityPlayer.UnitySendMessage calls in this class are in purchase/billing callback flows (for example PurchaseBehaviour), not evidence of a mod-menu callback.
- The APKPure Java output contains zero com.platinmods classes, and its manifest does not declare android.permission.SYSTEM_ALERT_WINDOW or a Platinmods-style floating-menu service. The Activity trace shows no direct WindowManager-based overlay hook or addContentView call in the existing class.
- Evidence: [APK_CODE_ANALYSIS.md](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/APK_CODE_ANALYSIS.md); integration decision record: [MOD_INTEGRATION_PLAN.md](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/MOD_INTEGRATION_PLAN.md).
- **Interpretation:** the current APKPure base has no ready-made Android floating menu integration to enable. An independently implemented same-Activity menu is a candidate, not a proven solution; it must be patched into the actual game and runtime-tested. No gameplay feature is proven by this Activity trace.

## Historical Platinmods V11.0.0 evidence (reference only)

- Decoded package name: jp.konami.duellinks.
- Unity/IL2CPP indicators, three DEX files and 20 native libraries were inventoried.
- Decompiled com/platinmods/FloatingModMenuService.java contains generic menu-control construction and callbacks.
- com/platinmods/Preferences.java uses native Changes(...) callbacks and SharedPreferences-based preference loading/saving.
- com/platinmods/PMLauncher.java loads the platinmods native library.
- Strings in global-metadata.dat include ShowMonster/showMonster, CHEATCARD, PROCESS_DAMAGE variants; libduel.so includes DLL_DuelGetDamageValue and DLL_DuelComCheatCard.
- This is V11.0.0 evidence from Platinmods, not confirmation of a V11.1.0 APKPure feature.

## Candidate register

| Candidate | Current feasibility | Evidence | Next validation | Boundary |
|---|---|---|---|---|
| Custom CHATGPT MOD floating menu | High for UI concept; integration risk high/unknown | APKPure lacks the exact Platinmods libplatinmods.so path; old reference has a generic menu architecture, but its implementation is not part of APKPure | Trace the clean manifest and YgomMainActivity DEX lifecycle; determine whether an owned menu can attach cleanly without importing Platinmods code | Own implementation on APKPure base; do not copy Platinmods binary components blindly |
| Menu drag/minimize/restore, size, opacity and theme | High for UI behavior; not yet integrated | Standard Android UI concept; no runtime test yet | Implement an isolated menu layer and verify window/lifecycle behavior on target Android versions | Local presentation/accessibility only |
| Toggle, slider, dropdown, text input | High for UI controls; no game action proven | Generic controls appeared in historical Platinmods V11.0.0 code | Create owned controls, persistence and state tests; map gameplay callback separately if one is approved | A visible toggle does not imply an active gameplay feature |
| Persist own menu settings | High | Android preference storage is a straightforward independent design; historical reference used SharedPreferences | Define namespace, defaults, reset and migration tests | Keep CHATGPT MOD preferences independent |
| Show Monster & Status Details | Low/medium, unconfirmed | Il2CppDumper produced `ShowMonster(bool immediate, bool showAura, Action onFinished)` and a `Task3DCardMove.showMonster` field. Neither proves a status-reading feature or a mod callback. | Confirm enclosing type, call sites and input data in the now CRC-clean source, then determine whether this is only animation/render state. | Local rendering only; no hidden-opponent-information feature |
| Card-face inspection API | Unknown; no reveal feature approved | `dump.cs` contains `GetFieldCardFace(int player, int position, int index)`, `GetCardFace(...)`, and `DLL_DuelGetCardFace(...)`. This shows query APIs exist, not that hidden faces can be accessed in an online state. | Establish the enclosing types, callers, state/visibility semantics and behavior on a clean package. | Do not expose hidden opponent information in online duels |
| AutoPlay Bot | Unknown; built-in controls found, mod feasibility unproven | `DuelMenu` metadata includes `GetAutoPlay`, `SetAutoPlay(bool)`, `ChangeAutoPlay`, `autoPlayEnable` and `fastAutoEnable`; `DuelClient` metadata includes autoplay-related state. No third-party mod callback was found in APKPure. | Establish intended game mode, enclosing types, callers and whether these controls are normal game behavior; test only a permitted isolated mode. | No automation that abuses online matches or bypasses fair-play controls |
| FPS/performance/display/accessibility settings | Low/medium, unverified | ARM64 Unity libraries exist; no candidate setter/callback confirmed | Inspect manifest/config and IL2CPP dump, then test controlled settings in a sandbox | Prefer display/accessibility or stability improvements |
| Offline damage-rule simulator | High as a separate test utility | Can be implemented independently of proprietary game internals | Define deterministic test vectors and verify with unit tests | Offline sandbox only; not a live-game patch |
| Damage inspection / Cheat Card symbols | Read-only damage inspection is a research candidate; live manipulation is excluded | `dump.cs` shows `DLL_DuelGetDamageValue(int)`, `PVP_DuelGetDamageValue(int)`, source/destination-position getters and `PvP.Command.CHEATCARD = 9`. The relevant ARM64 package now passes CRC checks, but these signatures still do not reveal writable hooks or runtime semantics. | Trace getter call sites and data semantics for local display only. Test calculations separately in an offline model. | No live-duel damage manipulation; no unfair outcome changes |

## Additional IL2CPP observations (static only)

- Metadata version 31 and IL2CPP version 31 were read. Il2CppDumper generated `dump.cs`, `script.json`, and `stringliteral.json`, then exited with `-6` at its final `Console.ReadKey` prompt because standard input was redirected. The dump outputs exist, but the run is not a clean tool exit.
- `PvP.Command.CHEATCARD = 9` is an enum value, not evidence that a cheat-card operation works or can be triggered.
- `IDS_CARD.PROCESS_DAMAGE` and variants 1–3 are enum constants, not proof of a damage modification hook.
- `DLL_DuelGetDamageValue` is a getter declaration; no writable damage multiplier was identified by this pass.
- The refreshed APKPure package passed container digest, both embedded APK outer CRCs, and both inner ZIP CRC/decompression scans. Conclusions remain provisional because the metadata dump does not show full call flow or prove runtime behavior.

## Feature priority recommendation

1. **First:** map the Activity/DEX entry point and document an APKPure-only integration strategy for an independent CHATGPT MOD UI. No actual overlay is integrated yet.
2. **Second:** prototype and test menu UI/preferences independently, then integrate only through a reviewed patch path that preserves the original game package.
3. **Third:** investigate any game-information/display helper only after its type, callers, data semantics and permitted mode have been established.
4. **Separate optional work:** offline damage/card-rule simulator with unit tests.

## Evidence required before feature approval

1. Exact input Release, asset names, container and inner APK SHA-256, CRC results and package/split structure.
2. Exact class, method, resource, native symbol or IL2CPP reference with surrounding context.
3. Clear separation of verified facts, hypotheses and unknown behavior.
4. Compatibility, crash, ABI, split/OBB and signer/update impact.
5. Reproducible isolated test for anything claimed to work.
6. User approval of the bounded safe scope before implementation.

## Current decision

The refreshed APKPure source passes container and inner-package integrity checks, so source corruption is no longer the blocker. Final packaging remains blocked because reverse engineering is partial, no bounded feature scope has been approved, XAPK/split install strategy and signing compatibility are unresolved, and a genuine APKPure-based patch/build tool does not yet exist. Do not treat any candidate as a working cheat based only on names or strings.

## Build approval checkpoint

**Build approval: PENDING_REVERSE_ENGINEERING**

No feature scope is approved for final APK packaging yet. The build workflow requires the exact marker Build approval: APPROVED_FOR_IMPLEMENTATION before it can proceed.
