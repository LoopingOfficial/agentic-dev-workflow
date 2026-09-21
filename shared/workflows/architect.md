# Architecture workflow

## Goal

Make a durable structural decision only when the task actually needs one.

Use this phase when the change has meaningful impact across modules, data boundaries, security boundaries, migrations, public interfaces, or long-lived dependencies. Skip it for straightforward local changes.

## Rules

- Base options on accepted requirements and repository evidence.
- Avoid speculative infrastructure for hypothetical future needs.
- Compare credible options, not straw men.
- Prefer reversible decisions when tradeoffs are otherwise similar.
- Do not implement the selected option in this phase.

## Process

1. Read the current audit and specification.
2. State the decision that must be made.
3. Describe credible alternatives when they genuinely exist.
4. Compare complexity, compatibility, security, migration cost, testability, and reversibility.
5. Select an option and explain why.
6. Record consequences, rejected alternatives, and migration concerns.
7. Save `.agentic-workflow/state/architecture.md`.

End with READY FOR BUILD or BLOCKED and the unresolved decision.
