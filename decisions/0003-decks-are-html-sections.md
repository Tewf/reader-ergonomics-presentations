# Decks are HTML, one section per slide

**Decided:** 2026-10-29.

## Context

Checks need a format they can read. PowerPoint and Keynote files are binary and closed. reveal.js and plain HTML decks share one convention: a slide is a <section>, speaker notes are an <aside class="notes">.

## Decision

The deck checks read HTML decks of that convention, named in checks/config.toml. The example deck follows it.

## Consequences

A deck made in another tool is checked once exported to HTML, or not at all. A deck in a git-ignored folder is out of scope, and the deck-scope check says so rather than passing in silence.

## Alternatives rejected

- Markdown slides only: reveal.js and many hand-made decks are HTML first.
- Reading .pptx: a closed format, and a dependency for every run.
