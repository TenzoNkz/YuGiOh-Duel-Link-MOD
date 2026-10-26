# APK Static Analysis Report

**Status:** PENDING_AUTOMATED_ANALYSIS  
**Checkpoint date:** 2026-10-26  
**Source of truth:** public GitHub Release metadata. This file is a bootstrap checkpoint, not a claim that the APK has already been inspected.

## Release metadata verified
- Repository: TenzoNkz/YuGiOh-Duel-Link-MOD
- Release: https://github.com/TenzoNkz/YuGiOh-Duel-Link-MOD/releases/tag/Platinmods_V11.0.0
- Release title: Platinmods Original
- Tag: Platinmods_V11.0.0
- Asset: Yu-Gi-Oh.Duel.Links.Platinmods.V11.0.0.apk
- GitHub-reported size: 127,424,878 bytes (about 121.5 MiB)
- GitHub-reported SHA-256: d7855754afbfe8e6b0a5db51ba47e4cefcd3079631190c11478d6556e06c56fb

## Not yet verified by a workflow run
- Downloaded bytes and actual SHA-256 comparison.
- ZIP/APK central-directory integrity and CRC scan.
- AndroidManifest.xml decoding, package ID, min/target SDK, version fields, and signing-certificate validation.
- DEX inventory, native library inventory, engine indicators, and code-level feature tracing.
- Whether any candidate modification is feasible or works.

## Required next step
Run the GitHub Actions workflow named APK Static Analysis. It should replace this bootstrap report with its measured inventory. Review the new report and workflow run result before making claims about the APK contents.

## Analysis limits
The first stage treats the APK as data and does not execute it. A successful inventory is not a complete reverse-engineering result and does not prove any in-game feature works.
