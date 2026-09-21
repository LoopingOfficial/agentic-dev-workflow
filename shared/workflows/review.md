# Review workflow

## Goal

Evaluate whether the implementation satisfies accepted requirements without avoidable regressions or security problems.

## Rules

- Review the actual diff and relevant surrounding code.
- Read the accepted specification and test report when present.
- Findings come before praise or summary.
- Do not report stylistic preferences as defects unless the repository defines them as requirements.
- A missing or skipped test is a validation gap, not a passing result.
- Do not modify implementation files unless the user explicitly asks for review-and-fix.

## Process

1. Determine review scope from the current diff or user target.
2. Map accepted requirements to implemented behavior.
3. Inspect correctness, edge cases, security, regressions, compatibility, and maintainability.
4. Check validation evidence and important checks that were not run.
5. Report findings in severity order with repository-relative references.
6. Record coverage and residual risk.
7. Write `.agentic-workflow/state/review.md`.

Each finding should include severity, affected area, concrete behavior/risk, why it matters, and focused remediation. End with PASS or NEEDS CHANGES.
