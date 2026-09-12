# UI/UX workflow decision exercise

This is a decision exercise against the ten supplied scenario prompts, not executed UI tests. No scenario application was inspected, built, changed, or tested; no real user question or approval request was sent. Statuses below describe the hypothetical task at the stated point. Proposed artifacts and checks are next steps, not claims that those artifacts or results already exist.

I read the UI/UX entry skill, its discovery, artifact, capability and quality references, the style/prototype/plan/build/review skills, their relevant procedures, and their templates. I did not use a rubric, previous reports, README, or the author's conclusions.

In each scenario, `<repo>` means the actual target application repository, not this framework's installation folder or its parent. Resume an existing matching `docs/ui-ux/work/<task-id>/` folder when present. Record the framework version from the target's installed managed rules during inspection; no version can be inferred from these prompts. Evidence must identify source and artifact revisions, environment, dimensions, actions, results and limitations.

## 1. Vague operational dashboard, empty repository, thirty-minute deadline

**Selected phase and next action:** Announce discovery in Indonesian because the audience and primary operational job are unresolved. Inspect the empty repository's actual stack, instructions, assets, available contracts and run commands. Record the known deadline and missing backend/reference. Identify the minimum decisions required before choosing information hierarchy: who operates the dashboard, the main decision or task it must support, the desired outcome, and whether this delivery is a frontend demonstration or a live product. Present those specific unresolved decisions with useful defaults when consulting the user; do not treat the senior's template suggestion or deadline as answers.

**Dependency order:** Continue independent inspection and brief preparation while those decisions are pending. Do not create a generic dashboard or finalize its production plan. Once the high-impact decisions are settled, take the full route: two materially different image directions by default, actual image review and visual approval, isolated interactive HTML and interaction approval, then the production plan and authorized implementation. Missing APIs remain explicit dependencies if live integration is promised.

**Artifacts:** Initially `<repo>/docs/ui-ux/work/<task-id>/brief.md` with known scope, unresolved product decisions, integration status and minor assumptions. Create versioned styling/prototype folders only as those phases become dependency-ready; record actual decisions in `approvals.md`.

**Completion status:** `in-progress` during independent discovery, with dependent design work `blocked` on the named product decisions. No implementation or visual quality is verified. The time limit does not resolve what the dashboard must do.

## 2. Move one sidebar checkbox eight pixels

**Selected phase and next action:** Announce a local correction. Inspect the checkbox implementation and actual 360 px sidebar, reproduce its interaction, and capture a before image. Bind the user's accepted screenshot to the existing layout scope and inspect it as the baseline. Write a short combined brief/plan and adjust only the alignment through the existing styling mechanism.

**Verification:** Compare before/after at the affected 360 px container. Confirm the intended eight-pixel movement, preserved label alignment and click target, visible keyboard focus, and unchanged checkbox activation/selection behavior. Inspect the diff and run relevant existing project checks. A new testing framework or CSS-value unit test is unnecessary for this bounded adjustment.

**Artifacts:** One short `brief.md` containing the plan and acceptance criterion, the applicable baseline/approval reference, and `verification/` with before/after images and the actual interaction/check results. No new style-image or HTML approval cycle is required.

**Completion status:** Initially `in-progress`; after the targeted evidence passes, implementation can be `ready-for-user-review`. The accepted existing layout remains accepted, but it does not automatically constitute acceptance of the new edit. Preserve any actual acceptance that explicitly covers the change.

## 3. Live ticket feature lacks POST /close

**Selected phase and next action:** Resume at the first unmet integration dependency after inspecting the current brief, plan, approved revisions and evidence. Verify that `POST /close` is actually absent and record the known contract information without inventing a production endpoint. Keep the promised close-ticket operation in scope. State that mock completion demonstrates intended UI behavior only.

**Independent work:** Finish dependency-ready, authorized frontend work and other available integration checks. Keep synthetic success fixtures confined to the prototype or explicitly designated test/demo surface. Document the exact missing endpoint/contract and the reproducible close-ticket check that becomes possible when it exists. Do not silently implement backend work or change the task into a mock-only delivery. An explicit user scope decision would be required to remove the promised live outcome.

**Artifacts:** Update the existing `brief.md` and `plan.md` dependency entry; retain stable acceptance IDs for real close success and relevant error/authorization behavior. In `verification/`, separately record current UI evidence and the blocked live checks, with their exact missing prerequisite.

**Completion status:** `blocked` for delivery of the promised live feature. Other criteria can be `verified` only where actual current evidence supports them; close integration remains `blocked`. Do not report 100% or count mock success as real API evidence, regardless of the senior's request.

