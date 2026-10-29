# 0003: Decks are HTML, one section per slide

**Decision:** The deck checks read HTML decks whose slides are <section> elements and whose notes are <aside class="notes">.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/v1.12.0/shapes/decision-record.md).

## Context

Checks need a format they can read. PowerPoint and Keynote files are binary and closed. reveal.js and plain HTML decks share one convention: a slide is a <section>, speaker notes are an <aside class="notes">.

## Decision

The deck checks read HTML decks of that convention, named in checks/config.toml. The example deck follows it.

## Alternatives rejected

- Markdown slides only: reveal.js and many hand-made decks are HTML first.
- Reading .pptx: a closed format, and a dependency for every run.

## Consequences

A deck made in another tool is checked once exported to HTML, or not at all. A deck in a git-ignored folder is out of scope, and the deck-scope check says so rather than passing in silence.

## See also

[Decisions](README.md); [The checks](../checks/), [the example deck](../shapes/example-talk.html).
