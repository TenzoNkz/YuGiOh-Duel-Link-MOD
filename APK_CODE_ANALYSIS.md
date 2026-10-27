# APK Code Analysis Report

**Generated:** 2026-10-27 04:26:09 UTC
**Method:** JADX/Apktool static analysis; the APK was not installed or executed.
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Requested release tag: APKPure_Latest
- JADX pinned version: 1.5.6
- Apktool pinned version: 3.0.3

## Source Release and integrity
- Release page: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest
- Release tag: APKPure_Latest
- Release asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- GitHub-reported size: 92726986 bytes
- Downloaded container size: 92726986 bytes
- Expected container SHA-256: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16
- Calculated container SHA-256: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16
- Container digest comparison: PASS
- Package input type: XAPK
- APK selected for code analysis: jp.konami.duellinks.apk
- Selected APK size: 55854706 bytes
- Embedded APK members: 2
- Embedded APK member: config.arm64_v8a.apk (36869159 bytes); outer CRC: FAIL; scan: EXTRACTED
- Embedded APK member: jp.konami.duellinks.apk (55854706 bytes); outer CRC: FAIL; scan: EXTRACTED
- Embedded APKs extracted for static inventory: 2
- OBB members in XAPK: 0
- No OBB member detected.
- Selected APK member CRC in outer XAPK: FAIL

**Status:** CODE_ANALYSIS_PARTIAL

## Android manifest (decoded by Apktool)
- Package name: jp.konami.duellinks
- Version name: not declared
- Version code: not declared
- minSdkVersion: not declared
- targetSdkVersion: not declared
- Application class: not declared
- Application label reference: @string/app_name
- Declared permission entries: 16
  - android.permission.INTERNET
  - android.permission.ACCESS_NETWORK_STATE
  - android.permission.ACCESS_WIFI_STATE
  - android.permission.POST_NOTIFICATIONS
  - com.google.android.gms.permission.AD_ID
  - com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE
  - android.permission.VIBRATE
  - android.permission.WRITE_EXTERNAL_STORAGE
  - android.permission.READ_EXTERNAL_STORAGE
  - com.android.vending.BILLING
  - android.permission.WAKE_LOCK
  - com.google.android.c2dm.permission.RECEIVE
  - android.permission.ACCESS_ADSERVICES_ATTRIBUTION
  - android.permission.ACCESS_ADSERVICES_AD_ID
  - jp.konami.duellinks.permission.C2D_MESSAGE
  - jp.konami.duellinks.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION
- Declared activity/service/receiver/provider entries: 24
  - service: com.google.firebase.messaging.MessageForwardingService, exported=true, permission=android.permission.BIND_JOB_SERVICE
  - receiver: jp.konami.duellinks.plugins.LocalPushNotificationReceiver, exported=unspecified
  - provider: androidx.core.content.FileProvider, exported=false
  - activity: jp.konami.duellinks.plugins.YgomMainActivity, exported=true
  - activity: jp.applilink.sdk.common.ApplilinkWebViewActivity, exported=false
  - activity: com.android.billingclient.api.ProxyBillingActivity, exported=false
  - activity: com.android.billingclient.api.ProxyBillingActivityV2, exported=false
  - receiver: com.google.firebase.iid.FirebaseInstanceIdReceiver, exported=true, permission=com.google.android.c2dm.permission.SEND
  - service: com.google.firebase.messaging.FirebaseMessagingService, exported=false
  - service: com.google.firebase.components.ComponentDiscoveryService, exported=false
  - receiver: com.google.android.gms.measurement.AppMeasurementReceiver, exported=false
  - service: com.google.android.gms.measurement.AppMeasurementService, exported=false
  - service: com.google.android.gms.measurement.AppMeasurementJobService, exported=false, permission=android.permission.BIND_JOB_SERVICE
  - activity: com.google.android.gms.common.api.GoogleApiActivity, exported=false
  - provider: com.google.firebase.provider.FirebaseInitProvider, exported=false
  - service: com.google.firebase.messaging.cpp.ListenerService, exported=false
  - service: com.google.firebase.messaging.cpp.RegistrationIntentService, exported=false
  - activity: com.google.games.bridge.GenericResolutionActivity, exported=false
  - activity: com.google.android.gms.auth.api.signin.internal.SignInHubActivity, exported=false
  - service: com.google.android.gms.auth.api.signin.RevocationBoundService, exported=true, permission=com.google.android.gms.auth.api.signin.permission.REVOCATION_NOTIFICATION
  - activity: com.google.games.bridge.NativeBridgeActivity, exported=unspecified
  - service: com.google.android.datatransport.runtime.backends.TransportBackendDiscovery, exported=false
  - service: com.google.android.datatransport.runtime.scheduling.jobscheduling.JobInfoSchedulerService, exported=false, permission=android.permission.BIND_JOB_SERVICE
  - receiver: com.google.android.datatransport.runtime.scheduling.jobscheduling.AlarmManagerSchedulerBroadcastReceiver, exported=false

