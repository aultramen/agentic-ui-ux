# Example: a checkbox alignment correction

**Illustrative filled brief/plan; this is not an executed product task or a record of real user approval.**

- Task: align the Select Message checkbox in a 360 px ticket sidebar.
- Maturity: brownfield. Integration: existing backend, unaffected by this task.
- Outcome: checkbox and its label align without changing selection behavior.
- Route: local correction; the existing layout is the baseline to inspect. No new styling/HTML approval cycle solely for an 8 px correction.
- Scope: this control and its supported container sizes. No ticket workflow, endpoint, permission or global design-system change.

Before the compact plan, select a capable reasoning model at `high` by default. Immediately before changing production CSS, make a separate build decision. A proposed build preflight could read:

| Field | Illustrative proposal |
| --- | --- |
| Skill / phase | `ui-ux-build` / local production correction |
| Scope | This checkbox, label and supported sidebar widths; deliver the CSS diff and focused verification evidence |
| Recommended model | A host-resolved efficient coding model; fill its concrete ID from the available host catalog |
| Recommended effort | `low` if supported and the inspected correction remains straightforward |
| Reason | Existing behavior and a small, reversible layout change limit the reasoning needed |
| Cheaper alternative | None established until the host's available models and billing context are known |
| Cost / time | Unknown; no measured usage or duration is supplied by this example |

Record the actual choice in `docs/ui-ux/work/<task-id>/model-routing.md`. This proposal supplies no approval: assess material impact against the real task's current or approved choice and request approval when required. If a switch is needed but the host cannot apply it, wait for the user's manual switch and confirmation before the CSS edit. Record unobservable active settings as user-attested, never host-verified. A later review has its own preflight before review starts.

On resume, an applicable approval for the same skill/phase, scope, concrete model, effort and artifact target is reused. If the user rejects a choice, record `rejected`, leave that phase unexecuted and offer a lower model or effort; do not silently substitute an alternative. Model approval does not approve the resulting alignment.

| ID | Criterion | Implementation | Verification | Initial status |
| --- | --- | --- | --- | --- |
| UX-01 | Checkbox and label align at 360 px without clipping | Adjust the existing layout token/rule where appropriate | Compare actual before/after render at 360 px | unverified |
| UX-02 | Label click and keyboard activation still toggle selection | Preserve existing semantic control and event behavior | Exercise pointer/keyboard and inspect focus | unverified |

Deliver the actual diff, screenshots and observations, then a working preview. Do not add broad snapshot/unit tests merely to assert a CSS value. Do not claim this example's two criteria are verified without running those checks on the real application.
