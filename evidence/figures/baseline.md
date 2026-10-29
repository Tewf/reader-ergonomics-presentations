# Baseline: what the figure rules are compared against

This file names the figure a proposed figure design must beat, and how the two would be compared.

## The baseline named

- **Practice baseline:** the Urban Institute data visualization style guide (Urban 2025, updated 2025-08-27).
- **Testable floor:** WCAG 2.2 success criteria 1.1.1 and 1.4.11 (W3C 2023e, W3C 2023g, W3C 2023f).
- **Peer-reviewed counterpart:** Rougier 2014, ten simple rules for better figures.
- **Null baseline:** the figure as most repositories draw it today: text art in a code block, no alternative text, no source line.
- For diagrams of systems, the baseline stays the one held in system-diagrams (the C4 guidance and its review checklist).

## Why this one

| Reason | Urban 2025 |
|---|---|
| Public, dated, versioned | yes: dated 2025-08-27, previous version linked |
| Scored | 13 of 20, above the threshold of 10 |
| Rules a program can check | source line, fewer than seven categories, alt text, contrast (titles are to be concise, with no length stated) |
| Accessibility included | WCAG 2.0 AA contrast for text and alt text for web charts |
| Rival considered | FT 2026 (11 of 20) chooses chart types and gives no layout rules; Rougier 2014 is expert advice with no experiment, and few of its rules have a threshold (a caption on every figure is checkable) |
| Weakness | no study cited; made for charts more than for diagrams |

## What the new figure shape is compared on

| Property | Urban 2025 | Evidence in this strand |
|---|---|---|
| Title that states the message | yes | Borkin 2016, Rougier 2014 |
| Source line | yes | none; convention |
| Direct labels | yes, when possible; otherwise a legend across the top | none for direct labels; Huestegge 2011 tested data-legend compatibility |
| Colour restraint | yes (fewer than seven categories) | W3C 2023c (held); Song 2025 found colour raised credibility against grayscale and cartoon bars lowered it, so it does not support restraint |
| Alternative text | yes | W3C 2023e, W3C 2026a |
| Contrast of lines and fills | WCAG AA, text only | W3C 2023g adds 3:1 for graphics |
| Drawn from source, not typed | not covered | W3C 2023f, Mermaid 2026c |
| Crossings and angles | not covered | Purchase 1997, Huang 2008b |
| Long description | not covered | W3C 2026a |

- The new shape adds three rows the baseline lacks: drawn from source, crossings and angles, long description.
- The comparison is by checklist on the same figures: a sample of the family's existing text-art diagrams, drawn again and scored on each row.
- No outcome test with readers is planned or implied; none of the rows above has one for diagrams.

## Status

- The review is finished for Q11a to Q11d, because a baseline is named.
- Q11e is a first pass: newsroom guides were not opened (see protocol.md).
