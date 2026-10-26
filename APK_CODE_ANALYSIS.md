# APK Code Analysis Report

**Generated:** 2026-10-26 05:16:59 UTC
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
- JADX-reported decompiler error count: 0
- Decompiled Java source files found: 8194
- Decoded Apktool output entries: 18765

### Apktool output excerpt
    I: Using Apktool 3.0.3 on source.apk with 4 threads
    I: Baksmaling classes.dex...
    I: Baksmaling classes2.dex...
    I: Loading resource table...
    I: Baksmaling classes3.dex...
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
    INFO  - progress: 6983 of 8893 (78%)
    INFO  - progress: 7090 of 8893 (79%)
    INFO  - progress: 7110 of 8893 (79%)
    INFO  - progress: 7242 of 8893 (81%)
    INFO  - progress: 7369 of 8893 (82%)
    INFO  - progress: 7529 of 8893 (84%)
    INFO  - progress: 7664 of 8893 (86%)
    INFO  - progress: 7771 of 8893 (87%)
    INFO  - progress: 7818 of 8893 (87%)
    INFO  - progress: 7858 of 8893 (88%)
    INFO  - progress: 8001 of 8893 (89%)
    INFO  - progress: 8110 of 8893 (91%)
    INFO  - progress: 8208 of 8893 (92%)
    INFO  - progress: 8396 of 8893 (94%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8822 of 8893 (99%)
                                                                 
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
- Matching lines found: 110; displaying up to 100.
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
- androidx/core/app/Person.java:10: private static final String IS_BOT_KEY = "isBot";
- androidx/core/app/Person.java:27: return new Builder().setName(persistableBundle.getString("name")).setUri(persistableBundle.getString(Person.URI_KEY)).setKey(persistableBundle.getString(Person.KEY_KEY)).setBot(persistableBundle.ge...
- androidx/core/app/Person.java:35: persistableBundle.putBoolean(Person.IS_BOT_KEY, person.mIsBot);
- androidx/core/app/Person.java:124: return new Builder().setName(bundle.getCharSequence("name")).setIcon(bundle2 != null ? IconCompat.createFromBundle(bundle2) : null).setUri(bundle.getString(URI_KEY)).setKey(bundle.getString(KEY_KEY...
- androidx/core/app/Person.java:181: bundle.putBoolean(IS_BOT_KEY, this.mIsBot);
- com/adjust/sdk/BackoffStrategy.java:12: long milliSecondMultiplier;
- com/adjust/sdk/BackoffStrategy.java:18: this.milliSecondMultiplier = j;
- com/adjust/sdk/Util.java:337: return (long) (Math.min(((long) Math.pow(2.0d, i - backoffStrategy.minRetries)) * backoffStrategy.milliSecondMultiplier, backoffStrategy.maxWait) * randomInRange(backoffStrategy.minRange, backoffSt...
- com/google/common/base/CharMatcher.java:904: static final int MULTIPLIER = 1682554634;
- com/google/common/base/CharMatcher.java:915: return TABLE.charAt((MULTIPLIER * c) >>> SHIFT) == c;
- com/google/common/escape/CharEscaper.java:9: private static final int DEST_PAD_MULTIPLIER = 2;
- com/google/thirdparty/publicsuffix/PublicSuffixPatterns.java:7: public static final ImmutableMap<String, PublicSuffixType> EXACT = TrieParser.parseTrie("a&0&0trk9--nx?27qjf--nx?e9ebgn--nx?nbb0c7abgm--nx??1&2oa08--nx?apg6qpcbgm--nx?hbbgm--nx?rdceqa08--nx??2&8ugb...
- com/platinmods/AnimationSetupCallback.java:1: package com.platinmods;
- com/platinmods/FloatingModMenuService.java:1: package com.platinmods;
- com/platinmods/FloatingModMenuService.java:121: button.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.12
- com/platinmods/FloatingModMenuService.java:141: button.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.13
- com/platinmods/FloatingModMenuService.java:172: button.setOnClickListener(new View.OnClickListener(z, i, strReplace, button) { // from class: com.platinmods.FloatingModMenuService.14
- com/platinmods/FloatingModMenuService.java:222: checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() { // from class: com.platinmods.FloatingModMenuService.17
- com/platinmods/FloatingModMenuService.java:256: View.OnClickListener onClickListener = new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.18
- com/platinmods/FloatingModMenuService.java:315: seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() { // from class: com.platinmods.FloatingModMenuService.11
- com/platinmods/FloatingModMenuService.java:368: spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() { // from class: com.platinmods.FloatingModMenuService.15
- com/platinmods/FloatingModMenuService.java:394: r0.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() { // from class: com.platinmods.FloatingModMenuService.10
- com/platinmods/FloatingModMenuService.java:422: button.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.16
- com/platinmods/FloatingModMenuService.java:515: button.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.9
- com/platinmods/FloatingModMenuService.java:567: this.startimage.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.2
- com/platinmods/FloatingModMenuService.java:591: textView.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.3
- com/platinmods/FloatingModMenuService.java:645: titanicButton.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.4
- com/platinmods/FloatingModMenuService.java:654: titanicButton.setOnLongClickListener(new View.OnLongClickListener() { // from class: com.platinmods.FloatingModMenuService.5
- com/platinmods/FloatingModMenuService.java:667: button.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.6
- com/platinmods/FloatingModMenuService.java:703: new Handler().postDelayed(new Runnable() { // from class: com.platinmods.FloatingModMenuService.7
- com/platinmods/FloatingModMenuService.java:754: return new View.OnTouchListener() { // from class: com.platinmods.FloatingModMenuService.8
- com/platinmods/FloatingModMenuService.java:811: valueAnimatorOfFloat.addUpdateListener(new ValueAnimator.AnimatorUpdateListener() { // from class: com.platinmods.FloatingModMenuService.19
- com/platinmods/FloatingModMenuService.java:846: handler.post(new Runnable() { // from class: com.platinmods.FloatingModMenuService.1
- com/platinmods/MainActivity.java:1: package com.platinmods;
- com/platinmods/MainActivity.java:11: new Handler().postDelayed(new Runnable() { // from class: com.platinmods.MainActivity.2
- com/platinmods/MainActivity.java:20: new Handler().postDelayed(new Runnable() { // from class: com.platinmods.MainActivity.1
- com/platinmods/PMLauncher.java:1: package com.platinmods;
- com/platinmods/PMLauncher.java:19: activity.runOnUiThread(new Runnable() { // from class: com.platinmods.PMLauncher.1
- com/platinmods/PMLauncher.java:70: System.loadLibrary("platinmods");
- com/platinmods/Preferences.java:1: package com.platinmods;
- com/platinmods/Shimmer.java:1: package com.platinmods;
- com/platinmods/Shimmer.java:87: final Runnable runnable = new Runnable() { // from class: com.platinmods.Shimmer.1
- com/platinmods/Shimmer.java:101: Shimmer.this.animator.addListener(new Animator.AnimatorListener() { // from class: com.platinmods.Shimmer.1.1
- com/platinmods/Shimmer.java:134: v.setAnimationSetupCallback(new ShimmerViewHelper.AnimationSetupCallback() { // from class: com.platinmods.Shimmer.2
- com/platinmods/Shimmer.java:135: @Override // com.platinmods.ShimmerViewHelper.AnimationSetupCallback
- com/platinmods/ShimmerButton.java:1: package com.platinmods;
- com/platinmods/ShimmerButton.java:34: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:39: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:44: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:49: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:54: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:77: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:82: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:87: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:92: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerButton.java:97: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:1: package com.platinmods;
- com/platinmods/ShimmerTextView.java:34: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:39: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:44: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:49: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:54: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:77: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:82: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:87: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:92: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerTextView.java:97: @Override // com.platinmods.ShimmerViewBase
- com/platinmods/ShimmerViewBase.java:1: package com.platinmods;
- com/platinmods/ShimmerViewHelper.java:1: package com.platinmods;
- com/platinmods/Titanic.java:1: package com.platinmods;
- com/platinmods/Titanic.java:33: final Runnable runnable = new Runnable() { // from class: com.platinmods.Titanic.3
- com/platinmods/Titanic.java:50: Titanic.this.animatorSet.addListener(new Animator.AnimatorListener() { // from class: com.platinmods.Titanic.3.1
- com/platinmods/Titanic.java:83: titanicButton.setAnimationSetupCallback(new AnimationSetupCallback() { // from class: com.platinmods.Titanic.4
- com/platinmods/Titanic.java:84: @Override // com.platinmods.AnimationSetupCallback
- com/platinmods/Titanic.java:89: @Override // com.platinmods.AnimationSetupCallback
- com/platinmods/Titanic.java:97: final Runnable runnable = new Runnable() { // from class: com.platinmods.Titanic.1
- com/platinmods/Titanic.java:114: Titanic.this.animatorSet.addListener(new Animator.AnimatorListener() { // from class: com.platinmods.Titanic.1.1
- com/platinmods/Titanic.java:147: titanicTextView.setAnimationSetupCallback(new AnimationSetupCallback() { // from class: com.platinmods.Titanic.2
- com/platinmods/Titanic.java:148: @Override // com.platinmods.AnimationSetupCallback
- com/platinmods/Titanic.java:152: @Override // com.platinmods.AnimationSetupCallback
- com/platinmods/TitanicButton.java:1: package com.platinmods;
- com/platinmods/TitanicButton.java:45: Drawable drawableCreateFromStream = Drawable.createFromStream(context.getAssets().open("platinmodsRB.png"), null);
- com/platinmods/TitanicTextView.java:1: package com.platinmods;

## Search hits in decoded resources
- Matching lines found: 0; displaying up to 0.
- No matching term was found in the scanned decoded resource XML/text.

## Search hits in selected native/IL2CPP strings
- Total matching printable strings: 468.
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
- Cheat
- CHEATCARD
- autoPlay
- CutinDamage
- DamageVoiceTable
- PROCESS_DAMAGE
- PROCESS_DAMAGE1
- PROCESS_DAMAGE2
- PROCESS_DAMAGE3
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
- _ZNK8CryptoPP7Integer21MultiplicativeInverseEv
- _ZTVN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTE
- _ZNK8CryptoPP24MontgomeryRepresentation21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP17ModularArithmetic22MultiplicativeIdentityEv
- _ZNK8CryptoPP17ModularArithmetic21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP24MontgomeryRepresentation22MultiplicativeIdentityEv
- _ZNK8CryptoPP17EuclideanDomainOfINS_7IntegerEE22MultiplicativeIdentityEv
- _ZNK8CryptoPP17EuclideanDomainOfINS_7IntegerEE21MultiplicativeInverseERKS1_
- _ZN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTD0Ev
- _ZNK8CryptoPP12AbstractRingINS_7IntegerEE19MultiplicativeGroupEv
- _ZTIN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTE
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
- _ZNK8CryptoPP7Integer21MultiplicativeInverseEv
- _ZTVN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTE
- _ZNK8CryptoPP24MontgomeryRepresentation21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP17ModularArithmetic22MultiplicativeIdentityEv
- _ZNK8CryptoPP17ModularArithmetic21MultiplicativeInverseERKNS_7IntegerE
- _ZNK8CryptoPP24MontgomeryRepresentation22MultiplicativeIdentityEv
- _ZNK8CryptoPP17EuclideanDomainOfINS_7IntegerEE22MultiplicativeIdentityEv
- _ZNK8CryptoPP17EuclideanDomainOfINS_7IntegerEE21MultiplicativeInverseERKS1_
- _ZN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTD0Ev
- _ZNK8CryptoPP12AbstractRingINS_7IntegerEE19MultiplicativeGroupEv
- _ZTIN8CryptoPP12AbstractRingINS_7IntegerEE20MultiplicativeGroupTE

## Interpretation guardrails
- Exact string hits locate potential code/resources; they do not prove event wiring, control flow, or that a menu toggle works.
- JADX primarily analyzes DEX/Java/Kotlin code. Unity IL2CPP game logic may be compiled into native libraries and metadata; full native tracing requires separate tooling and careful symbol/metadata analysis.
- Static decompilation does not prove server-authoritative behavior, online compatibility, or runtime success.
- The APK was not executed or installed. Temporary decompiled source was not committed to the repository.

## Recommended next step
Review the source/resource/native-string hits together with the decompiled manifest. Record exact file/class/method evidence for each feature in MOD_CANDIDATES.md, then separate code-reading hypotheses from any isolated test results.

