# APKPure IL2CPP Analysis

**Generated:** 2026-10-27 04:15:53 UTC
**Status:** IL2CPP_DUMP_PARTIAL
**Tool:** Perfare Il2CppDumper 6.7.46
**Source rule:** APKPure Original is the input; Platinmods is not used by this stage.
**Method:** extracts read-only binary inputs to a temporary workspace and runs static metadata recovery. No APK is installed or executed.

## Source integrity
- Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest
- Tag: APKPure_Latest
- XAPK asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- Container size: 92726986 bytes
- GitHub expected SHA-256: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16
- Calculated container SHA-256: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16
- Container digest match: True
- Primary APK member: jp.konami.duellinks.apk
- Primary APK outer CRC: FAIL
- ARM64 split member: config.arm64_v8a.apk
- ARM64 split outer CRC: FAIL
- ARM64 libil2cpp.so size: 64335248 bytes
- ARM64 libil2cpp.so SHA-256: 4f865d1c8fd657b9ee6d335864208c1b0a13dca8932bba8683668ddaf9faef29
- global-metadata.dat size: 11183816 bytes
- global-metadata.dat SHA-256: c7cc5295d5e9dbec0feba45a0af855ece74dcfa33fae4be798f1fa6a845ff6d4
- Dumper archive: https://github.com/Perfare/Il2CppDumper/releases/download/v6.7.46/Il2CppDumper-net6-v6.7.46.zip
- Dumper archive size: 406027 bytes
- Dumper archive SHA-256: db9bbbc538e33abfb057c7757ae5d6c1f16a05fdc0d13af8a5a67ea31faaba0c

## Il2CppDumper result
- Exit code: -6
- dump.cs generated: YES
- script.json generated: YES
- stringliteral.json generated: YES
- Focused dump.cs match lines: 80

