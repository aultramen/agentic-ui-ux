# Interactive HTML prototype

Use the smallest runnable artifact that demonstrates the agreed interaction scope. Plain HTML/CSS/JavaScript with local assets is the default; a separate local build is acceptable when the interaction actually requires it. Follow the project's visual foundations without coupling the experiment to the production runtime.

## Isolation and reproducibility

- Keep all prototype source in its versioned task artifact folder. Do not edit production components, routes, dependencies, or configuration to make a mockup run.
- Read existing components, tokens, and contracts to understand them; reproduce necessary presentation decisions locally. Do not import production modules or reuse authenticated clients, environment secrets, or real endpoints.
- Use local synthetic fixtures with explicit sample-data labeling. Fix dates, IDs, values, and simulated delays so scenarios reproduce reliably. Avoid uncontrolled random results.
- Actions affect only the mockup. Keep state in memory by default; if persistence is needed to demonstrate the journey, namespace prototype-only storage and provide a clear reset.
- Keep fonts, images, scripts, and styles locally available where feasible. Do not add a network dependency just to make the prototype easy to scaffold.
- Retain approved versions unchanged. Create a new revision for changes; record what affected visual or interaction decisions changed.

## Define a journey before assembling screens

Map the starting state, intended user action, validation or guard, resulting state, and navigation for each significant step. Make every transition in the agreed journey reachable in the prototype. Several attractive pages with disconnected primary actions do not demonstrate a multi-page workflow.

State selectors or fixture controls can expose scenarios that are otherwise slow or impossible to reproduce. Keep these controls visibly separate from the product UI; they are review aids, not proposed product features. Provide loading, empty, failure with retry, success, disabled, and confirmation scenarios where each is applicable. Mark omitted states as not applicable with a reason instead of adding artificial states.

For similar Open/Close workflows, reuse presentation where helpful, but represent action-specific guards and required inputs. A local supervisor scenario simulates authorization for review; it does not implement or prove trusted backend enforcement.

Use the real field names and formats from known API contracts, but fixtures remain synthetic. Record unavailable endpoints and unresolved contracts. Mock success is evidence about the intended experience, not live integration.

## Exercise actual behavior

Provide a local entrypoint, stable navigation between related pages, and launch instructions that work from the documented folder. For a static prototype, prefer direct file opening; if a local server is necessary, document the actual command, URL, and runtime requirements. Verify the URL before calling it accessible. Do not deploy or publish simply to get a preview.

Run the primary journey and applicable failure/retry paths. Check keyboard movement, activation, focus after dialogs and navigation, visible status feedback, label associations, and recovery. Check normal and long/dense content at the intended desktop and smallest relevant container, including a narrow sidepanel if in scope. Do not infer narrow-container usability from desktop screenshots.

Record actual dimensions, scenario, tool or manual method, observed outcome, and evidence path. Screenshots demonstrate appearance; interaction checks demonstrate the behavior actually exercised. Source inspection alone proves neither rendered appearance nor a working keyboard journey. If tools cannot run, provide the feasible artifact and exact remaining review steps without claiming success for those checks.

## Review handoff

Use [prototype review](../templates/prototype-review.md) to give the user the entrypoint, scenario controls, walkthrough, evidence, and limitations. Request approval of the concrete revision's information structure and interactions. Reuse an applicable explicit approval rather than asking again.

Carry exact artifact revisions and written state decisions into [ui-ux-plan](../../ui-ux-plan/SKILL.md). The production plan must still map components, integration, tests, and acceptance criteria to the real architecture. Approval of a disposable mockup is not authorization to silently change domain rules or report unfinished backend integration complete.