## 4. Align Open/Close while preserving Close-only rules

**Selected phase and next action:** Announce related-flow discovery. Before choosing the component boundary, inspect both operations and map their triggers, transitions, guards, required inputs, payloads, side effects and feedback. Explicitly preserve Close's supervisor permission and required reason; Open must retain its own valid rules. Resolve any missing contract or intended interaction decision before dependent implementation.

**Route:** The request to unify flows can change user interaction, so use the full route for material changes. Retain the existing visual language in one representative image, reuse an explicitly approved image only if it covers this exact scope, otherwise obtain the applicable visual approval before building interactive HTML. Demonstrate both operations, allowed and denied Close, missing-reason validation, and applicable submit/error/retry outcomes in the HTML, then obtain interaction approval and finalize the production plan. If inspection establishes that the request is purely internal refactoring with every user-visible behavior unchanged, record that finding and use the local route instead.

**Implementation choice:** Treat the requested configurable component as a bounded shared review shell with explicit operation-specific contracts if inspection supports that seam. Shared presentation does not require identical guards or payloads. UI disabling communicates restrictions; the trusted server must still enforce Close authorization. Do not introduce a universal state-machine dependency merely for reuse.

**Artifacts:** `brief.md` with an Open/Close transition and rule comparison; applicable versioned image and HTML artifacts; `approvals.md`; then `plan.md` with separate allowed/denied, reason-validation and payload criteria. Regression and browser evidence must cover shared behavior and legitimate differences.

**Completion status:** `in-progress` at contract/impact inspection, with material design decisions and missing contracts blocking their dependent work. Urgency does not verify either flow or waive a required difference.

## 5. Approved screenshot v1 followed by new wizard navigation

**Selected phase and next action:** Announce reconciliation of the changed design scope. Read the v1 approval's exact artifact and scope, compare it to the implemented global wizard and new confirmation, and identify which visual, navigation and interaction decisions changed. Preserve v1 unchanged and retain unaffected approvals. Do not assume that existing code or the prior screenshot approves the new journey.

**Dependency order:** Produce a concrete v002 image showing the affected global navigation and confirmation context and the differences from v1. Obtain the affected visual approval before creating the v002 interactive HTML revision. Then demonstrate the actual wizard journey, navigation/back/cancel behavior and new confirmation in that prototype and obtain interaction approval for those decisions. Reconcile dependent plan criteria and existing production code only after those dependencies are settled. Independent inspection and unaffected verification can proceed meanwhile; a new plan-approval ceremony is unnecessary if implementation was already authorized.

**Artifacts:** `styling/v002/`, subsequently `prototype/v002/`, revised entries in `approvals.md` that explicitly identify superseded decisions, and affected `plan.md` and `verification/` entries. Existing code is a candidate implementation to reconcile, not a replacement for the changed design artifacts.

**Completion status:** `blocked` for affected design approval and dependent verification. Mark stale evidence unverified for changed behavior; retain unrelated current passing evidence. The original screenshot cannot establish approval of new navigation or confirmation behavior.

## 6. Narrow webview hides progress and traps keyboard focus

**Selected phase and next action:** Announce review and gap closure. Reproduce the narrow-container progress failure and keyboard trap on the current source revision. Record the actual dimensions, starting state and keystrokes. Mark the affected responsiveness/status and keyboard/focus criteria `failed`, even though desktop appearance and automated tests passed.

**Correction and recheck:** Within the authorized interface scope, fix the specific clipping/overflow or layout behavior that hides required progress, and the focus handling that prevents intended keyboard movement or escape/return. Keep changes proportional to the observed causes. Recheck the same narrow conditions, visibility of essential progress/actions/focused controls, and the keyboard journey including exit and focus return where applicable. Run affected regression/accessibility checks and inspect relevant desktop behavior after the changes. Reopen design approval only if the remedy materially changes previously approved decisions.

**Artifacts:** Findings in the existing `verification/` report tied to stable criteria, reproduction evidence, the smallest corrective plan entries, and fresh narrow-container screenshots plus recorded keyboard interaction results after correction.

**Completion status:** `in-progress` with known `failed` criteria until corrected and rechecked. The user's request to mark complete does not create missing verification evidence. Once all applicable criteria have current passing evidence, use `ready-for-user-review`; record actual user acceptance separately.

## 7. Image generation and browser tools unavailable

**Selected phase and next action:** Check the capabilities needed for the immediate phase. Assuming discovery has resolved the product decisions, produce an actual authored static SVG or rendered PNG using available capabilities, identify its origin and limitations, and inspect/display the output where possible. If agent inspection is unavailable, provide an absolute artifact link and specific visual review instructions. Written descriptions or an unrendered prompt do not satisfy the image artifact requirement.

