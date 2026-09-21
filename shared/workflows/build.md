# Build workflow

## Goal

Implement accepted requirements with the smallest complete change and verifiable evidence.

Read current audit, specification, and architecture state when present. The current user request and current repository remain authoritative if state is stale.

## Safety rules

- Inspect version-control status before editing.
- Preserve unrelated user changes.
- Never discard, reset, overwrite, or rewrite unrelated work to make the task easier.
- Do not weaken tests, authentication, authorization, validation, or security controls merely to obtain a passing result.
- Do not claim a check passed unless it actually ran and succeeded.
- Avoid new dependencies unless necessary for accepted scope.

## Process

1. Confirm requirements and relevant existing behavior.
2. Inspect the exact files to change.
3. Implement the smallest complete solution.
4. Run the most relevant available syntax, lint, unit, integration, build, or type checks.
5. Investigate failures caused by the change; do not hide them.
6. Re-read the diff for accidental scope expansion and sensitive data.
7. Write `.agentic-workflow/state/test-report.md`.

For every meaningful check record command/method, PASS/FAIL/NOT RUN, concise evidence, and the reason for NOT RUN. End with IMPLEMENTED, PARTIAL, or BLOCKED.
