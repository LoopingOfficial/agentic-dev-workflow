# Security Policy

Agentic Dev Workflow can influence coding agents that read repositories, edit files, and run commands. Unsafe workflow instructions are therefore security-sensitive.

Do not publish credentials, exploit payloads, private repository content, or a working destructive prompt injection in a public issue.

If GitHub private vulnerability reporting is available, use it. Otherwise open a minimal issue requesting a private contact channel without including exploit details.

Please report issues involving secret exposure, destructive Git/filesystem behavior, unsafe prompt-injection handling, false claims that skipped tests passed, unsafe installer overwrites, path traversal, or instructions that weaken authentication or authorization.

Security fixes target the current `main` branch and the latest documented release line.