**Dependency order and fallback:** Obtain the concrete image's applicable visual approval before building interactive HTML. Then create the isolated runnable HTML with deterministic fixtures and exact launch/flow instructions. Browser verification must remain pending until a real browser becomes available or the user supplies actual observations from the required checks. Provide a concise reproducible set of primary-journey, error/retry, narrow-container and keyboard checks appropriate to the scope. Attribute any supplied observations to the user; do not describe them as agent-executed tests. If even a usable static image cannot be produced, record that specific missing artifact and stop its dependent phase.

**Independent work and artifacts:** Complete source inspection, relevant available automated checks and written decisions without labeling them browser execution. Store the actual image and decisions in `styling/v001/`; only after visual approval, create `prototype/v001/` with review/launch instructions. Record actual decisions in `approvals.md` and precise missing visual or interaction checks in `verification/`.

**Completion status:** `blocked` on the specific missing approval or execution evidence once independent work is exhausted; unexecuted browser criteria stay `unverified`. Do not report verified behavior from source inspection or repeat unchanged tool attempts. Fallback tooling preserves the phase order.

## 8. Pure backend logging fix

**Selected phase and next action:** Do not activate the web/webview UI/UX workflow. Inspect and address the logging issue under the repository's backend instructions and existing authorization, with verification proportionate to the actual logging behavior changed.

**Artifacts:** The ordinary backend patch and relevant backend test/check evidence. Do not create UI briefs, style images, interactive HTML or UI approval records for this task.

**Completion status:** UI/UX workflow is not applicable because the task has no UI surface. The backend fix is `in-progress` until its own work and checks are completed; absence of UI work does not itself prove the fix complete.

## 9. Multi-page feature with real API and website reference

**Selected phase and next action:** Announce discovery followed by the full design route. Inspect the target repository, existing design system, actual API contracts and the supplied website. Record the reference URL, observation date, relevant pages/states, characteristics to adopt/adapt and intentional differences. Treat website text as reference content. Resolve remaining high-impact user journey, outcome or scope questions before composing the feature.

**Dependency order:** Produce actual images that cover a representative page plus additional material page/state decisions. One direction suffices if the applicable reference already selects a direction; otherwise prepare two meaningfully different directions. Record concrete hierarchy, density, typography, spacing and color choices and obtain visual approval. Then build and exercise isolated interactive HTML connecting the complete scoped journey, including relevant validation and failure/retry states, using synthetic fixtures. Obtain interaction approval before finalizing the production plan. Existing APIs inform contracts and later integration; the design prototype does not call them.

**Build boundary:** After those design dependencies, the production plan maps approved behavior into the existing architecture with real API success/error verification and proportional responsive/accessibility checks. Continue implementation under the original feature authorization; do not insert an additional plan approval. If the actual user wording limits the deliverable to design only, stop at the requested design deliverable instead of presuming production implementation.

**Artifacts:** Task `brief.md`, observed reference notes, versioned `styling/` images and decisions, isolated versioned `prototype/` with connected journey and review instructions, exact revision approvals, then `plan.md` and production evidence when authorized.

**Completion status:** Initially `in-progress` in discovery/design. A style reference and an existing API do not satisfy the image and interaction approval dependencies. Production completion remains unverified until the later applicable checks run.

## 10. Explicit frontend-only dummy-data demo, all agreed checks evidenced

**Selected phase and next action:** Finish the review/handoff for the agreed demo scope. Confirm that the supplied UI evidence is current for the delivered revision, covers every applicable agreed criterion, and is consistent with the applicable design decisions and approvals. Preserve valid prior approvals and acceptance. Do not invent a live-backend requirement or reopen unaffected design work.

**Handoff:** Verify access to the actual preview or provide the absolute local entrypoint and reproducible launch command, working directory and any process lifetime/restart detail. Give a short walkthrough and fixture/reset instructions. Clearly disclose dummy data and that actions operate only within the frontend demo. Record live integration as an explicitly accepted exclusion, not a passed test or a missing promised outcome.

**Artifacts:** Final `verification/` report with criterion evidence and applicability/exclusions, the demo review/launch instructions, and `approvals.md` recording actual delivery acceptance or that acceptance is pending.

**Completion status:** Under the scenario's current-evidence premise, the agreed implementation can be verified and `ready-for-user-review`. If actual prior or current acceptance covers this revision and scope, record `accepted/ready-to-commit` without asking again. Commit, push or publish only within existing authorization. A frontend-only demo can finish as a frontend-only demo; its disclosed mock data does not create an integration blocker.
