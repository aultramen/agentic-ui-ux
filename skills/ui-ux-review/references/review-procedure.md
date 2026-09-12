# Review procedure

## Establish the target

Identify source revision/dirty state, approved artifact revisions, changed scope and acceptance IDs. Use a separate reviewer when available and useful; supply raw requirements and artifacts rather than the author's desired conclusion. A distinct self-review is allowed when no independent reviewer is available; label it accurately.

Select checks by changed behavior and the existing project contract:

| Change | Minimum useful evidence |
| --- | --- |
| Local cosmetic correction | Before/after at affected size, visual inspection and affected control interaction |
| New or changed workflow | Relevant regression tests, actual end-to-end interactions, important states and domain differences |
| Real API integration | Observed contract, request/response and success/error behavior in an authorized test environment |
| Responsive/sidepanel change | Actual narrow-container and supported viewport checks, overflow and focus visibility |
| Accessibility change | Applicable automated checks and manual keyboard/semantics checks; assistive-technology observation when required |
| Performance-sensitive change | Agreed measured scenario under recorded conditions, compared to the project's budget or baseline |

For a static website, do not invent API states it does not possess. For a ticket operation, successful static rendering is insufficient evidence of submission behavior. Existing required checks remain required even if this table is narrower.

## Inspect and record

1. Start the documented preview; verify it is reachable and displays the intended revision.
2. Inspect the primary task using realistic data, long content, empty/error cases and supported container sizes. Verify essential information remains discoverable after progressive disclosure.
3. Use keyboard navigation through the affected controls; inspect accessible names, visible focus, focus return and relevant status announcements. Check contrast and non-color meaning. A green accessibility scan cannot prove all of these.
4. Verify appropriate separation of presentation/domain behavior and reuse. For related workflows, explicitly test both shared invariants and legitimate differences.
5. Record actual command/action, result and evidence path per acceptance ID. Report pre-existing failures separately without calling required checks passed.

Screenshots should name page/state and viewport/container dimensions. Compare the relevant revision, not an outdated screenshot. Use stable fixtures for visual comparison; do not require exact pixel identity between a generated style image and a responsive production page.

## Findings and closure

Each finding identifies an observable failure, affected criterion, reproduction conditions and smallest useful correction. Separate preference questions from defects against the agreed contract. Do not create a numeric beauty score.

Recheck a corrected failure with its original reproduction and relevant regression coverage. Update only evidence affected by changes. If the same external blocker remains, record it and stop dependent retries; do not declare all work complete or keep asking for the same permission.

Deliver a working preview (or reproducible local launch), data-source disclosure, concise test result and unresolved findings. If every applicable criterion is verified, say implementation is ready for user review. Record acceptance when actually supplied; do not turn silence or author confidence into approval.
