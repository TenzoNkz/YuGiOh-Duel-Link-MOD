# CHATGPT MOD — APKPure Integration Plan

**Date:** 2026-10-27  
**Mod base:** APKPure Original V11.1.0 — Release tag APKPure_Latest  
**Comparison reference only:** Platinmods V11.1.0 — Release tag Latest  
**Status:** UI_SOURCE_AND_PATCHER_IMPLEMENTED; APK_BUILD_AND_RUNTIME_NOT_TESTED  
**Build approval:** PENDING_REVERSE_ENGINEERING

## 1. Current APK input, verified
- XAPK SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb.
- Primary APK: jp.konami.duellinks.apk, 55,854,706 bytes, SHA-256 e2f38c25eb8d32c66f6b2a036cbe1eeb44164841f6cb684073d9f5ea1ac0c11d.
- ARM64 config split: config.arm64_v8a.apk, 36,869,159 bytes, SHA-256 d2bb8f75605e457b1680b2c428ba653840aed11ca49644d9ad5d10bd649dacf4.
- Container digest, both embedded-member outer CRCs and both inner APK CRC/decompression scans pass.
- The base APK contains three DEX files. The config split contains nine native libraries, including libduel.so and libil2cpp.so. No OBB member was found.
- Evidence: [APK code analysis / Activity entry-point trace](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/APK_CODE_ANALYSIS.md), [APK static inventory](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/blob/main/APP_ANALYSIS_REPORT.md).

## 2. Android entry point observed in the clean APK
The static decompiler report finds:
- Source: jp/konami/duellinks/plugins/YgomMainActivity.java (581 lines).
- Type: YgomMainActivity extends com.google.firebase.MessagingUnityPlayerActivity and implements BillingClientStateListener and PurchasesUpdatedListener.
- onCreate(Bundle) lines 85–93: sets a fullscreen no-action-bar theme, calls super.onCreate(bundle), initializes a logger, reads the launch Intent, reports re-engagement data and updates URI state.
- onResume() and onPause() delegate to super. onDestroy() calls super and tears down the billing client. onNewIntent() updates the Intent/URI and reports re-engagement.
- UnityPlayer.UnitySendMessage is used in billing/purchase callbacks to communicate with Unity objects such as PurchaseBehaviour. These are purchase bridge calls, not mod-menu callbacks.
- The APKPure primary DEX output contains no com.platinmods package classes. The manifest/component inventory does not declare a Platinmods-style floating menu service or android.permission.SYSTEM_ALERT_WINDOW. The Activity trace does not show an existing WindowManager-based menu hook or addContentView call.
- Interpretation: APKPure has no ready-made Platinmods floating menu integration that can simply be enabled. The menu must be independently implemented and attached through a reviewed integration path.

## 3. Implemented UI-only prototype source — not yet integrated into an APK
Owned source: src/mod_menu/com/chatgptmod/menu/ModMenu.java.
- Creates a CHATGPT MOD launcher and panel in the existing Activity content view.
- Supports opening/closing the panel, dragging the launcher within the Activity bounds, and remembering whether the panel should be open on the next launch.
- Uses its own SharedPreferences namespace, chatgpt_mod_local_ui.
- Contains no IL2CPP calls, native hooks or gameplay actions. The panel explicitly indicates that gameplay actions are not connected.
- Java source compiles to DEX and patcher tests (including full report preflight and approval-bypass regression) pass in [CHATGPT MOD Menu Source Validation](https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40457542823).
- Patcher primitives and Python unit tests passed in the same run. Checkpoint/record validation also passed at https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/actions/runs/40456595229.
- This validates source compilation and selected patcher logic only. No original APK has yet been rebuilt, signed, installed or runtime-tested with this UI.

## 4. Integration implementation and safety checks
The gated patch tool is in tools/build_chatgpt_mod.py. It is designed to:
1. Require Build approval: APPROVED_FOR_IMPLEMENTATION in MOD_CANDIDATES.md.
2. Download only the XAPK asset from APKPure_Latest, require a Release SHA-256 digest, and verify XAPK and embedded APK CRC/decompression integrity.
3. Decode the primary APK with pinned Apktool, confirm package jp.konami.duellinks, find the Activity onCreate(Bundle) smali method and inject one call immediately after the superclass onCreate call.
4. Compile the owned menu helper with javac/D8, merge validated ARM64 libraries from config split into the decoded primary package, rebuild, append the helper DEX, zipalign, sign with an explicitly provided key and verify APK signature/archive integrity.
5. Fail closed if the Activity method structure changes, DEX hook already exists, source hashes/CRCs fail, expected native libraries are missing, non-ARM64 ABI libraries appear, or required signing values are unavailable.

