# Agentic Dev Workflow

A provider-neutral, file-driven development workflow with first-class adapters for **Codex**, **Claude Code**, and **OpenCode**.

The project turns a coding-agent session into a traceable workflow:

```text
audit → spec → architect? → build → review
```

Each phase writes durable state under `.agentic-workflow/state/`, so decisions, validation results, and review findings survive context changes and can be inspected by humans or another agent.

> Independent open-source project. Not affiliated with or endorsed by OpenAI, Anthropic, or OpenCode.

## Why this exists

Coding agents are good at implementation, but long tasks become harder to trust when requirements, decisions, tests, and review findings only live in chat history.

Agentic Dev Workflow keeps those steps explicit:

- **audit** maps the real codebase before changes;
- **spec** turns the request into verifiable requirements;
- **architect** records structural decisions only when they are actually needed;
- **build** implements the smallest complete change and records validation;
- **review** checks the result against the specification and evidence.

The workflow core is provider-neutral. Provider adapters only translate invocation and discovery conventions.

## Supported adapters

| Provider | Native integration | Installed location |
| --- | --- | --- |
| Codex | Agent Skills | `.agents/skills/adw-*/SKILL.md` |
| Claude Code | Project commands | `.claude/commands/*.md` |
| OpenCode | Custom commands | `.opencode/commands/*.md` |

Codex is the reference adapter. Its workflows use the current Agent Skills format and keep each skill intentionally small: the skill routes to a provider-neutral workflow instead of duplicating large prompts.

## State contract

Installed projects use:

```text
.agentic-workflow/
├── STATE_CONTRACT.md
├── workflows/
│   ├── audit.md
│   ├── spec.md
│   ├── architect.md
│   ├── build.md
│   └── review.md
└── state/
    ├── audit.md
    ├── spec.md
    ├── architecture.md
    ├── test-report.md
    └── review.md
```

Generated state is intentionally separate from the workflow definitions.

## Install

Requirements: Python 3.10+.

```bash
python scripts/install.py --provider codex --target /path/to/project
python scripts/install.py --provider claude --target /path/to/project
python scripts/install.py --provider opencode --target /path/to/project
```

Install all adapters:

```bash
python scripts/install.py --provider all --target /path/to/project
```

Preview without writing:

```bash
python scripts/install.py --provider codex --target /path/to/project --dry-run
```

Existing files are never overwritten unless `--force` is supplied. Identical files are left untouched.

### Windows

```powershell
py scripts\install.py --provider codex --target "C:\path\to\project"
```

### macOS / Linux

```bash
python3 scripts/install.py --provider codex --target ~/src/my-project
```

## Codex

The Codex adapter installs Agent Skills:

```text
$adw-audit
$adw-spec
$adw-architect
$adw-build
$adw-review
```

Example:

```text
Use $adw-audit to map this repository before we change the authentication flow.
```

## Claude Code

The Claude adapter installs thin project commands under `.claude/commands/`:

```text
/audit
/spec
/architect
/build
/review
```

## OpenCode

The OpenCode adapter installs project commands under `.opencode/commands/` with the same phase names.

## Validate this repository

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

CI runs both checks on Linux, Windows, and macOS.

## Design principles

1. Investigate before editing.
2. Preserve unrelated user work.
3. Keep requirements, decisions, tests, and findings inspectable.
4. Never report a skipped check as passing.
5. Keep provider-specific behavior out of the shared workflow.
6. Keep adapters small and discoverable.
7. Build the smallest complete solution that satisfies the accepted spec.

## Project status

**v0.1.0** establishes the workflow contract, three provider adapters, installer, validation, tests, and CI.

This is an early-stage project. Feedback based on real use is especially useful.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security-sensitive reports should follow [SECURITY.md](SECURITY.md).

## License

MIT — see [LICENSE](LICENSE).
