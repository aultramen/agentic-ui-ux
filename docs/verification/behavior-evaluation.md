# Behavioral evaluation record

## Method and limits

Version 0.1.0 was evaluated using separate fresh agents with the ten scenarios in `tests/behavior/scenarios.json`. The baseline received neither proposed framework nor source skills. The forward evaluator received the `ui-ux` entrypoint and linked references, but not the baseline or rubric. Both produced next-action/artifact/status decisions without executing UI applications. Exact responses are preserved separately; these are behavioral samples, not statistical reliability or real browser/API evidence.

## Baseline observations

[behavior-baseline.md](behavior-baseline.md) is the unedited baseline response. Case 1 chose: "Build a small, coherent dashboard prototype ... Choose defaults without delaying for questions" despite unresolved audience/job/scope. Case 9 allowed "wireframes, a visual mockup, or a disposable prototype as appropriate" and did not preserve the required image-first/HTML-second sequence.

Cases 2–8 and 10 already preserved several important constraints (small scope, domain invariants, honest verification and mock boundaries). Those are not counted as new gains.

## First forward run

[behavior-forward.md](behavior-forward.md) is the unedited first forward response. Cases 1 and 9 corrected the observed gaps: unresolved product decisions were held open, and the response explicitly sequenced image approval then interactive HTML approval before production planning. Other scenarios retained the baseline's correct scope and evidence boundaries.

An independent content review found an inconsistent related-flow branch in discovery: a materially changed workflow could inherit an audited visual baseline without an actual image approval. The first forward case 4 reflected that branch. The router, style, prototype and discovery instructions were aligned: material interaction changes use an actual representative image with applicable approval; unchanged visual language needs only one direction or an existing explicitly approved image covering that scope.

Case 7's compressed next-action wording also left its artifact fallback's approval sequencing implicit. The capabilities reference now states explicitly that a fallback changes tools/evidence source, not phase order. These changes close demonstrated ambiguity without requiring redesign for an internal refactor or a local correction.

## Follow-up

The full scenario set was rerun with a fresh evaluator after these corrections. [behavior-forward-r2.md](behavior-forward-r2.md) preserves that raw response. The final assessment below uses the declared rubric, not matching phrasing.

| Case | Assessment of second forward response |
| --- | --- |
| 1 | Pass: unresolved user/job/scope decisions block dependent design; independent inspection continues; full sequence is explicit |
| 2 | Pass: existing accepted baseline, short plan and affected 360 px/control evidence; no forced redesign |
| 3 | Pass: live endpoint remains blocked, independent UI work proceeds, mock evidence cannot satisfy integration |
| 4 | Pass: maps domain differences, material flows use representative image approval then HTML, unchanged internal refactor can use local route |
| 5 | Pass: retains v1, reopens affected v2 decisions and dependent plan/evidence only |
| 6 | Pass: known narrow-container and focus failures remain failed until rechecked |
| 7 | Pass: actual disclosed image fallback, approval before HTML, browser checks remain pending until observed |
| 8 | Pass: backend-only work does not generate UI artifacts |
| 9 | Pass: observes API/reference and uses image then interactive HTML approvals before production plan |
| 10 | Pass: frontend-only can be verified with current evidence, while actual user acceptance is separate |

Result: 10/10 scenario decisions met their expected constraints in this forward sample. This is a manual rubric assessment of actual recorded responses, not ten executed UI tests and not an estimate of future reliability.
