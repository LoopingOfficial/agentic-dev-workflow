#!/usr/bin/env python3
"""Install Agentic Dev Workflow adapters into a target repository."""

from __future__ import annotations

import argparse
import filecmp
import json
from dataclasses import dataclass
from pathlib import Path
import shutil
import sys
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class CopyItem:
    source: Path
    destination: Path


def load_manifest(root: Path = REPO_ROOT) -> dict:
    with (root / "manifest.json").open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _expand_mapping(root: Path, target: Path, mapping: dict) -> list[CopyItem]:
    source = root / mapping["source"]
    destination = target / mapping["destination"]

    if source.is_file():
        return [CopyItem(source, destination)]
    if not source.is_dir():
        raise FileNotFoundError(f"Manifest source does not exist: {source}")

    return [
        CopyItem(path, destination / path.relative_to(source))
        for path in sorted(p for p in source.rglob("*") if p.is_file())
    ]


def build_copy_plan(provider: str, target: Path, root: Path = REPO_ROOT) -> list[CopyItem]:
    manifest = load_manifest(root)
    providers = manifest["providers"]

    if provider != "all" and provider not in providers:
        raise ValueError(f"Unknown provider: {provider}")

    mappings = list(manifest["shared"])
    selected = providers.keys() if provider == "all" else [provider]
    for name in selected:
        mappings.extend(providers[name])

    items: list[CopyItem] = []
    for mapping in mappings:
        items.extend(_expand_mapping(root, target, mapping))

    destinations = [item.destination for item in items]
    if len(destinations) != len(set(destinations)):
        raise ValueError("Manifest contains duplicate destination paths")
    return items


def _same_file(source: Path, destination: Path) -> bool:
    return destination.is_file() and filecmp.cmp(source, destination, shallow=False)


def install(
    provider: str,
    target: Path,
    *,
    force: bool = False,
    dry_run: bool = False,
    root: Path = REPO_ROOT,
) -> dict[str, int]:
    target = target.expanduser().resolve()
    plan = build_copy_plan(provider, target, root)

    collisions = [
        item for item in plan
        if item.destination.exists() and not _same_file(item.source, item.destination)
    ]
    if collisions and not force:
        formatted = "\n".join(
            f"  - {item.destination.relative_to(target)}" for item in collisions
        )
        raise FileExistsError(
            "Refusing to overwrite existing files. Re-run with --force only after "
            f"reviewing these paths:\n{formatted}"
        )

    result = {"created": 0, "updated": 0, "unchanged": 0}
    for item in plan:
        exists = item.destination.exists()
        if exists and _same_file(item.source, item.destination):
            result["unchanged"] += 1
            continue

        result["updated" if exists else "created"] += 1
        if dry_run:
            continue

        item.destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item.source, item.destination)

    return result


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    providers = sorted(load_manifest()["providers"].keys())
    parser = argparse.ArgumentParser(description="Install Agentic Dev Workflow.")
    parser.add_argument("--provider", required=True, choices=providers + ["all"])
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)

    if not args.target.exists() or not args.target.is_dir():
        print(f"Target must be an existing directory: {args.target}", file=sys.stderr)
        return 2

    try:
        result = install(
            args.provider,
            args.target,
            force=args.force,
            dry_run=args.dry_run,
        )
    except (FileExistsError, FileNotFoundError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    action = "Would install" if args.dry_run else "Installed"
    print(
        f"{action} provider={args.provider}: "
        f"{result['created']} created, "
        f"{result['updated']} updated, "
        f"{result['unchanged']} unchanged."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
