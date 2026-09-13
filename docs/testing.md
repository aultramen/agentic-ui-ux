# Testing the framework

## Deterministic checks

From the package root, run:

```sh
python -m unittest discover -s tests -v
```

Python 3.10+ and standard library only. Installer tests use temporary source packages, projects and fake homes, not the real user configuration. Package tests verify discoverable names/descriptions, compact entrypoints, implicit Codex invocation metadata and references that remain valid after copying the six-skill bundle. Routing tests check that all six entrypoints link the shared policy and that the actual policy/template ship intact to both hosts, with valid installed links, no-write dry-run and idempotent reinstall. Phase timing, defaults and approval decisions require the separate behavioral evaluation below; file/link checks do not prove a model obeys the policy or switches at runtime.

Dry-run an actual destination before installing:

```sh
python scripts/install.py --scope project --platform both --project-dir /path/to/project --dry-run
```

Dry-run proves the proposed file operations/conflict checks, not that a host has loaded the skills.

## Agent behavior evaluation

Give a fresh evaluator the scenario text in `tests/behavior/scenarios.json` without the rubric, previous answers or implementation author's conclusions. First run without the framework. Record exact decisions. Then use a separate fresh evaluator with the installed `ui-ux` entrypoint and relevant linked references, running the same scenarios. Ask for next action, artifacts and completion status; for this decision exercise, prohibit actual app mutations and label outputs accordingly.

The original rubric is in `tests/behavior/rubric.md`. For 0.2.0, also evaluate [model-routing scenarios](../tests/behavior/model-routing-scenarios.json) against the separate [model-routing rubric](../tests/behavior/model-routing-rubric.md), keeping the rubric out of the evaluator's prompt. Use the same read-only constraints and ask for the proposed preflight, whether execution may start, and what would be recorded. Simulated decisions are not real user approvals.

For this upgrade's RED baseline, use committed 0.1.0 skill content; for GREEN, use a separate fresh evaluator with the new skill content and identical cases. Identify whether guidance was read from source or a temporary installation. Preserve exact answers and the tested source identity; do not read old answers into the new evaluator's context.

Cover all direct phase invocations and the router, `high`/supported `xhigh` planning defaults, seven preflight fields, contextual material impact, unchanged approval reuse, changed scope/model/effort/artifact, rejection without execution, and manual-switch waiting. Include an unknown effective effort requiring user attestation, a tool-managed image model, and unavailable price/time estimates. Check that model approval never becomes design or result acceptance.

Preserve actual baseline and forward responses for this release under `docs/verification/0.2.0/`; failures must lead to narrow guidance corrections and another fresh forward run. Do not rewrite a scenario to make the existing instructions pass. Distinguish new gains from behaviors the baseline already handled correctly.

These exercises test workflow choices under ambiguity, deadline, authority and sunk-cost pressure. They are not executed browser, accessibility or API tests, nor a statistical guarantee for every model.

## Native host smoke tests

Install into a temporary project using each platform adapter. Start a fresh host session with its normal skill discovery; no real global install is needed. Check:

1. The host lists/selects `ui-ux` from the temporary project's skill directory.
2. A natural-language frontend request routes to the framework, or record a missed automatic selection.
3. Explicit `$ui-ux` (Codex) or `/ui-ux` (Claude Code) loads the intended version and reads relevant references.
4. An unresolved greenfield request does not skip product decisions and both full-route design stages.
5. A backend-only request remains outside the frontend workflow.
6. Direct phase invocation and router dispatch both show the model/effort preflight at the required boundary before the dependent action.
7. Requested and effective settings are distinguished; unsupported automatic switching leaves the dependent phase waiting for manual switch/confirmation, and unavailable active-setting evidence is labeled user-attested if the user confirms it.

Use read-only/limited tools and isolated artifacts. Record host version, exact prompt, tool invocation evidence and observed output; never store credentials or debug headers. Missing authentication/capability is a smoke-test limitation, not an automatic pass. A single host pass proves that observed invocation, not future invocation reliability.

Report current results in [0.2.0 verification](verification/0.2.0/results.md). [Original results](verification/results.md) and [native host evidence](verification/native-hosts.md) describe 0.1.0 only: Codex invocation was observed there, while Claude execution was blocked by organization access. Neither proves new routing behavior. Do not overwrite that history or report a fresh native smoke pass unless it actually ran. A read-only decision exercise also does not prove an actual runtime model change; record that separately only when observed.

## Product validation remains separate

When a future project uses the framework, run that project's appropriate build, test, browser, responsive/container, accessibility and performance checks. This package's unit tests do not validate any downstream UI. Review source changes, then rerun only affected evidence unless the project's required suite says otherwise.
