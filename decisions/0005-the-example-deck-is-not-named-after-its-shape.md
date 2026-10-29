# The example deck is not named after its shape

**Decided:** 2026-10-29.

## Context

Quarto renders shapes/talk.md to shapes/talk.html inside the source folder before moving it to _site. On 2026-10-29 that overwrote a hand-made deck of the same name, on disk.

## Decision

The example deck is shapes/example-talk.html, with example-talk.css, listed as resources in _quarto.yml.

## Consequences

No hand-made .html file may share its stem with a .md file in this repository.

## Alternatives rejected

- Excluding the deck from rendering: the overwrite comes from talk.md's output, not from the deck.