## Tool execution
- Apktool exit code: 1
- JADX exit code: 3
- JADX-reported decompiler error count: 96
- Decompiled Java source files found: 8180
- Decoded Apktool output entries: 18234

### Apktool output excerpt
    Exception in thread "main" brut.androlib.exceptions.AndrolibException: brut.directory.DirectoryException: Error copying file: assets/bin/Data/e1f73dc34613ec042897cc46749d448c
    	at brut.androlib.ApkDecoder.copyRawFiles(SourceFile:239)
    	at brut.androlib.ApkDecoder.decode(SourceFile:95)
    	at brut.apktool.Main.main(SourceFile:523)
    Caused by: brut.directory.DirectoryException: Error copying file: assets/bin/Data/e1f73dc34613ec042897cc46749d448c
    	at brut.directory.Directory.copyToDir(SourceFile:301)
    	at brut.androlib.ApkDecoder.copyRawFiles(SourceFile:265)
    	... 2 more
    Caused by: java.util.zip.ZipException: invalid literal/length code
    	at java.base/java.util.zip.InflaterInputStream.read(InflaterInputStream.java:181)
    	at java.base/java.io.FilterInputStream.read(FilterInputStream.java:95)
    	at org.apache.commons.io.IOUtils.copy(SourceFile:1734)
    	at brut.directory.Directory.copyToDir(SourceFile:46)
    	... 3 more

### JADX output excerpt
    INFO  - progress: 6209 of 8855 (70%)
    INFO  - progress: 6344 of 8855 (71%)
    INFO  - progress: 6437 of 8855 (72%)
    INFO  - progress: 6529 of 8855 (73%)
    INFO  - progress: 6639 of 8855 (74%)
    INFO  - progress: 6722 of 8855 (75%)
    INFO  - progress: 7057 of 8855 (79%)
    INFO  - progress: 7133 of 8855 (80%)
    INFO  - progress: 7320 of 8855 (82%)
    INFO  - progress: 7430 of 8855 (83%)
    INFO  - progress: 7618 of 8855 (86%)
    INFO  - progress: 7732 of 8855 (87%)
    INFO  - progress: 7783 of 8855 (87%)
    INFO  - progress: 7931 of 8855 (89%)
    INFO  - progress: 8035 of 8855 (90%)
    INFO  - progress: 8104 of 8855 (91%)
    INFO  - progress: 8215 of 8855 (92%)
    INFO  - progress: 8496 of 8855 (95%)
    INFO  - progress: 8496 of 8855 (95%)
    INFO  - progress: 8496 of 8855 (95%)
    INFO  - progress: 8496 of 8855 (95%)
    INFO  - progress: 8505 of 8855 (96%)
                                                                 
    ERROR - finished with errors, count: 96

## Decompiled class namespace summary
- Decompiled class files found: 8180
- Classes under jp/konami/duellinks/: 10
- Classes under com/platinmods/: 0
- Top package-prefix counts:
  - com.google.android: 3676
  - com.google.common: 602
  - com.google.firebase: 273
  - org.checkerframework.checker: 222
  - com.unity3d.player: 190
  - kotlinx.coroutines.flow: 184
  - androidx.datastore.preferences: 179
  - kotlinx.coroutines: 133
  - com.android.billingclient: 123
  - androidx.privacysandbox.ads: 106
  - kotlin: 99
  - kotlin.jvm.internal: 84
  - kotlin.collections: 83
  - androidx.appcompat.widget: 79
  - androidx.datastore.core: 79
  - com.adjust.sdk: 77
  - androidx.core.view: 72
  - androidx.annotation: 68
  - kotlinx.coroutines.internal: 60
  - okio: 59
- Sample classes under jp/konami/duellinks/:
  - jp/konami/duellinks/R.java
  - jp/konami/duellinks/plugins/IabProductDetails.java
  - jp/konami/duellinks/plugins/IabPurchase.java
  - jp/konami/duellinks/plugins/IabResult.java
  - jp/konami/duellinks/plugins/LocalPushNotification.java
  - jp/konami/duellinks/plugins/LocalPushNotificationReceiver.java
  - jp/konami/duellinks/plugins/Logger.java
  - jp/konami/duellinks/plugins/R.java
  - jp/konami/duellinks/plugins/YgomMainActivity.java
  - jp/konami/duellinks/plugins/YgomUtility.java
