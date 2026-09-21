#!/usr/bin/env python3
"""Static validation for Agentic Dev Workflow."""

from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ["audit", "spec", "architect", "build", "review"]
PROVIDERS = ["codex", "claude", "opencode"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate() -> list[str]:
    errors: list[str] = []
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CHANGELOG.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
        ROOT / "manifest.json",
        ROOT / "shared" / "STATE_CONTRACT.md",
    ]

    for path in required:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")
        elif not read(path).strip():
            errors.append(f"empty required file: {path.relative_to(ROOT)}")

    try:
        manifest = json.loads(read(ROOT / "manifest.json"))
    except Exception as exc:
        errors.append(f"manifest.json is invalid: {exc}")
        return errors

    if manifest.get("workflows") != WORKFLOWS:
        errors.append("manifest workflows do not match expected workflow set")
    if sorted(manifest.get("providers", {}).keys()) != sorted(PROVIDERS):
        errors.append("manifest providers must be codex, claude, and opencode")

    for name in WORKFLOWS:
        core = ROOT / "shared" / "workflows" / f"{name}.md"
        if not core.is_file():
            errors.append(f"missing shared workflow: {core.relative_to(ROOT)}")
            continue

        text = read(core)
        if len(text.strip()) < 300:
            errors.append(f"shared workflow unexpectedly short: {core.relative_to(ROOT)}")
        if re.search(r"\b(Codex|Claude|OpenCode)\b", text, flags=re.IGNORECASE):
            errors.append(
                f"provider-specific name leaked into shared workflow: {core.relative_to(ROOT)}"
            )

        skill = ROOT / "adapters" / "codex" / "skills" / f"adw-{name}" / "SKILL.md"
        if not skill.is_file():
            errors.append(f"missing Codex skill: {skill.relative_to(ROOT)}")
        else:
            skill_text = read(skill)
            if not skill_text.startswith("---\n"):
                errors.append(f"Codex skill missing frontmatter: {skill.relative_to(ROOT)}")
            if f"name: adw-{name}" not in skill_text:
                errors.append(f"Codex skill has wrong name: {skill.relative_to(ROOT)}")
            if "description:" not in skill_text:
                errors.append(f"Codex skill missing description: {skill.relative_to(ROOT)}")

        claude = ROOT / "adapters" / "claude" / "commands" / f"{name}.md"
        if not claude.is_file() or len(read(claude).strip()) < 80:
            errors.append(f"missing/short Claude adapter: {claude.relative_to(ROOT)}")

        opencode = ROOT / "adapters" / "opencode" / "commands" / f"{name}.md"
        if not opencode.is_file():
            errors.append(f"missing OpenCode adapter: {opencode.relative_to(ROOT)}")
        else:
            opencode_text = read(opencode)
            if not opencode_text.startswith("---\n") or "description:" not in opencode_text:
                errors.append(f"OpenCode adapter missing frontmatter: {opencode.relative_to(ROOT)}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f" - {error}")
        return 1
    print("Repository validation passed: 5 workflows across 3 provider adapters.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