### Focused type/method context
- dump.cs:17616: public const PvP.Command RESULT = 7;
- dump.cs:17617: public const PvP.Command DBGCMD = 8;
- dump.cs:17618: public const PvP.Command CHEATCARD = 9;
- dump.cs:17619: public const PvP.Command CHAT = 10;
- dump.cs:17620: public const PvP.Command LIST = 11;
- dump.cs:23550: public bool playOnRealTime; // 0x2E
- dump.cs:23551: public Action onFinished; // 0x30
- dump.cs:23552: public bool autoPlay; // 0x38
- dump.cs:23553: public Action<TimelineWrapper> onLoaded; // 0x40
- dump.cs:23554: 
- dump.cs:24012: 
- dump.cs:24013: // RVA: 0x1A56AA0 Offset: 0x1A52AA0 VA: 0x1A56AA0
- dump.cs:24014: public static void OpenTimelineWithCreateCanvas(string path, Action<TimelineWrapper> onLoaded, Action onFinished, Transform parentTrans, int cameraDepth = 1, bool widthFit = True, bool autoPlay = True, bool onSaveState = False, bool onSaveChildState = True, bo
- dump.cs:24015: 
- dump.cs:24016: // RVA: 0x1A56F3C Offset: 0x1A52F3C VA: 0x1A56F3C
- dump.cs:24017: public static void OpenTimeline(string path, Action<TimelineWrapper> onLoaded, Action onFinished, Transform parentTrans, bool widthFit = True, bool widthFitRefParentSize = False, bool autoPlay = True, bool onSaveState = False, bool onSaveChildState = True, boo
- dump.cs:24018: 
- dump.cs:24019: // RVA: 0x1A57310 Offset: 0x1A53310 VA: 0x1A57310
- dump.cs:45235: public const IDS_CARD PROCESS_NOISE2 = 209;
- dump.cs:45236: public const IDS_CARD PROCESS_NOISE3 = 210;
- dump.cs:45237: public const IDS_CARD PROCESS_DAMAGE = 211;
- dump.cs:45238: public const IDS_CARD PROCESS_DAMAGE1 = 212;
- dump.cs:45239: public const IDS_CARD PROCESS_DAMAGE2 = 213;
- dump.cs:45240: public const IDS_CARD PROCESS_DAMAGE3 = 214;
- dump.cs:45241: public const IDS_CARD PROCESS_SAND = 215;
- dump.cs:45242: public const IDS_CARD PROCESS_SAND1 = 216;
- dump.cs:69990: public DuelMenu.MANUAL_TYPE manualType; // 0x14
- dump.cs:69991: public bool production3DEnable; // 0x18
- dump.cs:69992: public bool autoPlayEnable; // 0x19
- dump.cs:69993: public bool fastAutoEnable; // 0x1A
- dump.cs:69994: public bool manualChainEnable; // 0x1B
- dump.cs:70007: 
- dump.cs:70008: // RVA: 0x1BEA66C Offset: 0x1BE666C VA: 0x1BEA66C
- dump.cs:70009: public void .ctor(DuelMenu.CAMERA_TYPE init_cameraType, DuelMenu.CONTROL_TYPE init_controlType, DuelMenu.CHAIN_TYPE init_chainType, DuelMenu.ACTORDER_TYPE init_actorderType, DuelMenu.MANUAL_TYPE init_manualType, DuelMenu.UI_LAYOUT_TYPE init_uiLayoutType, bool 
- dump.cs:70010: }
- dump.cs:70011: 
- dump.cs:70045: public static DuelMenu.UI_LAYOUT_TYPE uiLayoutType { get; }
- dump.cs:70046: public static bool production3D { get; }
- dump.cs:70047: public static bool autoPlay { get; }
- dump.cs:70048: public static bool fastAuto { get; }
- dump.cs:70049: public static bool manualChain { get; }
- dump.cs:70114: 
- dump.cs:70115: // RVA: 0x1BE6AD0 Offset: 0x1BE2AD0 VA: 0x1BE6AD0
- dump.cs:70116: public static bool get_autoPlay() { }
- dump.cs:70117: 
- dump.cs:70118: // RVA: 0x1BE6B28 Offset: 0x1BE2B28 VA: 0x1BE6B28
- dump.cs:70242: 
- dump.cs:70243: // RVA: 0x1BE94C0 Offset: 0x1BE54C0 VA: 0x1BE94C0
- dump.cs:70244: private static bool GetAutoPlay() { }
- dump.cs:70245: 
- dump.cs:70246: // RVA: 0x1BE9564 Offset: 0x1BE5564 VA: 0x1BE9564
- dump.cs:73718: 
- dump.cs:73719: // RVA: 0x1C406C4 Offset: 0x1C3C6C4 VA: 0x1C406C4
- dump.cs:73720: public void ChangeAutoPlay() { }
- dump.cs:73721: 
- dump.cs:73722: // RVA: 0x1C403A0 Offset: 0x1C3C3A0 VA: 0x1C403A0
- dump.cs:73723: public void SetAutoPlay(bool active) { }
- dump.cs:73724: 
- dump.cs:73725: // RVA: 0x1C31374 Offset: 0x1C2D374 VA: 0x1C31374
- dump.cs:74935: private bool <fastForwardEnable>k__BackingField; // 0xC3
- dump.cs:74936: [CompilerGenerated]
- dump.cs:74937: private bool <IsAutoPlay>k__BackingField; // 0xC4
- dump.cs:74938: [CompilerGenerated]
- dump.cs:74939: private string <series>k__BackingField; // 0xC8
- dump.cs:75006: private bool __isFastForward { get; set; }
- dump.cs:75007: public bool fastForwardEnable { get; set; }
- dump.cs:75008: public bool IsAutoPlay { get; set; }
- dump.cs:75009: public string series { get; set; }
- dump.cs:75010: public string lastSeries { get; set; }
- dump.cs:75188: [CompilerGenerated]
- dump.cs:75189: // RVA: 0x1C5810C Offset: 0x1C5410C VA: 0x1C5810C
- dump.cs:75190: public bool get_IsAutoPlay() { }
- dump.cs:75191: 
- dump.cs:75192: [CompilerGenerated]
- dump.cs:75193: // RVA: 0x1C58114 Offset: 0x1C54114 VA: 0x1C58114
- dump.cs:75194: public void set_IsAutoPlay(bool value) { }
- dump.cs:75195: 
- dump.cs:75196: [CompilerGenerated]
- dump.cs:168907: private DuelClient.Step step; // 0x278
- dump.cs:168908: private Dictionary<string, object> dicResult; // 0x280
- dump.cs:168909: private bool reqAutoPlay; // 0x288
- dump.cs:168910: private float elapsedTimeAtWaitingResourceManager; // 0x28C
- dump.cs:168911: private const float maxTimeOfWaitingResourceManager = 5;
- dump.cs:168912: [CompilerGenerated]
- dump.cs:168913: private bool <isAutoPlay>k__BackingField; // 0x290
- dump.cs:168914: private bool m_isFast; // 0x291
- dump.cs:168915: [CompilerGenerated]
- dump.cs:168916: private int <autoPlayState>k__BackingField; // 0x294
- dump.cs:168917: [CompilerGenerated]
- dump.cs:168918: private Action<bool> <OnChangeAutoPlay>k__BackingField; // 0x298
- dump.cs:168919: private bool enabledAutoPlay; // 0x2A0
- dump.cs:168920: private ReplayStream replayStream; // 0x2A8
- dump.cs:168921: private bool isEngineRepalyMode; // 0x2B0
- dump.cs:168965: public static bool isPlayingSummonProduction { get; }
- dump.cs:168966: public static bool isDetectedTermination { get; }
- dump.cs:168967: public bool isAutoPlay { get; set; }
- dump.cs:168968: public bool isFast { get; set; }
- dump.cs:168969: public int autoPlayState { get; set; }
- dump.cs:168970: public Action<bool> OnChangeAutoPlay { get; set; }
- dump.cs:168971: public bool IsEngineInitialized { get; }

### Dumper log excerpt
    Initializing metadata...
    Metadata Version: 31
    Initializing il2cpp file...
    Applying relocations...
    WARNING: find JNI_OnLoad
    ERROR: This file may be protected.
    Il2Cpp Version: 31
    Searching...
    CodeRegistration : 3924ae0
    MetadataRegistration : 3a622c8
    Dumping...
    Done!
    Generate struct...
    Done!
    Generate dummy dll...
    Done!
    Press any key to exit...
    
    Unhandled exception. System.InvalidOperationException: Cannot read keys when either application does not have a console or when console input has been redirected. Try Console.Read.
       at System.ConsolePal.ReadKey(Boolean intercept)
       at Il2CppDumper.Program.Main(String[] args) in C:\projects\il2cppdumper\Il2CppDumper\Program.cs:line 109

## Interpretation
- Method names/type declarations recovered by Il2CppDumper are static metadata evidence; they do not prove a menu callback invokes the method or that behavior works at runtime.
- The APKPure XAPK and selected entries have reported CRC/decompression problems. Even successful metadata extraction does not clear those integrity warnings.
- Native library and metadata outputs are temporary; only this summary report is persisted.