The source validation action and Python tests do not execute the full APK patch/build pipeline. That end-to-end step remains intentionally blocked by the pending user feature-scope approval and signing configuration.

## 5. Runtime integration hypothesis and criteria
### Option A — attach an owned Android View to the existing Activity
- Injection point: immediately after super.onCreate(bundle) in YgomMainActivity.
- Advantages: uses the existing package/activity; the same-window view may avoid the special SYSTEM_ALERT_WINDOW permission.
- Risks: Unity fullscreen rendering/input can affect z-order, pointer pass-through, lifecycle, orientation, safe areas and performance. These are unknown until the patched APK is run.
- Needed proof: launch the signed test APK, inspect logcat/crash state, verify bubble/panel display, touch passthrough outside the controls, drag bounds, Activity pause/resume, orientation behavior and preference persistence.

### Option B — Unity/IL2CPP-side UI
- Would integrate more naturally with the Unity render/input loop, but requires a concrete Unity-side UI construction path and a safe native/IL2CPP injection technique. Static method names do not provide that path.
- Do not select this option until a concrete entry point and reproducible test are documented.

### Current recommendation
Use the existing UI-only Java prototype and evaluate Option A first after scope approval. Do not import Platinmods service/native-library binaries. No gameplay feature is ready to connect merely because a method name was recovered.

## 6. APK format and signing
- The prototype patch tool merges the validated ARM64 native libraries from the config split into the decoded primary APK before rebuilding a single-APK test artifact. This has not been tested with a full APK rebuild or installation, so any unexpected split payload or library conflict must stop the process rather than be ignored.
- The resulting APK is ARM64-only, matching the available APKPure XAPK split; it should not be represented as a universal multi-ABI APK.
- The rebuilt artifact requires a valid signing key. The build workflow expects repository Actions secrets named MOD_SIGNING_KEYSTORE_B64, MOD_SIGNING_KEY_ALIAS, MOD_SIGNING_STORE_PASSWORD and MOD_SIGNING_KEY_PASSWORD. These values should never be committed to the repository.
- Without the private key used for an installed Platinmods APK or an applicable signing-certificate rotation chain, overwriting that installation cannot be promised. A separate uninstall/reinstall may be required and could affect local app data.

## 7. Required gates before an APK test build
1. Review and explicitly approve the bounded UI-only scope in MOD_CANDIDATES.md; keep game-action controls disabled.
2. Configure an explicitly controlled signing key through repository Actions secrets; never store private keys or passwords in Git.
3. Run the gated APKPure-based build workflow only after approval. A successful archive/build step is not proof of installability or runtime behavior.
4. Inspect the resulting package, DEX entries, merged libraries, package/version and signer certificate.
5. Install on a dedicated device/emulator and test first launch/crash logs, Activity lifecycle, Unity touch interaction, display scaling and preference persistence.
6. Record artifact size, SHA-256, signer, install result, test device/Android version, and observed UI behavior.

## 8. Current gates
- Source integrity: PASS.
- Static Activity entry-point discovery: PASS, based on recovered DEX source.
- UI-only helper Java -> DEX compilation: PASS in CI.
- Patcher primitive/unit tests and full report preflight gate: PASS in CI, including a regression that explanatory prose cannot satisfy the approval marker.
- End-to-end APKPure XAPK download/decode/inject/rebuild/align/sign: NOT RUN.
- Full reverse engineering: PARTIAL (JADX reports 96 errors; Il2CppDumper generates outputs but has a post-output Console.ReadKey exception).
- Integrated/running mod menu: NOT IMPLEMENTED IN APK / NOT TESTED.
- Game-feature callbacks: NOT PROVEN.
- The required standalone line `**Build approval: APPROVED_FOR_IMPLEMENTATION**` is parsed as a separate checkpoint line; the current marker remains `**Build approval: PENDING_REVERSE_ENGINEERING**`.
- Final build approval: PENDING_REVERSE_ENGINEERING.
