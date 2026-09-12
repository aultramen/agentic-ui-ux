---
name: ui-ux-review
description: "Use when verifying or auditing web/webview UI changes against approved design, business behavior, responsive and accessibility requirements, or when a UI implementation has unresolved gaps."
---

# Review the implementation and its evidence

Read the user's scope, brief, plan, approved artifacts and current implementation before judging. An audit-only request produces findings; it does not authorize unrelated fixes. Do not treat a prototype approval, passing build or author's checklist as proof of production behavior.

## Check the real surface

Use the relevant [quality contract](../ui-ux/references/quality-contract.md), [review procedure](references/review-procedure.md), and [verification template](../ui-ux/templates/verification.md).

- Compare production against the applicable image/HTML decisions and before evidence. Inspect content, hierarchy, density and consistency in the actual task context.
- Exercise affected workflows and applicable loading/error/empty/success/retry/disabled/confirmation states. Verify domain-specific authorization, guards and payload differences where changed.
- Check supported viewport and container widths, including narrow webviews; use keyboard navigation and relevant accessibility checks. Confirm progress, actions and focus are not obscured.
- Run the project's relevant checks and agreed performance measurements. Report what actually ran, observed results and limitations. Never replace browser interaction with source inspection without labeling the missing evidence.

## Close gaps

Map every criterion to `verified`, `failed`, `blocked` or `unverified` with current evidence using the [artifact contract](../ui-ux/references/artifacts.md). Record justified non-applicable checks separately. Do not count exclusions as passed work or reduce scope without a user decision.

If implementation is authorized, send actionable gaps to [build](../ui-ux-build/SKILL.md), then rerun affected checks. For missing external prerequisites, finish independent review and identify the precise next input instead of looping unchanged attempts. Use [capability fallbacks](../ui-ux/references/capabilities.md).

## Deliver

All agreed applicable criteria must have valid evidence before claiming implementation verified. A frontend-only demo may finish with documented dummy data; promised live integration cannot finish against mocks.

Check the preview access, give short reproduction steps and evidence links, and record user acceptance separately. State remaining findings plainly. Only actual acceptance, or still-applicable prior acceptance, yields accepted/ready-to-commit. Never claim these instructions or automated scans guarantee aesthetic quality or complete accessibility conformance.
