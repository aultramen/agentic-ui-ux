# Artifact and decision contract

All paths in this document are relative to the selected target repository, never the package installation directory or the repository's parent. Use the minimum structure needed:

```text
docs/ui-ux/
  README.md                     index of relevant work and shared design rules
  design-system/foundations.md   approved reusable rules, or links to existing source tokens
  work/<task-id>/
    brief.md
    references/                 sources and observations when needed
    styling/v001/               images and written visual decisions
    prototype/v001/             HTML, local assets/fixtures, run instructions
    approvals.md
    model-routing.md             phase configuration, execution permission and actual settings
    plan.md
    verification/               reports and actual evidence
```

Use a short, unique task ID (date plus descriptive slug works). Resume the matching task instead of creating duplicate folders. Create phase folders only as used. Small tasks may combine brief and plan; do not scaffold empty directories or demand every template field.

## Authority and approvals

The user's current scope and explicit decisions govern the work. Written business/API contracts govern behavior; exact tokens and interaction contracts live in text or existing source. Images show visual intent. HTML demonstrates information architecture and interaction intent. Neither proves production accessibility, performance or integration.

Record artifact path/revision, approved scope, decision, who approved and when or the conversation reference in `approvals.md`. Quote only actual decisions. The agent cannot approve on the user's behalf. Existing approval or authorization persists while applicable; do not repeatedly request it.

Keep execution configuration decisions in `model-routing.md` using [model routing](model-routing.md) and its [template](../templates/model-routing.md). It records recommended/actual model and effort, scope/output identity, rationale/estimates, approval provenance, reuse and execution blockers. Brief, plan and evidence link the decision ID instead of duplicating its state. Routing approval authorizes only the named phase; `not-required` is not user approval, and neither status grants visual/interaction approval or final acceptance. A routine source edit can require fresh verification without requiring unchanged model approval again.

Keep approved revisions unchanged. Create v002 for changes; compare against v001. A material change invalidates only affected approval decisions, dependent plan items and evidence. Preserve unaffected approvals. If image, HTML and written contract conflict in a way that affects the user, resolve that specific conflict before dependent implementation; do not silently pick a new authority.

Changing tokens used across the app requires reviewing affected consumers; local experiments do not automatically become the shared design system. Update foundations only when shared decisions are approved. Link to authoritative source tokens rather than maintaining competing token copies.

## Plan and evidence

Assign stable criterion IDs such as UX-01. Record criterion, related design revision, implementation slice, integration dependency and verification method. Criteria are observable outcomes rather than file-count or code-style tasks. Keep exclusions separate from accepted criteria. A scope change needs an explicit user decision and retained history; do not delete a failed criterion to claim 100%.

Evidence names the current source revision (commit plus dirty state, or a dated snapshot description), artifact revision, environment, viewport/container, state, command/action, observed result and any limitations. Re-run affected checks after relevant changes; unrelated valid evidence need not be repeated.

Criterion states: `unverified`, `verified`, `failed`, `blocked`. `not-applicable` is allowed only with a documented applicability reason; it must not hide a promised outcome. Accepted exclusions are out of scope and do not count as passed tests. No weighted beauty score or fabricated completion percentage.

Delivery states: `in-progress`, `blocked`, `ready-for-user-review`, `accepted/ready-to-commit`. Implementation can be verified before human acceptance, but cannot be described as user-approved until the user actually accepts. Preserve any acceptance already provided. Commit, push and publish follow the user's authorized scope.

## Handoff

Provide a verified preview URL or absolute file link, actual launch command and working directory where needed, sample-data disclosure, and a short path through the relevant flow. Explain a preview process's lifetime; a stopped server URL is not working access. Keep prototypes and references available without importing their experiment code into production. Never delete user material merely because it is called throwaway.
