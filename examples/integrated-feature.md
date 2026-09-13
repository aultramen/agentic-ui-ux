# Example: align ticket review and submission

**Illustrative plan excerpt; no implementation, approval or test result is implied.**

Scope: Open and Close Ticket share a review layout, loading feedback and retry behavior. Close additionally requires a supervisor and a reason. The requested deliverable includes live integration.

Visual baseline: the existing ticket design system, after inspection. A material review-to-submit interaction change follows image approval then interactive HTML approval even without restyling: show one representative image using the existing visual language, or reuse an explicitly approved image that already covers this scope. Prototype fixtures remain isolated.

Keep a routing record at `docs/ui-ux/work/<task-id>/model-routing.md` alongside the separate design/result decisions in `approvals.md`. The following profiles are illustrative recommendations to resolve against the host's available models, not actual selections or approvals:

| Phase boundary | Proposed profile / effort | Reason and artifact target |
| --- | --- | --- |
| Immediately before `ui-ux-style` output | Capable visual reasoning / `medium` when supported | One representative static image; record the actual image tool separately, with generator model/settings only if exposed |
| Immediately before `ui-ux-prototype` output | Balanced coding / `high` when supported | Interactive HTML revision covering review, loading, retry and simulated permission states |
| Before `ui-ux-plan` | Strong reasoning / `high`, consider supported `xhigh` if discovered dependencies warrant it | Production plan preserving separate domain actions and real integration requirements |
| Before `ui-ux-build` changes production | Capable coding / `high` when supported | Approved plan's scoped code changes and integration evidence |
| Before `ui-ux-review` starts | Strong review reasoning / `high` when supported | Findings and acceptance evidence for the resulting production revision |

At each boundary, display the skill/phase, concrete scope, host-resolved model, supported effort, reason, cheaper alternative if available, and cost/time estimate if known. This example has no pricing or measured duration. A lower supported effort or efficient model may be proposed with its quality tradeoff; it is not an automatic fallback. Image tool quality is not the reasoning model's effort setting.

Request approval for contextually material cost, time or quality increases. After an approved tuple is recorded, resume with that approval while the skill/phase, scope, model, effort and artifact target remain unchanged; a changed output revision or scope requires reassessment. A rejection leaves that phase unexecuted while a lower option is offered. If automatic switching is unavailable, pause dependent work for the user's manual switch and confirmation, continue independent discovery, and distinguish host-observed from user-attested settings. Runtime confirmation and model approval never stand in for image, interaction or final acceptance.

| ID | Criterion | Contract/dependency | Verification | Initial status |
| --- | --- | --- | --- | --- |
| UX-01 | Both flows present consistent review and progress feedback | Shared presentation, separate domain actions | Exercise both workflows and relevant failure/retry states | unverified |
| UX-02 | Unauthorized Close cannot complete; reason is required | Observed server authorization and request validation contract | Permitted/denied integration cases plus UI feedback | unverified |
| UX-03 | Close persists through the real endpoint | Endpoint availability to be discovered; never invented from this example | Actual test-environment request/response and resulting state | unverified |
| UX-04 | Progress remains visible and keyboard focus usable at 360 px | Existing supported sidepanel width | Browser interaction and screenshot of narrow container | unverified |

If the promised Close endpoint is absent, record UX-03 as **blocked** with the actual dependency. Complete independent presentation work, but do not report the integrated feature 100% complete. An explicit user decision to deliver a frontend-only demo would be a documented scope change, not a passing integration test.

Reuse only the proven review/feedback invariants. A shared shell must not erase Close-specific permissions, payload or transitions. Prototype authorization is a scenario simulation, never enforcement evidence.
