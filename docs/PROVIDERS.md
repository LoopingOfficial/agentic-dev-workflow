# Provider adapters

The workflow core is independent of any coding-agent vendor.

## Codex

The Codex adapter uses Agent Skills and installs five skills into `.agents/skills/adw-<phase>/SKILL.md`. Each skill has a narrow routing description and delegates detailed behavior to the shared workflow.

## Claude Code

The Claude adapter installs thin project command files under `.claude/commands/`. Each command delegates to the same shared workflow.

## OpenCode

The OpenCode adapter uses Markdown custom commands under `.opencode/commands/` and passes `$ARGUMENTS` as optional user context.

## Adding another provider

A new adapter should use the provider's documented native discovery mechanism, remain thin, route to the shared workflows, be added to `manifest.json`, and include validation/tests for installer behavior.
