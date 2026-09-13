# Model and effort routing

Select the least costly available configuration that is adequate for the scoped work, considering complexity, uncertainty, domain risk, context size and required visual capabilities. Model selection is an execution decision, not design or delivery acceptance. Apply this contract when a phase is invoked directly as well as through the router.

## Select at the execution boundary

Inspect only the brief, scope, relevant prerequisites and host capabilities needed to make the choice before the boundary. Do not do the gated work while waiting for its decision.

| Skill | Boundary | Selection default |
| --- | --- | --- |
| `ui-ux` | Once scope is known, before dispatching the related skill | Select for the concrete next phase; the receiving skill validates the same decision at its boundary. Do not preapprove unsized future phases. |
| `ui-ux-build` | Before the first production edit in the selected scope/output batch | Economical capable model with low/medium effort for local corrections; stronger model and high/xhigh for complex, uncertain or high-risk changes. |
| `ui-ux-review` | Before assessing implementation or running review checks | Medium for focused review; high/xhigh with stronger reasoning for broad scope, permissions, integration or other high-risk behavior. Read-only review is still gated. |
| `ui-ux-style` | After reference/brief preparation, immediately before image or visual artifact generation | Match visual reasoning capability and effort to the composition/coverage complexity; evaluate generator costs separately. |
| `ui-ux-prototype` | After applicable design prerequisites, immediately before interactive HTML generation | Medium for straightforward interaction; high for branching flows, many states or complex domain behavior. |
| `ui-ux-plan` | After input discovery, before drafting the plan | Reasoning-capable model at high by default; xhigh for substantial complexity, dependencies or uncertainty. A small plan still defaults to high on an economical capable model. |

These are selection defaults, not promises that every host exposes those effort labels. Resolve a concrete model identifier and supported effort from current host tools/catalogue or attributed user configuration information. Do not invent model IDs, availability, pricing or supported effort values. If capability information is missing, obtain that specific information before the dependent phase. Keep the active model when it is suitable and no other available choice offers a justified efficiency or capability benefit; do not silently retain inadequate settings to avoid a checkpoint.

Planning below high requires an explicit user choice of the lower-effort alternative. An unsupported xhigh cannot be relabeled as high or treated as active. Offer a supported alternative and obtain the appropriate decision.

For style, distinguish the reasoning model from the image generator. Include the tool/provider/model and quality, resolution or candidate-count settings only when exposed. Otherwise identify the generator as tool-managed/unknown and generator effort as not exposed, not reasoning effort. A static SVG/PNG fallback also passes this boundary and discloses its production method. A new material generator charge requires a decision even if the reasoning configuration stays unchanged.

## Present the choice

Before executing, display this compact card in the user's language, with concrete values rather than an unfilled template:

1. **Skill / phase:** the next execution phase.
2. **Scope / artifacts:** covered work and intended output paths, revisions and quantity.
3. **Recommended model:** concrete supported model; generator/tool choice if relevant.
4. **Recommended effort:** supported reasoning effort; exposed generator settings separately.
5. **Reason:** adequacy, complexity/risk and the cost/time/quality tradeoff against the active or still-applicable approved configuration.
6. **Cheaper alternative:** supported lower-cost model/effort and its tradeoff, or state that none is known/adequate.
7. **Estimated cost / time:** sourced estimate with volume assumptions and uncertainty, or “belum dapat diketahui” / “unknown”.

Numeric estimates require current pricing or observed duration evidence plus workload assumptions. Qualify relative comparisons too; do not infer dollars from subscription quota, invent token counts, or promise a duration. Missing estimates alone do not mandate an extra approval when there is no identified material impact or explicit budget restriction.

A router card already shown for the immediate unchanged dispatch satisfies this presentation; the receiving skill need not echo it or ask twice. Show the current card again on a later resumed execution boundary, referencing the earlier decision without re-requesting unchanged approval.

## Decide and reuse authorization

Compare with the active or latest still-applicable approved configuration. Request approval for a material change in expected cost, duration or capability/output quality, including materially higher effort, provider/tool charges, or a capability tradeoff affecting the agreed outcome. Judge the actual scope and available evidence; neither every model change nor every higher effort is automatically material. Honor explicit spending constraints and previously authorized choices.

Before a required decision, make the proposal concrete with the seven fields and explain the material impact that requires approval under this contract. Record `pending` and stop the dependent phase. Silence, deadline pressure, sunk cost and another person's suggestion do not supply the user's decision. Independent authorized preparation may continue.

The decision identity is **skill + phase + semantic scope + concrete model + effort + intended artifacts (paths/revisions/count)**. Include exposed generator choice/settings in the visual model/output identity. Use stable acceptance IDs or a bounded scope description; ordinary edits, rewording and progress within that same batch do not change identity. Record input/source revisions as execution evidence without invalidating routing approval for every working-tree edit. A materially expanded output/scope is a new decision, not ordinary progress.

- Reuse an actual approval with the same identity and source, across router/phase handoff, retries and resume. Read the existing task record first; do not create a duplicate approval or ask again.
- Reassess a changed identity and its material impact. Preserve old records and unrelated valid approvals. Approval for another phase is not transferable; if the new phase requires no approval, record `not-required` instead of borrowing an old approval.
- With authorized task scope and no material impact or other explicit restriction, record `not-required` with the reason and proceed once the actual configuration is established. This is an agent decision, not user approval.
- On rejection, record `rejected`, stop that phase and offer a lower model/effort. Do not execute the rejected choice, automatically run the cheaper choice, or repeatedly seek the identical rejected approval. Wait for the user's specific alternative choice; preserve the rejected record.

Routing approval grants permission to run only the identified phase. It never approves a design, prototype, production change, test result or final delivery. Visual/interaction approvals and delivery acceptance still follow the [artifact contract](artifacts.md).

## Establish the actual configuration and record it

Use an exposed, authorized switching or phase-delegation capability if available. Record which executor will perform the phase; delegating a phase does not switch the parent assistant. Do not invent metadata keys, edit global configuration, or start a shell child and claim it replaced the active assistant.

If the selected configuration is already active and supported, continue under the applicable decision. Otherwise, when the host cannot switch automatically, pause the dependent phase and request the user's manual switch and confirmation. Do not silently substitute the active model. Use host evidence or attributed user confirmation of the effective model/effort; label user-attested settings accurately. Configuration text or a recommendation is not runtime evidence. Resolve conflicting observations before proceeding. If availability/support cannot be established, leave execution blocked and offer a supported alternative for a specific decision.

Use the [routing record template](../templates/model-routing.md) in the target task's `docs/ui-ux/work/<task-id>/model-routing.md`. Create it only when used. Record the selection and approval state before execution, then record actual settings, evidence/confirmation source and execution status. An approved choice can still be waiting for a switch; do not turn a runtime blocker into an approval rejection or erase either history.

This record is the source of routing decisions. Brief, plan, design approvals and verification notes reference its decision ID rather than copying approval state. Preserve actual decisions and provenance, including resumed executions and alternatives. The installer does not create task records.
