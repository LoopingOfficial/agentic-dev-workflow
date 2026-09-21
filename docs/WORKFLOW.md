# Workflow model

Agentic Dev Workflow separates software work into five phases. The phases are not a rigid waterfall: `architect` is optional, and a small bug fix may already have enough requirements to move from audit to build.

## Audit

Establish what is actually present before making claims or edits.

Output: `.agentic-workflow/state/audit.md`.

## Spec

Turn the requested outcome into explicit, testable requirements.

Output: `.agentic-workflow/state/spec.md`.

## Architect (optional)

Record durable structural decisions when multiple credible designs exist or the change has broad dependency, security, data, public-interface, or migration impact.

Output: `.agentic-workflow/state/architecture.md`.

## Build

Implement the accepted requirements while preserving unrelated user work.

Output: code changes plus `.agentic-workflow/state/test-report.md`.

## Review

Compare the implementation with accepted requirements and evidence.

Output: `.agentic-workflow/state/review.md`.

## State is evidence, not authority

Generated state can become stale. The current repository and current user request remain authoritative. When state conflicts with current code, investigate and update state rather than forcing code to match obsolete notes.
