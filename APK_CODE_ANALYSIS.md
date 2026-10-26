# APK Code Analysis Report

**Generated:** 2026-10-26 05:24:58 UTC
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
    I: Baksmaling classes.dex...
    I: Baksmaling classes2.dex...
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
    INFO  - progress: 6638 of 8893 (74%)
    INFO  - progress: 6785 of 8893 (76%)
    INFO  - progress: 6983 of 8893 (78%)
    INFO  - progress: 7098 of 8893 (79%)
    INFO  - progress: 7172 of 8893 (80%)
    INFO  - progress: 7250 of 8893 (81%)
    INFO  - progress: 7378 of 8893 (82%)
    INFO  - progress: 7448 of 8893 (83%)
    INFO  - progress: 7583 of 8893 (85%)
    INFO  - progress: 7771 of 8893 (87%)
    INFO  - progress: 7822 of 8893 (87%)
    INFO  - progress: 8001 of 8893 (89%)
    INFO  - progress: 8137 of 8893 (91%)
    INFO  - progress: 8217 of 8893 (92%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8535 of 8893 (95%)
    INFO  - progress: 8618 of 8893 (96%)
                                                                 
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
- Matching source lines found: 135; displaying context for up to 100 lines.
- com/platinmods/FloatingModMenuService.java:60: /* JADX INFO: loaded from: classes3.dex */
- com/platinmods/FloatingModMenuService.java:61: public class FloatingModMenuService extends Service {
- com/platinmods/FloatingModMenuService.java:62: public static final String TAG = "Mod_Menu";
- com/platinmods/FloatingModMenuService.java:65: GradientDrawable gdMenuBody;
- com/platinmods/FloatingModMenuService.java:66: String inputFieldFeatureName;
- com/platinmods/FloatingModMenuService.java:67: int inputFieldFeatureNum;
- com/platinmods/FloatingModMenuService.java:66: String inputFieldFeatureName;
- com/platinmods/FloatingModMenuService.java:67: int inputFieldFeatureNum;
- com/platinmods/FloatingModMenuService.java:68: TextView inputFieldTextView;
- com/platinmods/FloatingModMenuService.java:87: final int MENU_BG_COLOR = Color.parseColor("#DD1C2A35");
- com/platinmods/FloatingModMenuService.java:88: final int MENU_FEATURE_BG_COLOR = Color.parseColor("#FF171E24");
- com/platinmods/FloatingModMenuService.java:89: final int MENU_WIDTH = 290;
- com/platinmods/FloatingModMenuService.java:120: button.setBackgroundColor(this.BTN_COLOR);
- com/platinmods/FloatingModMenuService.java:121: button.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.12
- com/platinmods/FloatingModMenuService.java:122: @Override // android.view.View.OnClickListener
- com/platinmods/FloatingModMenuService.java:123: public void onClick(View view) {
- com/platinmods/FloatingModMenuService.java:124: FloatingModMenuService.this.localChanges(i, false);
- com/platinmods/FloatingModMenuService.java:125: Preferences.changeFeatureInt(str, i, 0);
- com/platinmods/FloatingModMenuService.java:124: FloatingModMenuService.this.localChanges(i, false);
- com/platinmods/FloatingModMenuService.java:125: Preferences.changeFeatureInt(str, i, 0);
- com/platinmods/FloatingModMenuService.java:126: }
- com/platinmods/FloatingModMenuService.java:140: button.setBackgroundColor(this.BTN_COLOR);
- com/platinmods/FloatingModMenuService.java:141: button.setOnClickListener(new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.13
- com/platinmods/FloatingModMenuService.java:142: @Override // android.view.View.OnClickListener
- com/platinmods/FloatingModMenuService.java:146: intent.setData(Uri.parse(str2));
- com/platinmods/FloatingModMenuService.java:147: FloatingModMenuService.this.startActivity(intent);
- com/platinmods/FloatingModMenuService.java:148: }
- com/platinmods/FloatingModMenuService.java:162: String strReplace = str.replace("OnOff_", "");
- com/platinmods/FloatingModMenuService.java:163: if (Preferences.loadPrefBoolean(str, i)) {
- com/platinmods/FloatingModMenuService.java:164: button.setText(strReplace + ": ON");
- com/platinmods/FloatingModMenuService.java:171: }
- com/platinmods/FloatingModMenuService.java:172: button.setOnClickListener(new View.OnClickListener(z, i, strReplace, button) { // from class: com.platinmods.FloatingModMenuService.14
- com/platinmods/FloatingModMenuService.java:173: boolean isOn;
- com/platinmods/FloatingModMenuService.java:174: final /* synthetic */ Button val$button;
- com/platinmods/FloatingModMenuService.java:175: final /* synthetic */ int val$featureNum;
- com/platinmods/FloatingModMenuService.java:176: final /* synthetic */ String val$finalFeatureName;
- com/platinmods/FloatingModMenuService.java:175: final /* synthetic */ int val$featureNum;
- com/platinmods/FloatingModMenuService.java:176: final /* synthetic */ String val$finalFeatureName;
- com/platinmods/FloatingModMenuService.java:177: final /* synthetic */ boolean val$finalIsOn;
- com/platinmods/FloatingModMenuService.java:180: this.val$finalIsOn = z;
- com/platinmods/FloatingModMenuService.java:181: this.val$featureNum = i;
- com/platinmods/FloatingModMenuService.java:182: this.val$finalFeatureName = strReplace;
- com/platinmods/FloatingModMenuService.java:181: this.val$featureNum = i;
- com/platinmods/FloatingModMenuService.java:182: this.val$finalFeatureName = strReplace;
- com/platinmods/FloatingModMenuService.java:183: this.val$button = button;
- com/platinmods/FloatingModMenuService.java:188: public void onClick(View view) {
- com/platinmods/FloatingModMenuService.java:189: FloatingModMenuService.this.localChanges(this.val$featureNum, this.isOn);
- com/platinmods/FloatingModMenuService.java:190: Preferences.changeFeatureBoolean(this.val$finalFeatureName, this.val$featureNum, this.isOn);
- com/platinmods/FloatingModMenuService.java:189: FloatingModMenuService.this.localChanges(this.val$featureNum, this.isOn);
- com/platinmods/FloatingModMenuService.java:190: Preferences.changeFeatureBoolean(this.val$finalFeatureName, this.val$featureNum, this.isOn);
- com/platinmods/FloatingModMenuService.java:191: if (this.isOn) {
- com/platinmods/FloatingModMenuService.java:192: this.val$button.setText(this.val$finalFeatureName + ": ON");
- com/platinmods/FloatingModMenuService.java:193: this.val$button.setBackgroundColor(Color.parseColor("#003300"));
- com/platinmods/FloatingModMenuService.java:195: } else {
- com/platinmods/FloatingModMenuService.java:196: this.val$button.setText(this.val$finalFeatureName + ": OFF");
- com/platinmods/FloatingModMenuService.java:197: this.val$button.setBackgroundColor(Color.parseColor("#7f0000"));
- com/platinmods/FloatingModMenuService.java:220: checkBox.setTextColor(this.TEXT_COLOR_2);
- com/platinmods/FloatingModMenuService.java:221: checkBox.setChecked(Preferences.loadPrefBoolean(str, i));
- com/platinmods/FloatingModMenuService.java:222: checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() { // from class: com.platinmods.FloatingModMenuService.17
- com/platinmods/FloatingModMenuService.java:221: checkBox.setChecked(Preferences.loadPrefBoolean(str, i));
- com/platinmods/FloatingModMenuService.java:222: checkBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() { // from class: com.platinmods.FloatingModMenuService.17
- com/platinmods/FloatingModMenuService.java:223: @Override // android.widget.CompoundButton.OnCheckedChangeListener
- com/platinmods/FloatingModMenuService.java:224: public void onCheckedChanged(CompoundButton compoundButton, boolean z) {
- com/platinmods/FloatingModMenuService.java:225: if (checkBox.isChecked()) {
- com/platinmods/FloatingModMenuService.java:226: Preferences.changeFeatureBoolean(str, i, z);
- com/platinmods/FloatingModMenuService.java:227: } else {
- com/platinmods/FloatingModMenuService.java:228: Preferences.changeFeatureBoolean(str, i, z);
- com/platinmods/FloatingModMenuService.java:229: }
- com/platinmods/FloatingModMenuService.java:235: private View RadioButton(final int i, final String str, String str2) {
- com/platinmods/FloatingModMenuService.java:236: FloatingModMenuService floatingModMenuService = this;
- com/platinmods/FloatingModMenuService.java:237: LinkedList linkedList = new LinkedList(Arrays.asList(str2.split(",")));
- com/platinmods/FloatingModMenuService.java:238: final TextView textView = new TextView(floatingModMenuService);
- com/platinmods/FloatingModMenuService.java:239: textView.setText(str + ":");
- com/platinmods/FloatingModMenuService.java:240: textView.setTextColor(floatingModMenuService.TEXT_COLOR_2);
- com/platinmods/FloatingModMenuService.java:241: final RadioGroup radioGroup = new RadioGroup(floatingModMenuService);
- com/platinmods/FloatingModMenuService.java:240: textView.setTextColor(floatingModMenuService.TEXT_COLOR_2);
- com/platinmods/FloatingModMenuService.java:241: final RadioGroup radioGroup = new RadioGroup(floatingModMenuService);
- com/platinmods/FloatingModMenuService.java:242: radioGroup.setPadding(10, 5, 10, 5);
- com/platinmods/FloatingModMenuService.java:249: while (i2 < linkedList.size()) {
- com/platinmods/FloatingModMenuService.java:250: final RadioButton radioButton = new RadioButton(floatingModMenuService);
- com/platinmods/FloatingModMenuService.java:251: final String str3 = (String) linkedList.get(i2);
- com/platinmods/FloatingModMenuService.java:255: int[] iArr4 = iArr;
- com/platinmods/FloatingModMenuService.java:256: View.OnClickListener onClickListener = new View.OnClickListener() { // from class: com.platinmods.FloatingModMenuService.18
- com/platinmods/FloatingModMenuService.java:257: @Override // android.view.View.OnClickListener
- com/platinmods/FloatingModMenuService.java:260: textView.setText(Html.fromHtml("<font face='roboto'>" + str + ": <font color='#41c300'>" + str3 + "</font>"));
- com/platinmods/FloatingModMenuService.java:261: Preferences.changeFeatureInt(str, i, radioGroup.indexOfChild(radioButton));
- com/platinmods/FloatingModMenuService.java:262: }
- com/platinmods/FloatingModMenuService.java:272: i2 = i3 + 1;
- com/platinmods/FloatingModMenuService.java:273: floatingModMenuService = this;
- com/platinmods/FloatingModMenuService.java:274: colorStateList = colorStateList2;
- com/platinmods/FloatingModMenuService.java:299: private View SeekBar(final int i, final String str, final int i2, int i3) {
- com/platinmods/FloatingModMenuService.java:300: int iLoadPrefInt = Preferences.loadPrefInt(str, i);
- com/platinmods/FloatingModMenuService.java:301: LinearLayout linearLayout = new LinearLayout(this);
- com/platinmods/FloatingModMenuService.java:314: seekBar.setProgress(iLoadPrefInt == 0 ? i2 : iLoadPrefInt);
- com/platinmods/FloatingModMenuService.java:315: seekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() { // from class: com.platinmods.FloatingModMenuService.11
- com/platinmods/FloatingModMenuService.java:316: @Override // android.widget.SeekBar.OnSeekBarChangeListener
- com/platinmods/FloatingModMenuService.java:328: }
- com/platinmods/FloatingModMenuService.java:329: Preferences.changeFeatureInt(str2, i6, i7);
- com/platinmods/FloatingModMenuService.java:330: TextView textView2 = textView;
- com/platinmods/FloatingModMenuService.java:366: spinner.setAdapter((SpinnerAdapter) arrayAdapter);

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

