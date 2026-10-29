# Visible lines

**Claim:** lines, arrows, borders and fills that carry meaning have at least 3:1 contrast against what lies next to them.

- **Grade:** convention (a standard).
- **Evidence:** [review, strand 4](../../evidence/figures/review.md).
- **Check:** `figure-contrast` (exact for declared colours): each stroke in an SVG against the page and against its own fill.
- **Reader styles:** none changes it.

## What it asks

- Give every outline and arrow a solid colour of 3:1 or more against the page and against the fill it borders, in both schemes.
- Write colours without an alpha channel: an 8-digit hex is dropped by some renderers, and the line vanishes.
- Text in a figure keeps the 4.5:1 of [sufficient contrast](https://github.com/Tewf/reader-ergonomics/blob/v1.11.0/principles/page/sufficient-contrast.md).

## Why

WCAG 2.2 success criterion 1.4.11 asks 3:1 for the parts of a graphic needed to understand it, against adjacent colours (W3C 2023g).

## Limits

- The threshold is a standard, not a measured point of failure.
- Text that carries the same information exempts a graphic; a figure whose labels say everything may pass with faint lines, but its structure is then harder to see.
