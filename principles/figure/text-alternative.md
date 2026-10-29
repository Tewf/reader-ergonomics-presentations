# Text alternative

**Claim:** beyond the alt text of reader-ergonomics' [figure next to its text](https://github.com/Tewf/reader-ergonomics/blob/v1.18.2/principles/page/figure-next-to-its-text.md), a figure of more than a few nodes has a long description of its parts and their relations. Its alt text reads each arrow in the direction the figure defines.

- **Grade:** convention (a standard), untested with readers of documentation.
- **Evidence:** [review, strand 4](../../evidence/figures/review.md).
- **Check:** reader-ergonomics' `figure-alt`, exact for the short alternative, which its figure next to its text names; whether a complex figure has its long description is not checked.
- **Reader styles:** none changes it.

## What it asks

- Write the alt text as the figure's message, in one sentence: what it shows, not what it is.
- For a diagram of more than a few nodes, add a long description: the type of figure, its parts and how they relate, as a list beside it or under it.
- Never use the file name, or "diagram", as the alternative.

## Why

For a chart or a diagram, WCAG 2.2 asks for two alternatives, a short one and a long one (W3C 2023e). The long alternative gives the type, a summary, the trends and, where practical, the data as a table. The same page lists a file name used as the alternative as a failure. The W3C tutorial on complex images shows three ways to attach the long description (W3C 2026a).

## Limits

- The standard is not tested with readers of documentation, and no study of long descriptions for node-link diagrams was found.
- Mermaid writes `accTitle` and `accDescr` into its SVG (Mermaid 2026c); GitHub's page on diagrams gives no alt-text guidance (GitHub 2026 diagrams).