- Classes under com/platinmods/:
  - (none found)

## APK split inventory
- config.arm64_v8a.apk (config/split APK): 14 entries, 9 native libraries, 0 IL2CPP metadata file(s), outer XAPK CRC=FAIL.
- jp.konami.duellinks.apk (primary APK): 3368 entries, 0 native libraries, 1 IL2CPP metadata file(s), outer XAPK CRC=FAIL.

## Native/IL2CPP inventory across readable APK members
- [config.arm64_v8a.apk] lib/arm64-v8a/libFirebaseCppAnalytics.so: 51296 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/libFirebaseCppApp-13_4_0.so: 4139608 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/libFirebaseCppMessaging.so: 67760 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/lib_burst_generated.so: 37104 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/libdatastore_shared_counter.so: 7112 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/libduel.so: 22315680 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/libil2cpp.so: 64335248 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/libmain.so: 6696 bytes
- [config.arm64_v8a.apk] lib/arm64-v8a/libunity.so: 21873584 bytes
- assets/bin/Data/Managed/Metadata/global-metadata.dat: 11183816 bytes

## APK/split read warnings
- [config.arm64_v8a.apk] lib/arm64-v8a/libduel.so: read failed (BadZipFile: Bad CRC-32 for file 'lib/arm64-v8a/libduel.so')

