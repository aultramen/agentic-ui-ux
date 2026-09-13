# UI/UX Workflow 0.2.0 verification

Dynamic model/effort routing is implemented and ready for user review. All 26 package/installer tests passed. Independent behavior exercises matched the targeted routing decisions in all 12 final cases. Native host model switching was not executed for this release.

## Executed checks

| Check | Observed result | Evidence |
| --- | --- | --- |
| RED distribution checks before policy/template existed | 26 tests, 5 expected failing assertions; original 24 tests still passed | [Original captured output](unit-tests-red.txt) |
| Final unit suite | 26 tests passed, no failures/skips; Python 3.14.7 on Windows | [Actual command/output](unit-tests.txt) |
| Actual-source disposable install, both hosts | Policy/template bytes match source; installed Markdown links resolve; Claude excludes Codex metadata; dry-run writes nothing and reinstall is idempotent | `test_actual_bundle_distributes_relocatable_routing_files_to_both_hosts` in the unit output |
| Direct entrypoint distribution | All six entrypoints link the same policy; every entrypoint remains below 500 whitespace words (359–438) | Package tests and source inspection |
| Behavioral RED → GREEN | Baseline 5/12 targeted criteria, first forward 12/12, final corrected-source forward 12/12 | [Assessment and exact responses](behavior-evaluation.md) |
| Independent source review | One style generation-order ambiguity found, corrected and rechecked; no remaining finding reported | Correction described in behavior assessment; current style entrypoint/procedure |
| Final documentation/snapshot check | 106 local Markdown links resolved across 41 documents; tested package/test hashes unchanged; `git diff --check` exited 0 (line-ending conversion warnings only) | `final-checks.json` |

The tested [source hashes](source-sha256.json) identify 37 package and test files. Tests used disposable projects and fake homes; the real user's global or project skill configuration was not installed or changed. The installer implementation and host metadata schema are unchanged.

## Requirement traceability

| Criterion | Implemented connection | Evidence / practical limit |
| --- | --- | --- |
| MR-A1: six phase boundaries | Router resolves next scope; each directly invoked phase links and applies the same policy at its execution boundary | Link/distribution tests; MR-01–MR-06; corrected style procedure |
| MR-A2: supported dynamic choices and high planning | Shared defaults resolve concrete available models/efforts; planning below high needs explicit choice | MR-05, MR-06, MR-12; no fixed provider model IDs in the core |
| MR-A3: disclosure, contextual approval, reuse/rejection | Seven-field card; semantic scope/output identity; preserved decisions; explicit alternative after rejection | MR-01–MR-09, MR-11; fixture comparisons are not real price measurements |
| MR-A4: requested versus effective configuration | Approved choice and actual executor settings have separate records; manual switch/confirmation when automatic control is absent | MR-10, MR-12; native switching not executed |
| MR-A5: durable separate routing history | Task-local model-routing template; brief, plan, verification and design approvals reference decision IDs | Artifact/template inspection; MR-07, MR-10, MR-11; no fabricated user decisions |
| MR-A6: portable distribution and onboarding | Shared files inside router skill tree; README, examples and testing guide updated to 0.2.0 | Actual-source installation and complete existing installer regression suite |

## Boundaries of this verification

Behavior reports are independent source-based decision exercises, not native-host discovery/execution or downstream UI tests. One auxiliary cheaper-alternative phrase lacked fixture pricing; the assessment discloses it and does not treat it as proven savings. These samples do not establish universal model compliance, optimal cost or output quality.

Codex/Claude model switching and native invocation of the new policy were **not run**. The [0.1.0 native report](../native-hosts.md) remains historical: its Codex observation and Claude organization-access restriction do not establish current 0.2.0 runtime results. Future native smoke should use the documented temporary-host procedure and record actual settings/provenance.

Implementation authorization comes from the user's approved plan; final user acceptance is separate. No publish, commit, push or real installation was performed. The [task plan](../../ui-ux/work/2026-09-13-model-routing/plan.md) retains the scope and authorization.
