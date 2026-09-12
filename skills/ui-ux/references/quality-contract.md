# Contextual UI quality contract

Translate the requested improvement into applicable acceptance criteria before implementation. Audit these dimensions against the actual product and approved references. Select necessary checks rather than imposing every interaction state on a static label.

| Dimension | Design decisions | Evidence to inspect |
| --- | --- | --- |
| Context and visual identity | Audience, primary job, brand, information density, compositional rationale | Representative real-domain content; match to the approved direction |
| Hierarchy and scanability | Primary action, heading levels, grouping, spacing, alignment, typography | Readable task order; distinguish primary content from secondary detail |
| Content | Meaningful labels, amounts, dates, explanatory copy, long strings and dense records | No lorem ipsum masking overflow or vague actions |
| States and feedback | Applicable loading, progress, empty, error, retry, success, disabled, confirmation, hover/focus/pressed states | Actual transitions and accessible feedback, not just state labels |
| Responsive containers | Supported viewport and container widths, overflow, sticky regions, zoom, orientation where relevant | Narrow sidepanel as well as desktop; no clipped actions or obscured focus |
| Accessibility | Native semantics, names/labels, keyboard order, focus/return, contrast, status announcements, non-color cues | Automated checks plus manual keyboard and relevant assistive-technology checks |
| Performance | Existing budget; otherwise agreed user-experience target and reproducible conditions | Measured relevant behavior, stable layout, responsive input; note lab-only limits |
| Consistency and structure | Existing tokens, layout primitives, components, icons and domain contracts | Reuse that preserves meaning; no unnecessary new UI framework |

For the web, target applicable WCAG 2.2 A/AA requirements. A clean automated scan is not a claim of full WCAG conformance. Use native controls first; consult the ARIA Authoring Practices for custom interaction patterns. Verify browser/webview and touch constraints relevant to the target, not every possible device.

- [WCAG quick reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)

## Visual judgment

Do not ban gradients, cards, rounded corners, particular fonts, or restrained interfaces by default. Explain why the layout supports this user's task. Alternatives must differ in hierarchy, composition, density or interaction emphasis, not only color. Avoid ungrounded decoration and template-shaped content that disguises missing product decisions.

Progressive disclosure may hide secondary detail, but must preserve discoverability of essential actions, actionable errors and necessary status. An icon-only connection indicator needs an accessible name and clear failure feedback. A sticky progress footer must not cover content or focused controls in a narrow panel. The solution depends on the observed problem; those patterns are examples, not mandatory placements.

## Shared workflows without lost domain rules

Compare triggers, states, events, guards, side effects, payloads and feedback before extracting behavior. Share proven invariants; retain explicit domain differences. Separate presentation from domain logic at the seams the project supports. Do not require a universal configurable component, formal state-machine library, or zero duplication.

For Open/Close Ticket, a common review shell and loading/retry feedback may be appropriate while Close still requires a supervisor, reason, different payload or different transitions. UI disabling is feedback, not replacement for server authorization. Regression evidence must cover permitted and denied operations and valid differences, not assert superficial parity everywhere.

## Proportional verification

A cosmetic alignment fix can use an inspected diff, targeted interaction and before/after screenshots. Changed workflow logic needs meaningful behavior/regression tests. API integration needs actual contract and success/error verification. Capture the important production states; an approved mock does not prove them.
