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

- APKPure Release asset is an XAPK (92,726,986 bytes). Its computed container SHA-256 matches GitHub's metadata.
- The XAPK contains jp.konami.duellinks.apk (55,854,706 bytes) and config.arm64_v8a.apk (36,869,159 bytes), and no OBB member was detected.
- Both embedded APK members fail their outer-container CRC check.
- The primary APK has three DEX files and 3,368 central-directory entries, but its compressed asset at assets/bin/Data/e1f73dc34613ec042897cc46749d448c fails decompression with “invalid literal/length code”.
- The ARM64 config split contains nine native libraries. Its lib/arm64-v8a/libduel.so fails its ZIP CRC check; findings depending on this library remain unverified.
- Aggregate comparison against Platinmods reports 2,874 identical readable paths, 205 different readable shared paths, 296 APKPure-only paths, 317 Platinmods-only paths, and two shared paths with unreadable APKPure content.
- ARM64 libil2cpp.so and global-metadata.dat are byte-identical in both packages. AndroidManifest.xml and the three DEX files differ by bytes; that does not establish what the changes mean.
- Platinmods includes libplatinmods.so in both ARM64 and ARMv7 libraries; those exact paths are absent from the APKPure package inventory. The current APKPure config split contains ARM64 libraries only.
- Apktool fails while copying the corrupted primary asset. JADX generates partial source and reports 96 decompilation errors. A pinned IL2CPP metadata-recovery stage has been added; read IL2CPP_ANALYSIS_REPORT.md after the current workflow finishes.
- **Hard blocker:** the current APKPure package is not clean enough for patch/build. Replace it with a clean original XAPK, then repeat the analysis. A matching outer checksum only proves the file matches the uploaded Release asset; it does not make its internal contents valid.

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
| Custom CHATGPT MOD floating menu | High for UI concept; integration risk high/unknown | APKPure lacks the exact Platinmods libplatinmods.so path; old reference has a generic menu architecture, but its implementation is not part of APKPure | After clean reupload, inspect manifest components and DEX entry points; design an independent overlay/service integration and test lifecycle | Own implementation on APKPure base; do not copy Platinmods binary components blindly |
| Menu drag/minimize/restore, size, opacity and theme | High for UI behavior; not yet integrated | Standard Android UI concept; no runtime test yet | Implement an isolated menu layer and verify window/lifecycle behavior on target Android versions | Local presentation/accessibility only |
| Toggle, slider, dropdown, text input | High for UI controls; no game action proven | Generic controls appeared in historical Platinmods V11.0.0 code | Create owned controls, persistence and state tests; map gameplay callback separately if one is approved | A visible toggle does not imply an active gameplay feature |
| Persist own menu settings | High | Android preference storage is a straightforward independent design; historical reference used SharedPreferences | Define namespace, defaults, reset and migration tests | Keep CHATGPT MOD preferences independent |
| Show Monster & Status Details | Low/medium, unconfirmed | ShowMonster/showMonster strings appear in APKPure global-metadata.dat; main metadata is byte-identical to reference | Use Il2CppDumper output and clean native assets to identify a real method/type path and the data source | Only local-client-visible information; no hidden-opponent-information feature |
| Reveal Card Face | Unknown | No verified APKPure callback or valid data path | Search clean DEX/native metadata and prove the relevant display/data path | Do not expose hidden opponent information in online duels |
| AutoPlay Bot | Unknown | No implementation found in current reports; historical label was only a reference clue | Search APKPure DEX/resources and establish context before judging feasibility | No automation that abuses online matches or bypasses fair-play controls |
| FPS/performance/display/accessibility settings | Low/medium, unverified | ARM64 Unity libraries exist; no candidate setter/callback confirmed | Inspect manifest/config and IL2CPP dump, then test controlled settings in a sandbox | Prefer display/accessibility or stability improvements |
| Offline damage-rule simulator | High as a separate test utility | Can be implemented independently of proprietary game internals | Define deterministic test vectors and verify with unit tests | Offline sandbox only; not a live-game patch |
| Damage multiplier or Cheat Card in live online duels | Not an implementation target | The relevant ARM64 libduel.so is corrupt in the source upload; strings alone prove no behavior | No live-match outcome implementation; use an offline model for rule exploration | Excluded because it unfairly changes competitive results |

## Feature priority recommendation

1. **First:** independent CHATGPT MOD menu shell, visual settings and preference persistence. This provides a usable foundation without claiming game toggles work.
2. **Second:** after a clean source package is available, inspect app manifest/window lifecycle and test menu integration plus installation integrity.
3. **Third:** only then decide whether any game-information or display helper can be implemented, based on the IL2CPP dump and reliable native binaries.
4. **Separate optional work:** offline damage/card-rule simulator with unit tests.

## Evidence required before feature approval

1. Exact input Release, asset names, container and inner APK SHA-256, CRC results and package/split structure.
2. Exact class, method, resource, native symbol or IL2CPP reference with surrounding context.
3. Clear separation of verified facts, hypotheses and unknown behavior.
4. Compatibility, crash, ABI, split/OBB and signer/update impact.
5. Reproducible isolated test for anything claimed to work.
6. User approval of the bounded safe scope before implementation.

## Current decision

Build remains blocked by source integrity. Do not start final packaging or call any gameplay feature possible until a clean APKPure package has been analyzed and the implementation path is supported by evidence.

## Build approval checkpoint

**Build approval: PENDING_REVERSE_ENGINEERING**

No feature scope is approved for final APK packaging yet. The build workflow requires the exact marker Build approval: APPROVED_FOR_IMPLEMENTATION before it can proceed.
