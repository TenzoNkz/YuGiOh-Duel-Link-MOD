#!/usr/bin/env python3
"""Validate that chatgpt-mod is a buildable Android Gradle project labelled CHATGPT Mod.

This is a source/project preflight only. It does not download, execute, patch,
or redistribute the proprietary game Release APK.
"""
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ANDROID_NS = "{http://schemas.android.com/apk/res/android}"


def resolve_app_label(project_dir: Path) -> tuple[str | None, str]:
    manifest = project_dir / "app" / "src" / "main" / "AndroidManifest.xml"
    if not manifest.is_file():
        return None, f"Android manifest not found: {manifest}"

    try:
        root = ET.parse(manifest).getroot()
    except (ET.ParseError, OSError) as exc:
        return None, f"Could not parse AndroidManifest.xml: {type(exc).__name__}: {exc}"

    application = root.find("application")
    if application is None:
        return None, "AndroidManifest.xml does not contain an <application> element."

    label = application.get(ANDROID_NS + "label")
    if not label:
        return None, "The <application> element has no android:label."

    if not label.startswith("@string/"):
        return label, ""

    resource_name = label.split("/", 1)[1]
    values_dir = project_dir / "app" / "src" / "main" / "res"
    for values_file in sorted(values_dir.glob("values*/strings.xml")):
        try:
            resources = ET.parse(values_file).getroot()
        except (ET.ParseError, OSError):
            continue
        for item in resources.findall("string"):
            if item.get("name") == resource_name:
                return "".join(item.itertext()).strip(), ""

    return None, f"Could not resolve {label} from app/src/main/res/values*/strings.xml."


def validate(project_dir: Path, required_label: str) -> list[str]:
    issues: list[str] = []
    if not project_dir.is_dir():
        return [f"Source project directory does not exist: {project_dir}"]

    wrapper = project_dir / "gradlew"
    if not wrapper.is_file():
        issues.append(f"Gradle wrapper is missing: {wrapper}")
    if not (project_dir / "settings.gradle").is_file() and not (project_dir / "settings.gradle.kts").is_file():
        issues.append("Project needs settings.gradle or settings.gradle.kts.")
    if not (project_dir / "gradle" / "wrapper" / "gradle-wrapper.properties").is_file():
        issues.append("Gradle wrapper configuration is missing: gradle/wrapper/gradle-wrapper.properties.")
    if not (project_dir / "app" / "build.gradle").is_file() and not (project_dir / "app" / "build.gradle.kts").is_file():
        issues.append("Android app module needs app/build.gradle or app/build.gradle.kts.")

    label, label_error = resolve_app_label(project_dir)
    if label_error:
        issues.append(label_error)
    elif label != required_label:
        issues.append(f"App label must be exactly {required_label!r}; resolved label is {label!r}.")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-dir", default="chatgpt-mod")
    parser.add_argument("--required-label", default="CHATGPT Mod")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    issues = validate(project_dir, args.required_label)
    if issues:
        print("CHATGPT Mod source preflight: BLOCKED")
        for issue in issues:
            print(f"- {issue}")
        return 2

    print("CHATGPT Mod source preflight: PASS")
    print(f"- Project directory: {project_dir}")
    print(f"- Required Android application label: {args.required_label}")
    print("- Gradle wrapper, app module, and manifest are present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
