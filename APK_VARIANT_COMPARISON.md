# APKPure Original vs Platinmods — Static Variant Comparison

**Status:** PENDING_ANALYSIS  
**Canonical repository:** TenzoNkz/YuGiOh-Duel-Link-MOD  
**Mod base:** APKPure Original Release tag `APKPure_Latest`  
**Reference only:** Platinmods Release tag `Latest`

This file is a placeholder until the GitHub Actions workflow runs the new APK/XAPK-aware comparison tool. No V11.1.0 binary comparison is claimed yet.

## Required outputs
- Validate each downloaded Release container against the GitHub-provided SHA-256 when present.
- Detect and inventory the APKPure XAPK's embedded APK files and OBB payloads.
- Select the likely primary APK safely and record its SHA-256 separately from the XAPK container.
- Compare primary APK ZIP entry names, sizes, and SHA-256 values with the Platinmods APK.
- Highlight manifest, DEX, native library, and Unity IL2CPP metadata differences for further analysis.
- Keep APKPure as the sole intended modification base; Platinmods is comparison evidence only.

## Current interpretation
- No mod feature is claimed as working based solely on archive differences or strings.
- APK v2/v3 certificate identity is not established by this report until an APK signature verification tool is integrated and its output is recorded.
- The XAPK may include split APKs or OBB files; producing a single APK requires a separate compatibility decision and testing.