## Search hits in decompiled Java
- Matching lines found: 31; displaying up to 31.
- androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:482: StaticLayout.Builder hyphenationFrequency = builderObtain.setAlignment(alignment).setLineSpacing(textView.getLineSpacingExtra(), textView.getLineSpacingMultiplier()).setIncludePad(textView.getInclu...
- androidx/appcompat/widget/AppCompatTextViewAutoSizeHelper.java:514: return new StaticLayout(charSequence, textPaint, i, alignment, textView.getLineSpacingMultiplier(), textView.getLineSpacingExtra(), textView.getIncludeFontPadding());
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:20: private static final float SHADOW_MULTIPLIER = 1.5f;
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:115: this.mShadowSize = (int) ((even * SHADOW_MULTIPLIER) + this.mInsetShadow + 0.5f);
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:129: return z ? (float) (((double) (f * SHADOW_MULTIPLIER)) + ((1.0d - COS_45) * ((double) f2))) : f * SHADOW_MULTIPLIER;
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:260: float f = this.mRawMaxShadowSize * SHADOW_MULTIPLIER;
- androidx/cardview/widget/RoundRectDrawableWithShadow.java:296: return (Math.max(f, this.mCornerRadius + this.mInsetShadow + ((f * SHADOW_MULTIPLIER) / 2.0f)) * 2.0f) + (((this.mRawMaxShadowSize * SHADOW_MULTIPLIER) + this.mInsetShadow) * 2.0f);
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:24: private int dimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:26: private int oppositeDimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:37: this.offset = this.dimensionMultiplier;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:40: this.oppositeOffset = this.oppositeDimensionMultiplier;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:107: this.offset = this.dimensionMultiplier * this.dimension.value;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:115: this.oppositeOffset = this.oppositeDimensionMultiplier * this.oppositeDimension.value;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:210: this.dimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:212: this.oppositeDimensionMultiplier = 1;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:254: this.dimensionMultiplier = i;
- androidx/constraintlayout/solver/widgets/ResolutionAnchor.java:266: this.oppositeDimensionMultiplier = i;
- com/adjust/sdk/BackoffStrategy.java:12: long milliSecondMultiplier;
- com/adjust/sdk/BackoffStrategy.java:18: this.milliSecondMultiplier = j;
- com/adjust/sdk/Util.java:477: return (long) (Math.min(((long) Math.pow(2.0d, i - backoffStrategy.minRetries)) * backoffStrategy.milliSecondMultiplier, backoffStrategy.maxWait) * randomInRange(backoffStrategy.minRange, backoffSt...
- com/google/common/base/CharMatcher.java:681: static final int MULTIPLIER = 1682554634;
- com/google/common/base/CharMatcher.java:692: return TABLE.charAt((MULTIPLIER * c) >>> SHIFT) == c;
- com/google/common/escape/CharEscaper.java:9: private static final int DEST_PAD_MULTIPLIER = 2;
- jp/applilink/sdk/common/ApplilinkVideoViewActivity.java:43: final boolean booleanExtra = intent.getBooleanExtra("autoPlay", false);
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:73: protected boolean _autoPlay;
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:223: this._autoPlay = false;
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:288: this._autoPlay = z;
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:364: if (str2 != null && str2.length() > 1 && !this._autoPlay) {
- jp/applilink/sdk/common/adview/ApplilinkAdViewVideo.java:753: if (this._autoPlay) {
- jp/applilink/sdk/recommend/RecommendNetworkCore.java:1069: intent.putExtra("autoPlay", z);
- kotlin/collections/builders/MapBuilder.java:385: throw new IllegalStateException("This cannot happen with fixed magic multiplier and grow-only hash array. Have object hashCodes changed?");

## Known reference menu-framework paths checked in APKPure DEX
- Matching source lines found: 0; displaying context for up to 4 lines.
- com/platinmods/FloatingModMenuService.java: not produced by JADX.
- com/platinmods/PMLauncher.java: not produced by JADX.
- com/platinmods/Preferences.java: not produced by JADX.
- com/platinmods/MainActivity.java: not produced by JADX.

## Search hits in decoded resources
- Matching lines found: 0; displaying up to 0.
- No matching term was found in the scanned decoded resource XML/text.

## Focused strings: feature labels, menu callbacks, and duel damage
- Focused string matches found: 10.
### [config.arm64_v8a.apk] lib/arm64-v8a/libil2cpp.so
- DLL_DuelGetDamageValue
### [jp.konami.duellinks.apk] assets/bin/Data/Managed/Metadata/global-metadata.dat
- URORAIDS_CARD.PROCESS_BLAZEIDS_CARD.PROCESS_CRYSTALIDS_CARD.PROCESS_DAMAGEIDS_CARD.PROCESS_DARKNESSIDS_CARD.PROCESS_FULLSTARLIGHTIDS_C
- CHEATCARD
- PROCESS_DAMAGE
- PROCESS_DAMAGE1
- PROCESS_DAMAGE2
- PROCESS_DAMAGE3
- DLL_DuelGetDamageValue
- ShowMonster
- showMonster

## Search hits in selected native/IL2CPP strings
- Total matching printable strings: 267.
### [config.arm64_v8a.apk] lib/arm64-v8a/libil2cpp.so
- DLL_DuelGetDamageDstPosition
- DLL_DuelGetDamageSrcPosition
- UnityEngine.Rendering.CommandBuffer::SetInstanceMultiplier_Injected(System.IntPtr,System.UInt32)
- DLL_DuelGetDamageValue
- UnityEngine.ParticleSystem/MainModule::get_startDelayMultiplier()
- UnityEngine.ParticleSystem/MainModule::get_startLifetimeMultiplier()
- UnityEngine.ParticleSystem/MainModule::set_startDelayMultiplier(System.Single)
### [config.arm64_v8a.apk] lib/arm64-v8a/libunity.so
- SetInstanceMultiplier
- octaveMultiplier
- ExternalForcesModule.multiplierCurve.scalar
- multiplierCurve
- UnityEngine.Rendering.CommandBuffer::SetInstanceMultiplier_Injected
- multiplier
- widthMultiplier
- UnityEngine.ParticleSystem/MainModule::get_startDelayMultiplier
- NoiseModule.octaveMultiplier
- damaged LZ stream
- downscaleMultiplier
- m_Parameters.widthMultiplier
- UnityEngine.ParticleSystem/MainModule::set_startDelayMultiplier
- UnityEngine.ParticleSystem/MainModule::get_startLifetimeMultiplier
- m_IntensityMultiplier
- ExternalForcesModule.multiplierCurve.minScalar
### [jp.konami.duellinks.apk] assets/bin/Data/Managed/Metadata/global-metadata.dat
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

## Interpretation guardrails
- Exact string hits locate potential code/resources; they do not prove event wiring, control flow, or that a menu toggle works.
- JADX primarily analyzes DEX/Java/Kotlin code. Unity IL2CPP game logic may be compiled into native libraries and metadata; full native tracing requires separate tooling and careful symbol/metadata analysis.
- Static decompilation does not prove server-authoritative behavior, online compatibility, or runtime success.
- The APK was not executed or installed. Temporary decompiled source was not committed to the repository.
- For XAPK input, JADX/Apktool decompile the selected primary APK; native-library and metadata inventory also scans other readable split APKs. Split payloads are not merged or proven installable as a single APK.
- The outer XAPK member CRC is reported separately from the selected APK's own ZIP structure. A failed outer CRC must be investigated and prevents treating the source container as clean, even if static analysis can read the inner APK bytes.

## Recommended next step
Review the source/resource/native-string hits together with the decompiled manifest. Record exact file/class/method evidence for each feature in MOD_CANDIDATES.md, then separate code-reading hypotheses from any isolated test results.

