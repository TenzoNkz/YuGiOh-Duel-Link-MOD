# CHATGPT MOD Build Report

**Status:** BLOCKED_APKPURE_SOURCE_INTEGRITY  
**Last updated:** 2026-10-27  
**Canonical repository:** TenzoNkz/YuGiOh-Duel-Link-MOD  
**Mod base:** APKPure Original V11.1.0 — Release tag APKPure_Latest  
**Comparison-only reference:** Platinmods V11.1.0 — Release tag Latest  
**Required in-game menu title:** CHATGPT MOD  
**Expected output:** verified modified APK (.apk)

## Actual analysis state
- APKPure XAPK size: 92,726,986 bytes. Its calculated SHA-256 matches GitHub metadata: 1f2cf45f87f52217227611b1d48f83a1d3990c326a0b2a6c64fa54296237be16.
- Embedded members: jp.konami.duellinks.apk (55,854,706 bytes) and config.arm64_v8a.apk (36,869,159 bytes). No OBB payload was identified.
- Both embedded APK outer-member CRC checks fail.
- The primary APK includes a decompression/CRC failure at assets/bin/Data/e1f73dc34613ec042897cc46749d448c.
- The ARM64 split's lib/arm64-v8a/libduel.so fails the APK CRC check.
- APKPure/Platinmods comparison is partial: the ARM64 libil2cpp.so and global-metadata.dat entries hash identically, but the corrupted libduel.so cannot be compared reliably. Manifest and DEX files differ at byte level.
- Static code analysis remains partial. Strings and method names do not prove feature wiring or runtime behavior.
- No CHATGPT MOD APK has been built, signed, installed or runtime-tested.

## Hard build blocker
The downloaded XAPK's container SHA-256 matches the checksum recorded by GitHub, but its embedded APK content is internally invalid. This is not a successful source-integrity check for patching; it means the uploaded asset itself needs to be replaced with a clean original package. Do not patch/build from this XAPK.

## Required preconditions
1. Replace the current APKPure XAPK with a clean source package and confirm container/member CRC checks pass.
2. Rerun APK Static Analysis, APK Code Analysis, package comparison and IL2CPP metadata recovery on the clean asset.
3. Review MOD_CANDIDATES.md and approve one bounded, safe feature scope.
4. Determine whether the XAPK can be combined into a valid single APK without breaking native ABI/package requirements.
5. Implement a real APKPure-based patch/build tool; do not use a standalone Gradle demo or simply rename/extract a file.
6. Verify package name, version, signing certificate and installation behavior before promising that the mod can overwrite Platinmods.
7. Build and upload the output artifact; record its size, SHA-256, signer check, Action URL and actual test results.

## Signature limitation
A public certificate is not the private signing key. Unless the required Platinmods private key or a valid certificate rotation chain is available, an APK signed with our own key cannot be assumed to update an installed Platinmods version. A separate uninstall/reinstall may be required and could affect app-local data.

## Scope
Safe local UI/accessibility/settings and compatibility changes, plus offline simulations, may be considered. Features designed to unfairly alter live-online-duel outcomes are excluded. A successful archive or packaging step is not proof that a gameplay feature works.

## NEXT ACTION
Obtain and upload a clean APKPure Original package. Do not run the final build workflow until source integrity and reverse-engineering preconditions pass.
