# Capabilities, not tool dependencies

Use tools actually available in the current environment. The core does not require a named model, shell, browser provider, image service or subagent API. Platform restrictions and the user's existing authorization apply.

| Need | Preferred evidence | Feasible fallback |
| --- | --- | --- |
| Inspect code/contracts | Repository reading and source-aware search | Available file search and direct reading |
| Inspect visual reference | Open image or browse supplied URL | User-accessible local reference; otherwise record missing reference |
| Produce style image | Available image-generation tool, following its instructions | Authored static SVG or rendered PNG; identify its origin |
| Review image | Display actual output and inspect it | Absolute file link and specific user review if agent cannot inspect |
| Prototype | Isolated HTML/CSS/JS with deterministic fixtures | Existing stack in a separate experiment if essential for fidelity; provide run instructions and HTML access |
| Browser verification | Real browser/webview interaction and screenshots | User-performed checks with recorded observations; pending until results arrive |
| Automated checks | Existing project's test/typecheck/build/accessibility tools | Relevant manual checks explicitly labeled; required automated checks remain pending if unavailable |
| Independent review | Separate reviewer or agent with raw requirements and artifacts | A distinct review pass against the same contract; disclose lack of independence |

Check only capabilities needed for the next phase. Do not install tools or request credentials speculatively. Prose is not an image. Reading HTML is not executing it. A screenshot is not proof of keyboard or API behavior. Synthetic test fixtures are not production API evidence.

If a required capability is absent, finish independent work, name the exact missing check and artifact, and request the smallest concrete input or access needed. Fallbacks change the tool or evidence source, not the phase order: on the full route, obtain the static image's applicable visual approval before building interactive HTML. An unavailable browser cannot silently waive interactive verification. If the user supplies actual observations, record their provenance; do not claim the agent ran those checks.

Stop repeating an action when the same external blocker cannot change through more local work. Leave status `blocked` or `unverified`, provide a reproducible next step, and resume when the missing input arrives. An explicit user scope change can remove a requirement; timeout, deadline pressure and exhausted retries cannot approve one.
