# APKPure IL2CPP Analysis

**Generated:** 2026-10-27 05:20:56 UTC
**Status:** IL2CPP_OUTPUTS_GENERATED_WITH_POST_DUMP_CONSOLE_ERROR
**Tool:** Perfare Il2CppDumper 6.7.46
**Source rule:** APKPure Original is the input; Platinmods is not used by this stage.
**Method:** extracts read-only binary inputs to a temporary workspace and runs static metadata recovery. No APK is installed or executed.

## Source integrity
- Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/APKPure_Latest
- Tag: APKPure_Latest
- XAPK asset: Yu-Gi-Oh.Duel.Links.APKPure.V11.1.0.xapk
- Container size: 92726986 bytes
- GitHub expected SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb
- Calculated container SHA-256: 66ba31c32fbba03b5fe0f75ef27dd9fa875978de7921a0c4ee8b93b878ce64eb
- Container digest match: True
- Primary APK member: jp.konami.duellinks.apk
- Primary APK outer CRC: PASS
- ARM64 split member: config.arm64_v8a.apk
- ARM64 split outer CRC: PASS
- Primary APK inner CRC scan: PASS (all archive entries passed)
- ARM64 split inner CRC scan: PASS (all archive entries passed)
- Integrity assessment: Container digest, embedded-member outer CRCs, and both inner APK CRC scans passed.
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
- Focused dump.cs match lines: 101
- Output generation confirmed from log: YES
- Final console-input exception after generation: YES
- Match count by term group:
  - ShowMonster: 2
  - Card-face API: 10
  - CHEATCARD: 1
  - PROCESS_DAMAGE: 4
  - Damage getter: 2
  - Damage positions: 14
  - AutoPlay: 46
  - DuelMenu/AutoPlay settings: 20
  - Monster/status: 2

### Focused type/method context
- ShowMonster: 2 matching dump.cs line(s); showing up to 3 context(s).
  - [CONTEXT] dump.cs:205060: public class CardRoot : MonoBehaviour, ICardStatusIconAnchor // TypeDefIndex: 4363
  - [CONTEXT] dump.cs:205371: // RVA: 0x22B652C Offset: 0x22B252C VA: 0x22B652C
  - [MATCH] dump.cs:205372: public void ShowMonster(bool immediate, bool showAura, Action onFinished) { }
  - [CONTEXT] dump.cs:205373: 
  - [CONTEXT] dump.cs:216022: public class Task3DCardMove : Task3D // TypeDefIndex: 4631
  - [CONTEXT] dump.cs:216037: private CardPlace toPlace; // 0x98
  - [MATCH] dump.cs:216038: private bool showMonster; // 0xA0
  - [CONTEXT] dump.cs:216039: 
- Card-face API: 10 matching dump.cs line(s); showing up to 3 context(s).
  - [CONTEXT] dump.cs:168769: public class DuelClient : ViewController, IFadeSupported, IDynamicHeaderSupported // TypeDefIndex: 3553
  - [CONTEXT] dump.cs:169587: // RVA: 0x2142574 Offset: 0x213E574 VA: 0x2142574
  - [MATCH] dump.cs:169588: public static bool GetFieldCardFace(int player, int position, int index) { }
  - [CONTEXT] dump.cs:169589: 
  - [CONTEXT] dump.cs:177530: public sealed class Engine // TypeDefIndex: 3734
  - [CONTEXT] dump.cs:177859: // RVA: 0x216C8A4 Offset: 0x21688A4 VA: 0x216C8A4
  - [MATCH] dump.cs:177860: private static extern int DLL_DuelGetCardFace(int player, int position, int index) { }
  - [CONTEXT] dump.cs:177861: 
  - [CONTEXT] dump.cs:178342: // RVA: 0x2174648 Offset: 0x2170648 VA: 0x2174648
  - [MATCH] dump.cs:178343: public static bool GetCardFace(int player, int position, int index) { }
  - [CONTEXT] dump.cs:178344: 
- CHEATCARD: 1 matching dump.cs line(s); showing up to 3 context(s).
  - [CONTEXT] dump.cs:17605: public enum PvP.Command // TypeDefIndex: 392
  - [CONTEXT] dump.cs:17617: public const PvP.Command DBGCMD = 8;
  - [MATCH] dump.cs:17618: public const PvP.Command CHEATCARD = 9;
  - [CONTEXT] dump.cs:17619: public const PvP.Command CHAT = 10;
