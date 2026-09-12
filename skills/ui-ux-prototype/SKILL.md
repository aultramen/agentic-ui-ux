---
name: ui-ux-prototype
description: "Use when a frontend page, feature, or business workflow needs a disposable interactive HTML mockup, or an approved interaction design needs a material revision."
---

# UI/UX Prototype

Turn the selected visual direction into an interactive, disposable HTML artifact using isolated dummy data. HTML approval establishes interaction intent; it does not prove production integration.

## Confirm the applicable gate

Read the brief, selected styling revision, written design decisions, and approval records. For new UI, material redesign, or materially changed workflows, require approval of the applicable image direction before building the HTML prototype; route missing visual work to [ui-ux-style](../ui-ux-style/SKILL.md). Existing explicit approval for the same artifact and scope remains valid. A small change inheriting an audited baseline can use the shortened route selected by [ui-ux](../ui-ux/SKILL.md).

Before creating screens, resolve high-impact interaction or domain questions through [discovery](../ui-ux/references/discovery.md). Preserve known authorization, validation, and state transitions. Image details cannot override these rules.

## Build and exercise the prototype

Follow [interactive prototype guidance](references/interactive-prototype.md). Save a versioned, runnable HTML entrypoint and its local assets under the task's `prototype/` folder, using [artifact conventions](../ui-ux/references/artifacts.md). Keep production source untouched. Do not import production application modules, contact real APIs, or reuse credentials. Dummy actions change only prototype-local state and must be resettable.

Cover the agreed scope: one page, related pages, or an entire feature journey. Make navigation, primary actions, validation, and applicable loading, error, retry, empty, success, disabled, and confirmation states exercisable with deterministic fixtures. Include realistic long/dense content and target narrow containers.

Use the [quality contract](../ui-ux/references/quality-contract.md) for hierarchy, accessibility, responsiveness, and task suitability. Actually open and exercise the artifact when browser tools are available. Record executed checks separately from source inspection. Follow [capability fallbacks](../ui-ux/references/capabilities.md) when required evidence cannot be obtained; do not label unexecuted behavior verified.

## Approval and production handoff

Provide a working preview or absolute file link, launch instructions, scenario controls, and limitations using the [prototype review template](templates/prototype-review.md). Show the complete scoped journey before seeking interaction approval.

Record exact revision, scope, and user decision with the [approval template](../ui-ux/templates/approvals.md). Retain approved versions; create a new revision for material interaction changes and reopen only affected approvals. Approval of a screenshot alone does not establish approval of new navigation or confirmation behavior.

After applicable visual and interaction approvals are present, pass the artifacts, state/flow decisions, API assumptions, and unverified items to [ui-ux-plan](../ui-ux-plan/SKILL.md). Treat prototype code as throwaway reference; map behavior into the production architecture deliberately.
