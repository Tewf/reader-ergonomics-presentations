# 0005: The example deck is not named after its shape

**Decision:** The example deck is shapes/example-talk.html, so that Quarto's rendering of shapes/talk.md cannot overwrite it.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/v1.10.0/shapes/decision-record.md).

## Context

Quarto renders shapes/talk.md to shapes/talk.html inside the source folder before moving it to _site. On 2026-10-29 that overwrote a hand-made deck of the same name, on disk.

## Decision

The example deck is shapes/example-talk.html, with example-talk.css, listed as resources in _quarto.yml.

## Alternatives rejected

- Excluding the deck from rendering: the overwrite comes from talk.md's output, not from the deck.

## Consequences

No hand-made .html file may share its stem with a .md file in this repository.

The cost: the example's name no longer matches its shape's, so a reader looking for talk.html finds example-talk.html instead.

## See also

[Decisions](README.md); [The shapes](../shapes/).
