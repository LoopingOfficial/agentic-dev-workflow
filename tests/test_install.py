from __future__ import annotations

import tempfile
from pathlib import Path
import unittest

from scripts.install import build_copy_plan, install

ROOT = Path(__file__).resolve().parents[1]


class InstallerTests(unittest.TestCase):
    def test_codex_install_creates_shared_workflows_and_skills(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            result = install("codex", target, root=ROOT)
            self.assertGreater(result["created"], 0)
            self.assertTrue((target / ".agentic-workflow/workflows/audit.md").is_file())
            self.assertTrue((target / ".agents/skills/adw-review/SKILL.md").is_file())

    def test_all_install_creates_every_provider(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            install("all", target, root=ROOT)
            self.assertTrue((target / ".agents/skills/adw-build/SKILL.md").is_file())
            self.assertTrue((target / ".claude/commands/build.md").is_file())
            self.assertTrue((target / ".opencode/commands/build.md").is_file())

    def test_identical_install_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            first = install("codex", target, root=ROOT)
            second = install("codex", target, root=ROOT)
            self.assertGreater(first["created"], 0)
            self.assertEqual(second["created"], 0)
            self.assertEqual(second["updated"], 0)
            self.assertGreater(second["unchanged"], 0)

    def test_different_existing_file_requires_force(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            path = target / ".agents/skills/adw-audit/SKILL.md"
            path.parent.mkdir(parents=True)
            path.write_text("local customization\n", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                install("codex", target, root=ROOT)
            install("codex", target, root=ROOT, force=True)
            self.assertIn("name: adw-audit", path.read_text(encoding="utf-8"))

    def test_dry_run_does_not_write(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            result = install("opencode", target, dry_run=True, root=ROOT)
            self.assertGreater(result["created"], 0)
            self.assertFalse((target / ".agentic-workflow").exists())
            self.assertFalse((target / ".opencode").exists())

    def test_copy_plan_has_unique_destinations(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            plan = build_copy_plan("all", Path(temp), root=ROOT)
            destinations = [item.destination for item in plan]
            self.assertEqual(len(destinations), len(set(destinations)))


if __name__ == "__main__":
    unittest.main()
