# Example: align ticket review and submission

**Illustrative plan excerpt; no implementation, approval or test result is implied.**

Scope: Open and Close Ticket share a review layout, loading feedback and retry behavior. Close additionally requires a supervisor and a reason. The requested deliverable includes live integration.

Visual baseline: the existing ticket design system, after inspection. A material review-to-submit interaction change follows image approval then interactive HTML approval even without restyling: show one representative image using the existing visual language, or reuse an explicitly approved image that already covers this scope. Prototype fixtures remain isolated.

| ID | Criterion | Contract/dependency | Verification | Initial status |
| --- | --- | --- | --- | --- |
| UX-01 | Both flows present consistent review and progress feedback | Shared presentation, separate domain actions | Exercise both workflows and relevant failure/retry states | unverified |
| UX-02 | Unauthorized Close cannot complete; reason is required | Observed server authorization and request validation contract | Permitted/denied integration cases plus UI feedback | unverified |
| UX-03 | Close persists through the real endpoint | Endpoint availability to be discovered; never invented from this example | Actual test-environment request/response and resulting state | unverified |
| UX-04 | Progress remains visible and keyboard focus usable at 360 px | Existing supported sidepanel width | Browser interaction and screenshot of narrow container | unverified |

If the promised Close endpoint is absent, record UX-03 as **blocked** with the actual dependency. Complete independent presentation work, but do not report the integrated feature 100% complete. An explicit user decision to deliver a frontend-only demo would be a documented scope change, not a passing integration test.

Reuse only the proven review/feedback invariants. A shared shell must not erase Close-specific permissions, payload or transitions. Prototype authorization is a scenario simulation, never enforcement evidence.