- PROCESS_DAMAGE: 4 matching dump.cs line(s); showing up to 3 context(s).
  - [CONTEXT] dump.cs:45022: public enum IDS_CARD // TypeDefIndex: 1146
  - [CONTEXT] dump.cs:45236: public const IDS_CARD PROCESS_NOISE3 = 210;
  - [MATCH] dump.cs:45237: public const IDS_CARD PROCESS_DAMAGE = 211;
  - [CONTEXT] dump.cs:45238: public const IDS_CARD PROCESS_DAMAGE1 = 212;
  - [CONTEXT] dump.cs:45239: public const IDS_CARD PROCESS_DAMAGE2 = 213;
  - [CONTEXT] dump.cs:45240: public const IDS_CARD PROCESS_DAMAGE3 = 214;
- Damage getter: 2 matching dump.cs line(s); showing up to 3 context(s).
  - [CONTEXT] dump.cs:177934: // RVA: 0x216D4F0 Offset: 0x21694F0 VA: 0x216D4F0
  - [MATCH] dump.cs:177935: private static extern int DLL_DuelGetDamageValue(int i) { }
  - [CONTEXT] dump.cs:177936: 
  - [CONTEXT] dump.cs:179041: // RVA: 0x2175D88 Offset: 0x2171D88 VA: 0x2175D88
  - [MATCH] dump.cs:179042: private static int PVP_DuelGetDamageValue(int index) { }
  - [CONTEXT] dump.cs:179043: 
- Damage positions: 14 matching dump.cs line(s); showing up to 3 context(s).
  - [CONTEXT] dump.cs:177928: // RVA: 0x216D414 Offset: 0x2169414 VA: 0x216D414
  - [MATCH] dump.cs:177929: private static extern int DLL_DuelGetDamageSrcPosition() { }
  - [CONTEXT] dump.cs:177930: 
  - [CONTEXT] dump.cs:177931: // RVA: 0x216D478 Offset: 0x2169478 VA: 0x216D478
  - [MATCH] dump.cs:177932: private static extern int DLL_DuelGetDamageDstPosition(int i) { }
  - [CONTEXT] dump.cs:177933: 
  - [CONTEXT] dump.cs:178408: // RVA: 0x2175B28 Offset: 0x2171B28 VA: 0x2175B28
  - [MATCH] dump.cs:178409: public static int GetDamageSrcPosition() { }
  - [CONTEXT] dump.cs:178410: 
- AutoPlay: 46 matching dump.cs line(s); showing up to 3 context(s).
  - [CONTEXT] dump.cs:70013: public class SettingsUtil // TypeDefIndex: 1307
  - [CONTEXT] dump.cs:70243: // RVA: 0x1BE94C0 Offset: 0x1BE54C0 VA: 0x1BE94C0
  - [MATCH] dump.cs:70244: private static bool GetAutoPlay() { }
  - [CONTEXT] dump.cs:70245: 
  - [CONTEXT] dump.cs:73609: public class ScenarioController // TypeDefIndex: 1442
  - [CONTEXT] dump.cs:73719: // RVA: 0x1C406C4 Offset: 0x1C3C6C4 VA: 0x1C406C4
  - [MATCH] dump.cs:73720: public void ChangeAutoPlay() { }
  - [CONTEXT] dump.cs:73721: 
  - [CONTEXT] dump.cs:73722: // RVA: 0x1C403A0 Offset: 0x1C3C3A0 VA: 0x1C403A0
  - [MATCH] dump.cs:73723: public void SetAutoPlay(bool active) { }
  - [CONTEXT] dump.cs:73724: 
- DuelMenu/AutoPlay settings: 20 matching dump.cs line(s); showing up to 3 context(s).
- Monster/status: 2 matching dump.cs line(s); showing up to 3 context(s).

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
- Interpretation of non-zero exit: the dumper generated all three output files, then failed in its final Console.ReadKey prompt because stdin was redirected; this is not a clean exit, but the generated dump outputs are present.
- Method names/type declarations recovered by Il2CppDumper are static metadata evidence; they do not prove a menu callback invokes the method or that behavior works at runtime.
- Integrity assessment: Container digest, embedded-member outer CRCs, and both inner APK CRC scans passed.
- Native library and metadata outputs are temporary; only this summary report is persisted.

