# 0006: The visual standard of the family

**Decision:** This repository is also the family's standard for the visual: figures and diagrams in any document, not only slides.

**Status:** accepted, 2026-10-29; its principles wait for review question 11. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/v1.9.0/shapes/decision-record.md).

## Context

Text-art diagrams across the family's repositories hid half their content behind a scrollbar and read worse than a drawn figure would. The maintainer asked whether this repository covers visual appearance and its ergonomics; it covered slides, legibility, colour and motion, but not how a figure or a diagram is drawn. The evidence on diagram design sat in reader-ergonomics-software-design's diagram review.

## Decision

This repository owns the visual: slides as before, and figures and diagrams in any document. A review strand comes first (question 11: layout, encoding and grouping, appeal, text-art against drawn diagrams, practice), then a figure group of principles, a figure shape and checks. The other repositories' figures are then redrawn, as feedback.

## Alternatives rejected

- Practical only, converting text figures to rendered diagrams now: the rules would have no evidence behind them.
- Leaving figures to reader-ergonomics' page principles: they say a relation should be drawn, not how to draw it well.

## Consequences

Principles about figures enter only from question 11, once audited. Software-design's diagram review is linked, not reviewed again. A figure rule here applies to every repository of the family through its link, once the principles exist.

The cost: every repository's figures now wait on this repository, on its review of question 11 and on its pace.

## See also

[Decisions](README.md), [the review](../evidence/presentations/review.md), reader-ergonomics-software-design's [system diagrams review](https://github.com/Tewf/reader-ergonomics-software-design/tree/master/evidence/system-diagrams).
