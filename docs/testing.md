# Testing the framework

## Deterministic checks

From the package root, run:

```sh
python -m unittest discover -s tests -v
```

Python 3.10+ and standard library only. Installer tests use temporary source packages, projects and fake homes, not the real user configuration. Package tests verify discoverable names/descriptions, compact entrypoints, implicit Codex invocation metadata and references that remain valid after copying the six-skill bundle.

Dry-run an actual destination before installing:

```sh
python scripts/install.py --scope project --platform both --project-dir /path/to/project --dry-run
```

Dry-run proves the proposed file operations/conflict checks, not that a host has loaded the skills.

## Agent behavior evaluation

Give a fresh evaluator the scenario text in `tests/behavior/scenarios.json` without the rubric, previous answers or implementation author's conclusions. First run without the framework. Record exact decisions. Then use a separate fresh evaluator with the installed `ui-ux` entrypoint and relevant linked references, running the same scenarios. Ask for next action, artifacts and completion status; for this decision exercise, prohibit actual app mutations and label outputs accordingly.

The rubric is in `tests/behavior/rubric.md`. Preserve actual baseline and forward responses under `docs/verification/`; failures must lead to narrow guidance corrections and another fresh forward run. Do not rewrite a scenario to make the existing instructions pass. Distinguish new gains from behaviors the baseline already handled correctly.

These exercises test workflow choices under ambiguity, deadline, authority and sunk-cost pressure. They are not executed browser, accessibility or API tests, nor a statistical guarantee for every model.

## Native host smoke tests

Install into a temporary project using each platform adapter. Start a fresh host session with its normal skill discovery; no real global install is needed. Check:

1. The host lists/selects `ui-ux` from the temporary project's skill directory.
2. A natural-language frontend request routes to the framework, or record a missed automatic selection.
3. Explicit `$ui-ux` (Codex) or `/ui-ux` (Claude Code) loads the intended version and reads relevant references.
4. An unresolved greenfield request does not skip product decisions and both full-route design stages.
5. A backend-only request remains outside the frontend workflow.

Use read-only/limited tools and isolated artifacts. Record host version, exact prompt, tool invocation evidence and observed output; never store credentials or debug headers. Missing authentication/capability is a smoke-test limitation, not an automatic pass. A single host pass proves that observed invocation, not future invocation reliability.

## Product validation remains separate

When a future project uses the framework, run that project's appropriate build, test, browser, responsive/container, accessibility and performance checks. This package's unit tests do not validate any downstream UI. Review source changes, then rerun only affected evidence unless the project's required suite says otherwise.
