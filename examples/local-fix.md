# Example: a checkbox alignment correction

**Illustrative filled brief/plan; this is not an executed product task or a record of real user approval.**

- Task: align the Select Message checkbox in a 360 px ticket sidebar.
- Maturity: brownfield. Integration: existing backend, unaffected by this task.
- Outcome: checkbox and its label align without changing selection behavior.
- Route: local correction; the existing layout is the baseline to inspect. No new styling/HTML approval cycle solely for an 8 px correction.
- Scope: this control and its supported container sizes. No ticket workflow, endpoint, permission or global design-system change.

| ID | Criterion | Implementation | Verification | Initial status |
| --- | --- | --- | --- | --- |
| UX-01 | Checkbox and label align at 360 px without clipping | Adjust the existing layout token/rule where appropriate | Compare actual before/after render at 360 px | unverified |
| UX-02 | Label click and keyboard activation still toggle selection | Preserve existing semantic control and event behavior | Exercise pointer/keyboard and inspect focus | unverified |

Deliver the actual diff, screenshots and observations, then a working preview. Do not add broad snapshot/unit tests merely to assert a CSS value. Do not claim this example's two criteria are verified without running those checks on the real application.
