---
name: ui-ux-style
description: "Use when new or materially changed web/webview UI or workflows need a visual direction, when styling exploration is requested, or when an approved visual direction has changed."
---

# UI/UX Style

Produce a concrete visual direction before interactive prototyping. This stage approves visual intent; it does not establish working behavior or production correctness.

## Start from the brief

Read the current brief, existing design foundations, and applicable approval records under `docs/ui-ux/`. If user goals, scope, or the chosen workflow are unresolved, return to [discovery](../ui-ux/references/discovery.md) through [ui-ux](../ui-ux/SKILL.md). A generic dashboard is not a substitute for unresolved product decisions.

For new UI, material redesign, or materially changed workflows, the sequence is **image → visual approval → interactive HTML → interaction approval → production plan**. An existing image explicitly approved for the current scope can satisfy the visual gate. Preserve that approval instead of asking again. A small correction inheriting an audited baseline does not need a new styling gate.

## Produce the visual proposal

Prepare with [visual exploration](references/visual-exploration.md) and relevant [quality criteria](../ui-ux/references/quality-contract.md). Inspect supplied images and URLs before deriving decisions. Record adopted, adapted and unsuitable aspects; defer generation until the routing boundary below.

Plan two materially different image directions by default; use one when the user's instruction or applicable reference selects a direction. Define page/workflow coverage and realistic fixtures, including dense or long content. Specify typography, spacing, color, hierarchy and density in writing.

Immediately before generating images or visual artifacts, apply [model routing](../ui-ux/references/model-routing.md): present model/effort, scope and generator settings/cost, resolve material-impact approval, and establish actual settings. Reuse matching decisions; keep reasoning effort separate from generator controls. This also applies to static fallbacks.

Output an actual image. Use available image tooling; if unavailable, follow [capability fallbacks](../ui-ux/references/capabilities.md) and produce a disclosed static PNG/SVG render. Prose, source code, or an unrendered prompt does not complete the image stage. Record limitations rather than silently waiving the gate.

## Review and handoff

Store candidates and decisions in the task's versioned `styling/` folder using the [visual decisions template](templates/visual-decisions.md) and [artifact conventions](../ui-ux/references/artifacts.md). Show the actual artifacts with accessible links or previews before requesting a choice or approval.

Bind the user's approval to the exact revision and scope using the [approval template](../ui-ux/templates/approvals.md). Keep approved files immutable. Reopen only decisions affected by a material change; a deadline does not supply missing approval. The written domain rules and explicit token decisions remain authoritative over accidental details in generated imagery.

Once visual approval is present, hand the chosen image, decisions, scope, and remaining questions to [ui-ux-prototype](../ui-ux-prototype/SKILL.md).
