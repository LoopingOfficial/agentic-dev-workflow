# Codex adapter

The Codex adapter uses Agent Skills.

Install with:

```bash
python scripts/install.py --provider codex --target /path/to/project
```

The installer places skills under `.agents/skills/` and shared workflows under `.agentic-workflow/`.

Invoke skills explicitly with names such as `$adw-audit` or `$adw-review`, or let Codex select a skill when the request matches its description.
