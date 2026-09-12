---
name: ui-ux-build
description: "Use when implementing a scoped web/webview UI plan with applicable design approvals or an audited baseline and concrete acceptance criteria."
---

# Implement the agreed interface

Read the brief, plan, approval revisions and latest evidence. Check their scope and freshness even when this skill is invoked directly. If the plan is missing or materially undecided, return to [planning](../ui-ux-plan/SKILL.md); do not invent a production design while coding.

## Execute

1. Follow the plan's dependency order, completing one demonstrable user task at a time. Use existing stack, components, tokens and test seams; no mandatory frontend library or state-machine dependency.
2. Apply the [quality contract](../ui-ux/references/quality-contract.md). Preserve business invariants and legitimate differences across similar flows. Prefer explicit domain operations over a universal component that hides permission or payload differences.
3. Add meaningful regression tests for changed behavior before implementing that behavior when the project's workflow supports it. Use proportional verification for reversible cosmetic changes; do not manufacture tests that mirror CSS or implementation details.
4. Integrate observed real APIs when promised. Dummy fixtures remain confined to prototyping or explicitly frontend-only scope. Never import throwaway experiment code automatically into production or claim mocks prove real integration.
5. Keep acceptance status and evidence aligned with actual progress. `verified` requires a current check, not a completed code edit. Preserve approved design revisions; route material departures back to the affected design decision and reconcile dependent plan items.

## Verify and continue

Run relevant project checks, then hand the implementation and raw requirements to [review](../ui-ux-review/SKILL.md). Fix actionable gaps within scope and rerun affected checks. Do not repeat unrelated passing checks without a reason. Use [artifact/evidence rules](../ui-ux/references/artifacts.md) and the [verification template](../ui-ux/templates/verification.md).

If an endpoint, tool, user decision or other prerequisite is unavailable, complete independent authorized work and record the exact blocker and reproducible next step. Follow [capability fallbacks](../ui-ux/references/capabilities.md); repeated attempts and deadlines do not change evidence status.

Provide a working preview or absolute file link, launch instructions, data-source disclosure and steps to inspect the changed flow. Distinguish implementation verified, ready for user review, and accepted/ready to commit. Honor acceptance already provided; do not ask again without a relevant change. Commit, push and publish only within the user's authorized scope.
