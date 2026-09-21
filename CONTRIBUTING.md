# Contributing

Contributions based on real usage are welcome.

Useful changes include reproducible workflow failures, provider compatibility fixes, clearer completion rules, installer portability fixes, tests for real regressions, and documentation improvements.

## Development

Use Python 3.10+ and run:

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

## Pull requests

Keep pull requests focused and explain the concrete problem first.

Before submitting:

- keep provider-neutral logic in `shared/`;
- update tests when installer behavior changes;
- update the changelog for user-visible behavior;
- do not commit credentials, private project state, or generated state from another repository;
- preserve backward compatibility unless a breaking change is intentional and documented.

## Provider adapters

Adapters should be thin. A provider adapter may define discovery metadata, invocation syntax, or argument passing, but workflow behavior belongs in `shared/workflows/`.

## License

By contributing, you agree that your contribution may be distributed under the MIT license.
