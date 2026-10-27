# APKPure IL2CPP Analysis

**Status:** PENDING_ANALYSIS  
**Canonical mod base:** APKPure Original V11.1.0 — Release tag APKPure_Latest  
**Tool:** Perfare Il2CppDumper v6.7.46 (pinned)

This placeholder is replaced by the APK Code Analysis workflow. No IL2CPP dump result is claimed until the tool runs and the generated report is reviewed.

## Intended analysis
- Extract the ARM64 libil2cpp.so from APKPure's config.arm64_v8a.apk split.
- Extract assets/bin/Data/Managed/Metadata/global-metadata.dat from the APKPure primary APK.
- Run a pinned metadata recovery tool in a temporary workspace.
- Persist only a short report with hashes, focused class/method context, tool result and limitations; do not commit full decompiler output or app binaries.

## Integrity warning
The current APKPure XAPK has known CRC/decompression failures in the primary APK and ARM64 split. Even if metadata recovery succeeds, it does not make the uploaded package valid for patch/build. The asset should be replaced with a clean original package before implementation or packaging.
