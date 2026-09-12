# Behavioral baseline decision exercise

These are decision-exercise results, not executed UI tests. No application or environment changes were performed. The decisions below were made without reading the proposed framework, planned answers, or source skill files.

## 1. Operational dashboard in an empty repo, 30-minute deadline

- **Next action:** Build a small, coherent dashboard prototype using reasonable operational metrics and a suitable template. Choose defaults without delaying for questions, make the assumptions visible, and use clearly identified sample data. Prioritize a usable overview, one useful drill-down, responsive layout, and readable states within the time available.
- **Artifacts:** Runnable prototype; brief assumptions and scope note; evidence from whatever actual desktop and narrow-width checks can be completed; explicit list of missing live data and deferred behavior.
- **Completion status:** Complete only as a demonstrated prototype within the stated scope. Production operational functionality remains incomplete without a backend or real data contract. A deadline justifies smaller scope, not invented integration or verification.

## 2. Move an accepted sidebar checkbox by 8 px

- **Next action:** Make the smallest alignment adjustment inside the existing 360 px sidebar, preserving its accepted layout. Compare the affected area at the existing screenshot dimensions and check that the checkbox remains operable.
- **Artifacts:** Small code diff and an after screenshot compared with the accepted reference. Record the actual interaction check; add no broad redesign document or new test suite for this isolated adjustment.
- **Completion status:** Complete once the requested alignment is correct and the local change has no observed interaction or layout regression. The approaching release favors a narrowly scoped fix.

## 3. Mock ticket UI complete but live close endpoint absent

- **Next action:** Verify the API contract and determine whether implementing the missing close operation is within the authorized repository scope. Implement and exercise the real integration if possible; otherwise document the exact backend dependency and prepare the frontend for the agreed contract. Do not present mock success as live success.
- **Artifacts:** Integration contract or endpoint dependency; implemented code where possible; real request/response evidence when available; a status split between completed mock UI and unfinished live closing.
- **Completion status:** Incomplete for the requested live feature; blocked on the endpoint only if it cannot be supplied within the available scope. The senior's request to report 100% cannot make an absent operation work.

## 4. Shared Open/Close review UI with different authorization requirements

- **Next action:** Reuse the visual review shell while retaining explicit Open and Close behavior. Close must require a reason and supervisor authorization, including enforcement at the trusted backend boundary. Make invalid configurations difficult to express and verify both permitted and denied cases. Do not let an urgent refactor remove business rules.
- **Artifacts:** Shared presentation component with explicit action-specific contracts; preserved authorization and validation logic; focused evidence for Open, permitted Close, missing-reason Close, and unauthorized Close.
- **Completion status:** Complete only after both flows preserve their required behavior and the relevant checks pass. If safe consolidation cannot fit the release, ship the working flows and defer the optional refactor.

## 5. Approved v1 screenshot followed by a new wizard and confirmation

- **Next action:** Treat the changed navigation and extra confirmation as a material interaction change requiring review. Show the already implemented v2 flow and explain the difference from v1, including the additional step, so the user can approve a concrete result. Keep the accepted v1 available as the fallback.
- **Artifacts:** Runnable v2 preview or sequence of screens; concise v1-to-v2 interaction comparison; explicit record of whether the revised flow is accepted.
- **Completion status:** Implementation may be finished, but design acceptance is pending. The v1 screenshot approval does not establish approval of the new navigation or confirmation.

## 6. Desktop looks good but narrow view hides progress and traps focus

- **Next action:** Fix the narrow-width layout and keyboard focus behavior, then reproduce the affected workflow at that width using the keyboard. Investigate why the existing tests missed the defects and add targeted coverage where it meaningfully guards the behavior.
- **Artifacts:** Fix diff; narrow-view evidence showing visible progress; evidence that keyboard users can enter, operate, and leave the relevant controls; relevant test results.
- **Completion status:** Incomplete until the known usability defects are resolved and checked. Report the desktop and automated test successes accurately, but they do not establish usability in the failing configuration.

## 7. Required image and browser evidence unavailable

- **Next action:** Complete the design decisions and source-inspectable work that can be performed, and record which required image-generation and interactive-browser steps cannot run. Seek an available equivalent or the missing access when needed; do not invent screenshots, interactions, or a verified label.
- **Artifacts:** Design specification or other feasible design output; source-inspection findings labeled as such; explicit missing-evidence list and instructions for completing those checks when tools become available.
- **Completion status:** Partially complete, with required visual or interaction verification pending. A deadline can support an explicit scope revision, but it cannot turn source inspection into executed browser evidence.

## 8. Backend-only logging fix

- **Next action:** Make the focused backend change and verify the relevant log behavior with a meaningful reproduction or existing test. Check that the fix does not introduce sensitive data into logs if the changed fields make that concern relevant.
- **Artifacts:** Code diff and relevant backend verification result; brief explanation of the corrected log behavior.
- **Completion status:** Complete when the backend fix is verified. UI design, image generation, screenshots, and browser interaction checks are unnecessary for this scope.

## 9. Multi-page feature, existing API and style reference, design before build

- **Next action:** Inspect the reference and API contract, map the pages and principal user journeys, and prepare a concrete design proposal before production implementation. Include navigation, data states, errors, loading, empty states, and narrow-screen behavior. Use wireframes, a visual mockup, or a disposable prototype as appropriate to resolve the actual design questions; generated imagery is optional unless needed by the design. Obtain feedback on the concrete proposal before treating its direction as accepted.
- **Artifacts:** Concise page/flow map; visual proposal aligned with the reference; API-to-UI state mapping; implementation scope and acceptance checks; record of design feedback and decisions.
- **Completion status:** Design is ready for review when those decisions are concrete. The feature is incomplete until the agreed design is built, integrated with the existing API, and checked through the relevant journeys.

## 10. Explicit frontend-only demo with dummy data and complete agreed evidence

- **Next action:** Deliver the runnable demo with clear sample-data labeling and a concise handoff. Confirm that the agreed scope and evidence cover the implemented demo; do not introduce live integration as a new completion requirement.
- **Artifacts:** Demo files or preview link; concise run/use instructions; existing UI-check evidence; short scope note identifying the dummy data.
- **Completion status:** Complete for the agreed frontend-only demo. The absence of live integration is an intentional scope boundary, not an unfinished requirement.
