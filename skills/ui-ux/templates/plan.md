# Production plan: <task-id>

- Framework version and source brief:
- Outcome and scope:
- Applicable baseline / approved image and HTML revisions:
- Relevant business and API contracts:
- Current state and next action:
- Applicable routing decision IDs in `model-routing.md` (execution permission only; resolve later phases at their own boundaries):

## Acceptance and implementation

| ID | Observable acceptance criterion | Design/contract reference | Implementation slice and dependencies | Verification method | Status |
| --- | --- | --- | --- | --- | --- |

Use stable IDs (UX-01, UX-02). Status starts `unverified`; valid outcomes are `verified`, `failed`, `blocked`. Document any `not-applicable` reason separately. Exclusions are not passed criteria.

## Architecture and integration

Identify reused tokens/components, shared behavior, domain-specific guards, presentation/domain boundaries and actual API seams. State whether integration is real or explicitly mock-only. Avoid a new abstraction solely to eliminate a few lines of duplication.

## Delivery slices

Order complete user tasks by dependency. Each slice names the criteria it satisfies and can be demonstrated, including relevant states. A short local fix may use one slice.

## Verification and preview

Specify commands, manual interactions, viewport/container sizes, evidence locations, preview launch/access and relevant performance conditions. Distinguish automated tests, manual observation, and user review.

## Scope changes and dependencies

Retain the user's explicit decision for changes to scope; list missing contracts/tools and independent work that can proceed. Do not turn a missing production endpoint into an implicit mock-only completion.
