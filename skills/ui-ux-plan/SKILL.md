---
name: ui-ux-plan
description: "Use when approved web/webview designs or an audited baseline need an implementation plan with acceptance criteria, API dependencies and verification methods."
---

# Plan the production UI

Turn settled design decisions into observable implementation work. This phase produces a Markdown plan, not production code. Preserve the user's scope and existing authorization.

## Inputs

Read the task brief, applicable baseline, approval records and current implementation. For new/material UI, check visual and interactive approvals against the exact artifacts and scope. Missing approval routes to [style](../ui-ux-style/SKILL.md) or [prototype](../ui-ux-prototype/SKILL.md); do not finalize a production plan around an unchosen direction. A small correction can use an audited baseline without new mockups.

Read the shared [artifact contract](../ui-ux/references/artifacts.md) and apply the relevant [quality criteria](../ui-ux/references/quality-contract.md). Use the [plan template](../ui-ux/templates/plan.md), trimming fields unrelated to the task.

## Plan

Before drafting, apply [model routing](../ui-ux/references/model-routing.md): select an available reasoning-capable model at high by default, xhigh for substantial complexity. Present the choice, resolve material-impact approval, establish actual settings and record/reuse the decision. Lower effort requires explicit user choice, even for a short plan. Routing approval does not approve the plan.

1. Define stable acceptance IDs for user-visible outcomes, with design/behavior references and verification methods. Include affected pages, relevant states and supported container sizes.
2. Inspect the actual stack and integration seams. Reuse tokens/components and preserve domain-specific guards, validation, payloads and transitions. Record API contracts from evidence, not guessed endpoints.
3. Distinguish frontend-only mock scope from promised production integration. Mark missing contracts/endpoints as dependencies; identify independent work that can proceed.
4. Order demoable slices by dependency, covering complete user tasks rather than separating all styling from all integration. Each slice points to its acceptance IDs. Keep a small fix to a short plan.
5. Specify tests/checks proportional to risk, browser/manual evidence, preview access and relevant performance conditions. Existing project checks remain applicable; do not add an unnecessary testing framework for a cosmetic fix.
6. Save under the task's `docs/ui-ux/work/<task-id>/plan.md`. Retain scope changes and unresolved dependencies; never silently drop a criterion to call the plan complete.

## Exit

The plan is ready when every agreed outcome has an implementation slice, dependencies and a concrete verification method, with no unresolved material design choice. Do not insert an extra approval gate if the user already authorized implementation; obey any explicit plan-only request or platform planning mode.

Hand off to [build](../ui-ux-build/SKILL.md) with the brief, current approved revisions, plan and next dependency-ready slice. Resume existing work instead of duplicating plans.
