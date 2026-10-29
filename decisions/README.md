# Decisions

The choices that shaped this repository, one record each, in the shape of reader-ergonomics'
[decision record](https://github.com/Tewf/reader-ergonomics/blob/v1.9.0/shapes/decision-record.md). A record is never edited to change its decision; a new record replaces it.

| Record | Decision |
|---|---|
| [0001: A public standard, and private styles](0001-a-public-standard-and-private-styles.md) | This repository holds the common ground of any presentation, and a person's own way of presenting stays in a style of their own that overrides it. |
| [0002: Contexts are written as audiences](0002-contexts-are-audiences.md) | Each context is a reader style named by its audience, so an academic talk, a business pitch and a casual talk override the base without a new mechanism. |
| [0003: Decks are HTML, one section per slide](0003-decks-are-html-sections.md) | The deck checks read HTML decks whose slides are <section> elements and whose notes are <aside class="notes">. |
| [0004: Pin reader-ergonomics at a release](0004-pin-reader-ergonomics-at-a-release.md) | CI checks out reader-ergonomics by the commit of a release, and the text links name the same release. |
| [0005: The example deck is not named after its shape](0005-the-example-deck-is-not-named-after-its-shape.md) | The example deck is shapes/example-talk.html, so that Quarto's rendering of shapes/talk.md cannot overwrite it. |
| [0006: The visual standard of the family](0006-the-visual-standard-of-the-family.md) | This repository is also the family's standard for the visual: figures and diagrams in any document, not only slides. |
| [0007: Diagrams are drawn with Graphviz](0007-diagrams-are-drawn-with-graphviz.md) | A diagram of relations in the family is written in Graphviz's dot language and kept beside the SVG it renders. |
