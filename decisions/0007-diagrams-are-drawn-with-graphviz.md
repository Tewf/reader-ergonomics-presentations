# 0007: Diagrams are drawn with Graphviz

**Decision:** A diagram of relations in the family is written in Graphviz's dot language and kept beside the SVG it renders.

**Status:** accepted, 2026-10-29, by the maintainer after a side-by-side comparison. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/v1.18.2/shapes/decision-record.md).

## Context

[Decision 0006](0006-the-visual-standard-of-the-family.md) made this repository the family's standard for figures. The first draft of a figure shape used Mermaid, because GitHub draws it from source and it can write an accessible title and description into its SVG.

That choice rested on how a figure is published, not on how it reads. So five tools were compared on one figure: where reader-ergonomics-topic sits, four boxes, three arrows, three levels. Each drew it with the same three colours, one per kind of repository, and the same font.

## Decision

Graphviz (dot) is the default for diagrams of relations: boxes and arrows, levels, dependencies. The `.dot` source sits beside the `.svg` it renders, and the page embeds the SVG with a [text alternative](../evidence/figures/frame.md#terms). Three other tools keep one job each:

- TikZ, for a figure inside a LaTeX document such as the academic report templates, where boxes are placed by hand;
- the family's flow script, for the counts of a literature search;
- Mermaid, only where GitHub itself must draw the diagram with no build step, as in an issue or a pull request.

## Alternatives rejected

- Mermaid as the default: it broke a repository name across two lines and set a level label on an arrow, and its layout can be tuned only through a theme.
- D2 with its ELK layout: two arrow labels printed over each other.
- TikZ everywhere: the best finish, but every box is placed by hand, and GitHub cannot draw it.
- The family's own script: greyscale by design and placed by hand; one arrow crossed its label.

## Consequences

- GitHub does not draw dot, so each diagram is two files, and a check must show that the SVG was rendered from the current source.
- The figure principles of question 11 and the figure shape are written for what Graphviz draws. They ask for one colour per kind, never the only cue, lines at 3:1 or more, and a text alternative on the page.
- CI that renders a diagram installs Graphviz.
- The comparison is one small figure. With larger diagrams the layered layout, which places nodes to reduce crossings, matters more; no larger test was run.

## See also

[Decisions](README.md), [0006: the visual standard of the family](0006-the-visual-standard-of-the-family.md).
