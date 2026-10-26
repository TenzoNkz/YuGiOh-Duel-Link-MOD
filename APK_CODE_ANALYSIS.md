# APK Code Analysis Report

**Generated:** 2026-10-26 05:28:12 UTC
**Method:** JADX/Apktool static analysis; the APK was not installed or executed.
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Requested release tag: Platinmods_V11.0.0
- JADX pinned version: 1.5.6
- Apktool pinned version: 3.0.3

## Source Release and integrity
- Release page: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Release tag: Platinmods_V11.0.0
- APK asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- GitHub-reported size: 127424878 bytes
- Downloaded size: 127424878 bytes
- Expected SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Calculated SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb
- Digest comparison: PASS

**Status:** CODE_ANALYSIS_PARTIAL

## Android manifest (decoded by Apktool)
- Package name: jp.konami.duellinks
- Version name: not declared
- Version code: not declared
- minSdkVersion: not declared
- targetSdkVersion: not declared

## Tool execution
- Apktool exit code: 0
- JADX exit code: 3
- JADX-reported decompiler error count: 96
- Decompiled Java source files found: 8194
- Decoded Apktool output entries: 18765

### Apktool output excerpt
    I: Using Apktool 3.0.3 on source.apk with 4 threads
    I: Baksmaling classes2.dex...
    I: Baksmaling classes.dex...
    I: Baksmaling classes3.dex...
    I: Loading resource table...
    I: Decoding value resources...
    I: Loading resource table from file: /home/runner/.local/share/apktool/framework/1.apk
    I: Decoding file resources...
    I: Generating values XMLs...
    I: Decoding AndroidManifest.xml with resources...
    I: Copying original files...
    I: Copying assets...
    I: Copying lib...
    I: Copying unknown files...

