# UI/UX Workflow 0.1.0 implementation

Approved scope: a standalone, stack-neutral web/webview workflow for Codex and Claude Code. No Super Compound runtime, app framework, image provider, or hosted service is required by the core. Build the package here; do not install into the user's global configuration without a selected installation scope.

| ID | Acceptance criterion | Verification |
| --- | --- | --- |
| FW-01 | Six discoverable, progressively loaded skills with an automatic router and explicit invocation fallback | Package checks; native discovery smoke tests where available |
| FW-02 | Discovery distinguishes project maturity, API readiness, scope, references and impact; backend-only tasks stay outside the router | Behavioral scenario evaluation |
| FW-03 | Material UI work uses image approval, interactive HTML approval, then a production plan; small fixes use an audited baseline | Behavioral scenario evaluation; reference inspection |
| FW-04 | Quality contract covers contextual aesthetics, content, states, responsive containers, accessibility, performance and domain-safe reuse | Contract/template inspection; adversarial scenarios |
| FW-05 | Revision-scoped artifacts, approvals, plans and evidence live under the target repository's docs/ui-ux | Template/link checks; worked example |
| FW-06 | Standard-library installer supports explicit user/project and codex/claude/both options and dry-run | Installer CLI and filesystem tests |
| FW-07 | Installer is idempotent, preserves existing instructions, detects local edits and preflights conflicts before writes | Installer regression tests |
| FW-08 | Native adapters preserve a common core and enable automatic invocation without platform tool names in core | Package checks; native smoke tests |
| FW-09 | Failed, blocked and unverified criteria cannot be reported complete; frontend-only mocks are distinguished from real integration | Pressure scenarios and worked evidence examples |
| FW-10 | Documentation explains install, update/conflict recovery, use, verification and capability limits | Run documented commands; inspect deliverables |

Implementation streams: installer/tests; core workflow/references/templates; independent behavioral baseline and forward evaluation. Source changes and actual commands form evidence; no claim that an LLM instruction provides deterministic aesthetic enforcement.

Implementation and evidence are available in [verification results](verification/results.md). The remaining external check is Claude model execution, blocked by organization access; native discovery, installer checks, and Codex invocation have separate recorded outcomes.
