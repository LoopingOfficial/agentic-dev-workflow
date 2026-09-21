# Audit workflow

## Goal

Establish the repository's real current state before proposing or making changes.

## Rules

- Treat the current user request as the task boundary.
- Read relevant files before making claims about them.
- Do not edit product code, configuration, dependencies, or generated assets during audit.
- Do not run destructive commands.
- Inspect version-control status before reasoning about a diff so unrelated user work is not mistaken for task work.
- Prefer direct evidence from code, configuration, tests, schemas, and build files.
- Record uncertainty instead of guessing.

## Process

1. Restate the concrete audit scope briefly.
2. Inspect repository structure and version-control status.
3. Locate entry points, modules, configuration, tests, and data boundaries relevant to the request.
4. Trace current behavior far enough to answer the task.
5. Identify constraints, security-sensitive areas, tests, and regression surfaces.
6. Record only unresolved questions that materially block a later phase.
7. Write `.agentic-workflow/state/audit.md`.

The audit file must include scope, relevant files/components, current behavior, constraints/risks, discovered validation commands, unresolved questions, and repository-relative evidence. End by stating whether the repository is sufficiently understood to continue.