### JADX output excerpt
    INFO  - progress: 6678 of 8893 (75%)
    INFO  - progress: 6872 of 8893 (77%)
    INFO  - progress: 7046 of 8893 (79%)
    INFO  - progress: 7098 of 8893 (79%)
    INFO  - progress: 7209 of 8893 (81%)
    INFO  - progress: 7288 of 8893 (81%)
    INFO  - progress: 7385 of 8893 (83%)
    INFO  - progress: 7469 of 8893 (83%)
    INFO  - progress: 7559 of 8893 (84%)
    INFO  - progress: 7769 of 8893 (87%)
    INFO  - progress: 7846 of 8893 (88%)
    INFO  - progress: 8001 of 8893 (89%)
    INFO  - progress: 8143 of 8893 (91%)
    INFO  - progress: 8269 of 8893 (92%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8625 of 8893 (96%)
                                                                 
    ERROR - finished with errors, count: 96

## Selected native/IL2CPP inventory
- assets/bin/Data/Managed/Metadata/global-metadata.dat: 11182904 bytes
- lib/arm64-v8a/libduel.so: 22185664 bytes
- lib/arm64-v8a/libil2cpp.so: 64327320 bytes
- lib/arm64-v8a/libplatinmods.so: 9289224 bytes
- lib/armeabi-v7a/libduel.so: 18973460 bytes
- lib/armeabi-v7a/libil2cpp.so: 54624932 bytes
- lib/armeabi-v7a/libplatinmods.so: 8744976 bytes

## Search hits in decompiled Java
- Matching lines found: 31; displaying up to 31.
- androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:57: return new StaticLayout(charSequence, textPaint, i, alignment, textView.getLineSpacingMultiplier(), textView.getLineSpacingExtra(), textView.getIncludeFontPadding());
- androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:80: StaticLayout.Builder hyphenationFrequency = builderObtain.setAlignment(alignment).setLineSpacing(textView.getLineSpacingExtra(), textView.getLineSpacingMultiplier()).setIncludePad(textView.getInclu...
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:20: private static final float SHADOW_MULTIPLIER = 1.5f;
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:60: float f = this.mRawMaxShadowSize * SHADOW_MULTIPLIER;
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:104: return z ? (float) (((double) (f * SHADOW_MULTIPLIER)) + ((1.0d - COS_45) * ((double) f2))) : f * SHADOW_MULTIPLIER;
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:175: this.mShadowSize = (int) ((even * SHADOW_MULTIPLIER) + this.mInsetShadow + 0.5f);
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:215: return (Math.max(f, this.mCornerRadius + this.mInsetShadow + ((f * SHADOW_MULTIPLIER) / 2.0f)) * 2.0f) + (((this.mRawMaxShadowSize * SHADOW_MULTIPLIER) + this.mInsetShadow) * 2.0f);
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:24: private int dimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:26: private int oppositeDimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:59: this.dimensionMultiplier = i;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:72: this.offset = this.dimensionMultiplier;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:75: this.oppositeOffset = this.oppositeDimensionMultiplier;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:86: this.dimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:88: this.oppositeDimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:119: this.offset = this.dimensionMultiplier * this.dimension.value;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:127: this.oppositeOffset = this.oppositeDimensionMultiplier * this.oppositeDimension.value;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:248: this.oppositeDimensionMultiplier = i;
- com/adjust/sdk/BackoffStrategy.java:12: long milliSecondMultiplier;
- com/adjust/sdk/BackoffStrategy.java:18: this.milliSecondMultiplier = j;
- com/adjust/sdk/Util.java:337: return (long) (Math.min(((long) Math.pow(2.0d, i - backoffStrategy.minRetries)) * backoffStrategy.milliSecondMultiplier, backoffStrategy.maxWait) * randomInRange(backoffStrategy.minRange, backoffSt...
- com/google/common/base/CharMatcher.java:904: static final int MULTIPLIER = 1682554634;
- com/google/common/base/CharMatcher.java:915: return TABLE.charAt((MULTIPLIER * c) >>> SHIFT) == c;
- com/google/common/escape/CharEscaper.java:9: private static final int DEST_PAD_MULTIPLIER = 2;
- jp/applilink/sdk/common/ApplilinkVideoViewActivity.java:33: final boolean booleanExtra = intent.getBooleanExtra("autoPlay", false);
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:73: protected boolean _autoPlay;
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:470: this._autoPlay = false;
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:535: this._autoPlay = z;
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:916: if (this._autoPlay) {
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:1161: if (str2 == null || str2.length() <= 1 || this._autoPlay) {
- jp/applilink/sdk/recommend/RecommendNetworkCore.java:1098: intent.putExtra("autoPlay", z);
- kotlin/collections/builders/MapBuilder.java:534: throw new IllegalStateException("This cannot happen with fixed magic multiplier and grow-only hash array. Have object hashCodes changed?");

## Key Platinmods menu-framework source references
- Matching source lines found: 904; displaying context for up to 56 lines.
- com/platinmods/FloatingModMenuService.java:1: package com.platinmods;
- com/platinmods/FloatingModMenuService.java:2: 
- com/platinmods/FloatingModMenuService.java:3: import android.R;
- com/platinmods/FloatingModMenuService.java:4: import android.animation.ArgbEvaluator;
- com/platinmods/FloatingModMenuService.java:5: import android.animation.TimeAnimator;
- com/platinmods/FloatingModMenuService.java:6: import android.animation.ValueAnimator;
- com/platinmods/FloatingModMenuService.java:7: import android.app.ActivityManager;
- com/platinmods/FloatingModMenuService.java:8: import android.app.AlertDialog;
- com/platinmods/FloatingModMenuService.java:9: import android.app.Service;
- com/platinmods/FloatingModMenuService.java:10: import android.content.Intent;
- com/platinmods/FloatingModMenuService.java:11: import android.content.res.ColorStateList;
- com/platinmods/FloatingModMenuService.java:12: import android.graphics.BitmapFactory;
- com/platinmods/FloatingModMenuService.java:13: import android.graphics.Color;
- com/platinmods/FloatingModMenuService.java:14: import android.graphics.PorterDuff;
- com/platinmods/FloatingModMenuService.java:15: import android.graphics.Typeface;
- com/platinmods/FloatingModMenuService.java:16: import android.graphics.drawable.GradientDrawable;
- com/platinmods/FloatingModMenuService.java:17: import android.net.Uri;
- com/platinmods/FloatingModMenuService.java:18: import android.os.Build;
- com/platinmods/FloatingModMenuService.java:19: import android.os.Handler;
- com/platinmods/FloatingModMenuService.java:20: import android.os.IBinder;
- com/platinmods/FloatingModMenuService.java:21: import android.text.Html;
- com/platinmods/FloatingModMenuService.java:22: import android.text.InputFilter;
- com/platinmods/FloatingModMenuService.java:23: import android.text.TextUtils;
- com/platinmods/FloatingModMenuService.java:24: import android.text.method.DigitsKeyListener;
- com/platinmods/FloatingModMenuService.java:25: import android.util.Base64;
- com/platinmods/FloatingModMenuService.java: displayed 25 selected lines; 877 cumulative source matches scanned so far.
- com/platinmods/PMLauncher.java:67: private static native void initialize(Context context);
- com/platinmods/PMLauncher.java:70: System.loadLibrary("platinmods");
- com/platinmods/PMLauncher.java: displayed 2 selected lines; 879 cumulative source matches scanned so far.
- com/platinmods/Preferences.java:4: import android.content.SharedPreferences;
- com/platinmods/Preferences.java:11: private static SharedPreferences.Editor editor;
- com/platinmods/Preferences.java:12: public static boolean savePref = false;
- com/platinmods/Preferences.java:16: public static native void Changes(Context context2, int i, int i2, boolean z, String str);
- com/platinmods/Preferences.java:18: public static void changeFeatureBoolean(String str, int i, boolean z) {
- com/platinmods/Preferences.java:26: savePref = z;
- com/platinmods/Preferences.java:28: Changes(context, i, 0, z, str);
- com/platinmods/Preferences.java:29: SharedPreferences.Editor editorEdit = PreferenceManager.getDefaultSharedPreferences(context).edit();
- com/platinmods/Preferences.java:34: public static void changeFeatureInt(String str, int i, int i2) {
- com/platinmods/Preferences.java:35: Changes(context, i, i2, false, str);
- com/platinmods/Preferences.java:36: SharedPreferences.Editor editorEdit = PreferenceManager.getDefaultSharedPreferences(context).edit();
- com/platinmods/Preferences.java:41: public static boolean loadPrefBoolean(String str, int i) {
- com/platinmods/Preferences.java:43: SharedPreferences defaultSharedPreferences = PreferenceManager.getDefaultSharedPreferences(context);
- com/platinmods/Preferences.java:45: savePref = defaultSharedPreferences.getBoolean(String.valueOf(i), false);
- com/platinmods/Preferences.java:47: if (!savePref && i > 0) {
- com/platinmods/Preferences.java:50: boolean z = defaultSharedPreferences.getBoolean(String.valueOf(i), false);
- com/platinmods/Preferences.java:51: Changes(context, i, 0, z, str);
- com/platinmods/Preferences.java:58: public static int loadPrefInt(String str, int i) {
- com/platinmods/Preferences.java:60: if (savePref) {
- com/platinmods/Preferences.java:61: int i2 = PreferenceManager.getDefaultSharedPreferences(context).getInt(String.valueOf(i), 0);
- com/platinmods/Preferences.java:62: Changes(context, i, i2, false, str);
- com/platinmods/Preferences.java: displayed 21 selected lines; 900 cumulative source matches scanned so far.
- com/platinmods/MainActivity.java:10: public static void CallToast(final Context context) {
- com/platinmods/MainActivity.java:14: MainActivity.Toast(context);
- com/platinmods/MainActivity.java:23: context.startService(new Intent(context, (Class<?>) FloatingModMenuService.class));
- com/platinmods/MainActivity.java:28: public static native void Toast(Context context);
- com/platinmods/MainActivity.java: displayed 4 selected lines; 904 cumulative source matches scanned so far.

## Search hits in decoded resources
- Matching lines found: 0; displaying up to 0.
- No matching term was found in the scanned decoded resource XML/text.

## Focused strings: feature labels, menu callbacks, and duel damage
- Focused string matches found: 21.
### assets/bin/Data/Managed/Metadata/global-metadata.dat
- URORAIDS_CARD.PROCESS_BLAZEIDS_CARD.PROCESS_CRYSTALIDS_CARD.PROCESS_DAMAGEIDS_CARD.PROCESS_DARKNESSIDS_CARD.PROCESS_FULLSTARLIGHTIDS_C
- CHEATCARD
- PROCESS_DAMAGE
- PROCESS_DAMAGE1
- PROCESS_DAMAGE2
- PROCESS_DAMAGE3
- DLL_DuelGetDamageValue
- ShowMonster
- showMonster
### lib/arm64-v8a/libduel.so
- DLL_DuelGetDamageValue
- DLL_DuelComCheatCard
### lib/arm64-v8a/libil2cpp.so
- DLL_DuelGetDamageValue
### lib/arm64-v8a/libplatinmods.so
- Java_com_platinmods_FloatingModMenuService_settingsList
- Java_com_platinmods_FloatingModMenuService_getFeatureList
- Java_com_platinmods_Preferences_Changes
### lib/armeabi-v7a/libduel.so
- DLL_DuelGetDamageValue
- DLL_DuelComCheatCard
### lib/armeabi-v7a/libil2cpp.so
- DLL_DuelGetDamageValue
### lib/armeabi-v7a/libplatinmods.so
- Java_com_platinmods_FloatingModMenuService_settingsList
- Java_com_platinmods_FloatingModMenuService_getFeatureList
- Java_com_platinmods_Preferences_Changes

## Search hits in selected native/IL2CPP strings
- Total matching printable strings: 284.
### assets/bin/Data/Managed/Metadata/global-metadata.dat
- )$WhiteIn$WhiteIn_1$WhiteOut$WhiteOut_1$__BindingManager--ClearAllBindings%% #% #-% -#%#%#-%)%-#%20%26%2C%3D%a%backspace%bannerid%%basepath%%c%d%down%f%left%right%s%subloop%%subloop0%%subloop00%%subloop000%%subloop000...
- -END-HERO-Infinity-_.!~*'()-bar-buildsrc-container-handle-image-inf-infinity-item-label-underline-unity-background-image-tint-color-unity-background-scale-mode-unity-editor-text-rendering-mode-unity-font-unity-font-de...
- AssignmentCharacter_001AssignmentCharacter_002AssignmentCharacter_003Async: AsyncGPUReadback cannot use Temp memory as input since the result may only become available at an unspecified point in the future.AsyncMiniJS...
- : Common Language Runtime detected an invalid program.CompareInfoCompareInfo - CompareOption.Ordinal cannot be used with other options.ComparerCompiler error: Generated a subpass pass but no pass is currently active.C...
- : Draw.01DrawMeshInstanced is not supported.DrawMeshInstancedProcedural is not supported.DrawReactionIsDoneDrawingDeckDropdown (Legacy)Dropdown ListDropdown.valueDuckEndDuckStartDuckVolDuckingCategoryDue time too larg...
- : Guid should contain 32 digits with 4 dashes (xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx).Guid string should only contain hexadecimal characters.GuideCharaWidgetGuideLineHH:mmHBoxHDR Mode Change RequestedHDR Output ActiveH...
- : OpaqueOpenOpenBannerOpenFloorOpenPackRootOpenPanelOpenRecommendListResultOpenRentalDeckOpenRewardListResultOpenUrlOpenedPacksOpenedPacks.dialogOpenedPacks.packOpenedPacks.packSROpenedPacks.packUROpenedPacks.recommen...
- sTwoPaneSplitView needs exactly 2 children.TypeType Type 'Type '{0}' in Assembly '{1}' is not marked as serializable.Type '{0}' of type '{1}' does not derive from System.ObjectType `Type and assembly attributes cannot...
- ]\\"\((?<v>[^\(]*?)\)\.[^\.]*$\<\>\A[a-zA-Z0-9-._~]{1,100}\Z\[[0-9]+\]\\\\[\b\f\n\r\t\u\x{0:X2}\{0:D3}\{0:D}]] ] First character index: ] Last character index: ] MaxRange: '] Property=[] Units Per EM set to ] and Igno...
- {2}error_codeertacardnameeses-ESescapeetetc_tabetexteueuc-cneuc-jpeuc-krev0002_charagetev0002_opev0002_pegasuslv50ev0004_charagetev0004_zorcev0007_paradoxbrothers_lv50ev0014_maliklv50ev01ev02ev03ev_idev_noevaluateeval...
- {76}: {77}{0}: {1} precompiled chunk{0}: {1}, {2}: {3}{0}: {1}, {2}: {3}, {4}: {5}, {6}: {7}{0}: {1}/{2}{0}:{1}{0}:{1}: {0}:{1}: {2}{0}<{1}>{0}L/{1:D4}{0}_mrk{1:D6}{0}_rank_{1:D2}{0}_{1}{0}_{1}_{2}{0}_{1}x{2}{0}f{0}fl...
- CHEATCARD
- autoPlay
- CutinDamage
- DamageVoiceTable
- PROCESS_DAMAGE
- PROCESS_DAMAGE1
- PROCESS_DAMAGE2
- PROCESS_DAMAGE3
- DAMAGELP
### lib/arm64-v8a/libduel.so
- DLL_DuelGetDamageSrcPosition
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageValue
- DLL_DuelComCheatCard
### lib/arm64-v8a/libil2cpp.so
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageSrcPosition
- UnityEngine.Rendering.CommandBuffer::SetInstanceMultiplier_Injected(System.IntPtr,System.UInt32)
- DLL_DuelGetDamageValue
- UnityEngine.ParticleSystem/MainModule::get_startDelayMultiplier()
- UnityEngine.ParticleSystem/MainModule::get_startLifetimeMultiplier()
- UnityEngine.ParticleSystem/MainModule::set_startDelayMultiplier(System.Single)
### lib/arm64-v8a/libplatinmods.so
- Java_com_platinmods_FloatingModMenuService_isGameLibLoaded
- Java_com_platinmods_FloatingModMenuService_Title
- Java_com_platinmods_FloatingModMenuService_Heading
- Java_com_platinmods_FloatingModMenuService_Icon
- Java_com_platinmods_FloatingModMenuService_IconWebViewData
- Java_com_platinmods_FloatingModMenuService_settingsList
- Java_com_platinmods_MainActivity_Toast
- Java_com_platinmods_FloatingModMenuService_getFeatureList
- Java_com_platinmods_Preferences_Changes
### lib/armeabi-v7a/libduel.so
- DLL_DuelGetDamageSrcPosition
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageValue
- DLL_DuelComCheatCard
### lib/armeabi-v7a/libil2cpp.so
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageSrcPosition
- UnityEngine.Rendering.CommandBuffer::SetInstanceMultiplier_Injected(System.IntPtr,System.UInt32)
- DLL_DuelGetDamageValue
- UnityEngine.ParticleSystem/MainModule::get_startDelayMultiplier()
- UnityEngine.ParticleSystem/MainModule::get_startLifetimeMultiplier()
- UnityEngine.ParticleSystem/MainModule::set_startDelayMultiplier(System.Single)
### lib/armeabi-v7a/libplatinmods.so
- Java_com_platinmods_FloatingModMenuService_isGameLibLoaded
- Java_com_platinmods_FloatingModMenuService_Title
- Java_com_platinmods_FloatingModMenuService_Heading
- Java_com_platinmods_FloatingModMenuService_Icon
- Java_com_platinmods_FloatingModMenuService_IconWebViewData
- Java_com_platinmods_FloatingModMenuService_settingsList
- Java_com_platinmods_MainActivity_Toast
- Java_com_platinmods_FloatingModMenuService_getFeatureList
- Java_com_platinmods_Preferences_Changes

## Interpretation guardrails
- Exact string hits locate potential code/resources; they do not prove event wiring, control flow, or that a menu toggle works.
- JADX primarily analyzes DEX/Java/Kotlin code. Unity IL2CPP game logic may be compiled into native libraries and metadata; full native tracing requires separate tooling and careful symbol/metadata analysis.
- Static decompilation does not prove server-authoritative behavior, online compatibility, or runtime success.
- The APK was not executed or installed. Temporary decompiled source was not committed to the repository.

## Recommended next step
Review the source/resource/native-string hits together with the decompiled manifest. Record exact file/class/method evidence for each feature in MOD_CANDIDATES.md, then separate code-reading hypotheses from any isolated test results.

