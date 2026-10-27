# CHATGPT MOD — APKPure Integration Plan

**Date:** 2026-10-27  
**Mod base:** APKPure Original V11.1.0 — Release tag APKPure_Latest  
**Comparison reference only:** Platinmods V11.1.0 — Release tag Latest  
**Status:** STATIC_ENTRYPOINT_MAPPED; RUNTIME_INTEGRATION_NOT_TESTED  
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
- The APKPure primary DEX output contains no com.platinmods package classes. The manifest/component inventory does not declare a Platinmods-style floating menu service or android.permission.SYSTEM_ALERT_WINDOW. The Activity trace does not show a current WindowManager-based menu hook or addContentView call.
- Interpretation: APKPure has no ready-made Platinmods floating menu integration that can simply be enabled. This does not prove a menu is impossible; it means an independently implemented and reviewed integration path is needed.

## 3. Proposed safe first scope — not yet approved
A bounded first milestone would be presentation and local preferences only:
1. An owned CHATGPT MOD menu launcher and panel, with open/close and a small set of visual controls.
2. Drag/minimize/restore behavior, size/opacity/theme controls only if these can be tested without disrupting Unity touch input.
3. Independent SharedPreferences namespace, sensible defaults and reset action.
4. No buttons represented as working gameplay cheats until a verified call path exists. No hidden-opponent-card access or online-duel outcome manipulation.

## 4. Integration options and decision criteria
### Option A — attach an owned Android View to the existing Activity
- Candidate injection point: immediately after super.onCreate(bundle) in YgomMainActivity, then attach a small view through the Activity's current window/view hierarchy.
- Advantages: uses the existing package/activity; a same-window view may avoid SYSTEM_ALERT_WINDOW special permission; Java UI and preference storage are straightforward.
- Risks: Unity fullscreen rendering/input may affect z-order, pointer handling, lifecycle, orientation and safe areas. No working runtime proof exists.
- Needed proof: compile a unique helper class into DEX, inject only the agreed call, rebuild and sign a test APK, then verify launch/crash, touch pass-through, drag behavior, pause/resume and persistence on a test device.

### Option B — Unity/IL2CPP-side UI
- Would integrate more naturally with the Unity render/input loop, but it requires locating the relevant Unity-side UI construction path and a safe native/IL2CPP injection technique. Static method names alone do not provide that path.
- Do not select this option until a concrete entry point and reproducible test are documented.

### Current recommendation
Evaluate Option A first because the Android Activity entry point and lifecycle are now identified. Treat it only as a hypothesis until a genuine APKPure-based patcher and device test establish that it works. Do not import Platinmods service or native-library binaries.

## 5. APK format and signing are still unresolved
The source is an XAPK with a base APK plus an ARM64 config split. The primary APK has no native library entries; the split contains the nine native libraries. A future single-APK output may require merging the split's required native libraries into the rebuilt primary APK, or the release artifact may need to remain an installable split set. Neither strategy has been implemented or validated; do not assume that extracting or merging the files creates an installable APK.

The rebuilt artifact will require a valid signature. Without the private key used for an installed Platinmods APK or an applicable signing-certificate rotation chain, overwriting that installation cannot be promised. A separate uninstall/reinstall might be necessary and could affect local app data.

## 6. Required before implementation/build
1. Review and explicitly approve the bounded feature scope in MOD_CANDIDATES.md.
2. Implement a real APKPure-only patch/build tool: preserve the main/split relationship, add only owned code, rebuild, align, sign and verify the exact output APK.
3. Record the injected class/method and patch diff; add automated checks that reject Platinmods components/binaries as build inputs.
4. Test on a dedicated device/emulator: install, first launch, crash/logcat, Activity lifecycle, touch input, display scaling, preference persistence, update/uninstall implications.
5. Record artifact size, SHA-256, package/version, signer certificate, install result and actual UI behavior.

## 7. Current gates
- Source integrity: PASS.
- Static Activity entry-point discovery: PASS, limited to recovered DEX source.
- Full reverse engineering: PARTIAL (JADX reports 96 errors; IL2CPP dumper generates outputs but has a post-output Console.ReadKey exception).
- Working mod menu: NOT IMPLEMENTED / NOT TESTED.
- Game-feature callbacks: NOT PROVEN.
- APKPure-based patcher and single-APK/split strategy: NOT IMPLEMENTED.
- Final build approval: PENDING_REVERSE_ENGINEERING.
