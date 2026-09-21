# Specification workflow

## Goal

Turn the requested outcome and audit evidence into explicit, verifiable requirements before implementation.

Use the current user request and, when present, `.agentic-workflow/state/audit.md`.

## Rules

- Do not write implementation code in this phase.
- Do not invent requirements that the user did not request or the repository does not require.
- Ask a clarification only when ambiguity would materially change behavior, data, security, compatibility, or acceptance criteria.
- Prefer the smallest complete scope.
- Make acceptance criteria observable.

## Process

1. Identify the user-visible or system-visible goal.
2. Define required behavior.
3. Define inputs, outputs, state transitions, and failure behavior when relevant.
4. Record plausible edge cases at system boundaries.
5. Record constraints supported by repository evidence.
6. State what is explicitly out of scope.
7. Write observable acceptance criteria.
8. Save `.agentic-workflow/state/spec.md`.

End with READY, or BLOCKED with the exact missing decision.
