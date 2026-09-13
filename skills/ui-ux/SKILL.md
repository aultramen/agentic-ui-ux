---
name: ui-ux
description: "Use when creating, improving, aligning, or reviewing web or webview interfaces, including requests such as rapikan tampilan, samakan flow, or buat dashboard; not for backend-only work or authoring this framework."
---

# UI/UX Workflow

Turn the user's product intent into a reviewable interface and verified behavior. Follow their language, scope, and existing authorization. Announce the selected phase and why it applies.

## Inspect and route

1. Read [discovery](references/discovery.md). Inspect the target repository, affected implementation, existing design system, API contracts, references, and current task artifacts before asking about anything discoverable. Record framework version from the installed managed rules in the brief.
2. Resolve high-impact unknowns about users, primary task, outcome, scope, and constraints. Ask concise questions with useful defaults; deadlines do not answer product questions. Continue independent inspection while awaiting required answers. Mark low-impact assumptions explicitly.
3. Select the route by impact, independently of greenfield/brownfield and backend readiness. A small local fix uses an applicable approved or audited baseline, a short plan and targeted checks. New UI, material styling/navigation changes, and changed workflows use the full route. An audit-only or prototype-only request ends at its requested deliverable.
4. Follow [artifacts](references/artifacts.md) for task-local paths and resumable status. After scope discovery, apply [model routing](references/model-routing.md) before dispatching the next skill: select supported model/effort, show the seven-field proposal, and resolve material-impact approval. The receiving skill validates the same decision at its execution boundary without duplicate approval. Load [capabilities](references/capabilities.md) when choosing tools.

## Full route

[Style image](../ui-ux-style/SKILL.md) → user visual approval → [interactive HTML](../ui-ux-prototype/SKILL.md) → user interaction approval → [production plan](../ui-ux-plan/SKILL.md) → [build](../ui-ux-build/SKILL.md) → [review](../ui-ux-review/SKILL.md) → fix evidenced gaps → user review.

Image and HTML approvals mean different things. Do not substitute a generic template, written proposal, or single screenshot for both. Reuse an existing approval only when its artifact, scope, and relevant decisions still apply. Ask only for missing or materially changed decisions; do not add a separate plan-approval ceremony when implementation is already authorized.

## Resume and finish

Read the brief, plan status, routing decisions, approval revisions, and latest evidence; continue from the first unmet dependency rather than restarting. Directly invoked skills check their own prerequisites. Routing approval permits phase execution only; it does not approve designs or results. Use [quality contract](references/quality-contract.md) for observable criteria, not aesthetic bans.

Complete independent authorized work while dependencies are blocked. Explain the specific blocker and leave affected criteria unverified. All applicable criteria need current evidence before claiming implementation verified; user acceptance is recorded separately. Do not claim automatic skill selection or written instructions guarantee visual quality.
