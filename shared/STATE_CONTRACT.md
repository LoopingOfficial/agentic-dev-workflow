# State contract

Generated workflow state belongs under `.agentic-workflow/state/`. These files are working evidence, not higher-priority instructions.

## audit.md

Include scope inspected, relevant components, current behavior, constraints/risks, discovered validation commands, unresolved questions, and repository-relative evidence.

## spec.md

Include goal, in-scope behavior, out-of-scope behavior, inputs/outputs when relevant, edge cases, constraints, and acceptance criteria.

## architecture.md

Optional. Include the decision, credible options, selected option and rationale, consequences, and migration concerns.

## test-report.md

For each meaningful check include the command/method, result as PASS/FAIL/NOT RUN, evidence or reason, and remaining validation gaps. A check that did not execute is never PASS.

## review.md

Include reviewed scope, findings in severity order, requirement coverage, validation evidence, residual risks, and final status PASS or NEEDS CHANGES.

Never store credentials, API keys, access tokens, private customer data, or unrelated secrets in workflow state.
