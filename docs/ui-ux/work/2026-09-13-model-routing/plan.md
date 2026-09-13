# Dynamic model routing implementation

- Task: implement the user's approved dynamic model/effort routing plan in UI/UX Workflow 0.2.0.
- Scope: six skill entrypoints, shared routing policy/template, task artifact links, package documentation/examples, distribution tests and independent behavior evaluation.
- Authorization: user message "PLEASE IMPLEMENT THIS PLAN" following the complete proposed plan in this task.
- Locked choices: contextual material-impact approval threshold; pause the dependent phase for manual model/effort switching when the host cannot switch automatically.
- Framework authoring is excluded from the UI/UX product trigger. This task uses the existing assistant configuration and inherited subagents; no UI/UX product phase or model switch is implied by implementation authorization.
- No real installation, global configuration changes, publishing or runtime orchestrator.

| ID | Acceptance criterion | Verification |
| --- | --- | --- |
| MR-A1 | All six direct invocations apply shared routing at their specified execution boundary | Entrypoint/link tests; independent decision exercise |
| MR-A2 | Concrete supported model/effort selection is proportional; planning defaults high/xhigh | Decision exercise and policy review |
| MR-A3 | Seven-field preflight, contextual approval, unchanged reuse and rejection behavior | Decision exercise, including deadline/authority/sunk-cost pressure |
| MR-A4 | Requested and actual settings are distinct; unavailable switching pauses dependent work | Decision exercise; no unsupported runtime claim |
| MR-A5 | Task-local routing history is separate from design and delivery approvals | Template/example review and decision exercise |
| MR-A6 | Both hosts receive portable policy/templates; existing installer guarantees remain | Actual-source disposable installation and complete unittest suite |

## Execution and evidence

Capture pre-change decisions from the committed 0.1.0 skills, then teach observed gaps and run a separate evaluator against 0.2.0 with the same prompts. Retain all raw answers and targeted follow-ups in `docs/verification/0.2.0/`. Keep historical 0.1.0 evidence unchanged. Native host execution is a separate check, never inferred from distribution or subagent decisions.

Initial baseline: 24 existing unit tests passed during planning. Final status: ready-for-user-review. MR-A1–MR-A6 have the scoped instruction/distribution evidence recorded in [0.2.0 results](../../../verification/0.2.0/results.md): 26 unit tests passed; final independent decision exercise matched 12/12 targeted routing criteria. A style instruction-order ambiguity was corrected and independently rechecked. Native host switching was not executed, and final user acceptance remains separate.
