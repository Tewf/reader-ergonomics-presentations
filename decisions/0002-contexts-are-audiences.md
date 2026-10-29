# 0002: Contexts are written as audiences

**Decision:** Each context is a reader style named by its audience, so an academic talk, a business pitch and a casual talk override the base without a new mechanism.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/v1.13.0/shapes/decision-record.md).

## Context

An academic talk and a business pitch follow the same base with a few changes. reader-ergonomics already has a format for what overrides it: the reader style.

## Decision

Each context is a file in reader-styles/ named by its audience: academic audience, business decision maker, casual audience. It has the format of reader-ergonomics' template: who, overrides, thresholds, open questions.

## Alternatives rejected

- A principle per context: it would copy the base and blur what changes.
- Contexts named by event (pitch, defence, meetup): one audience meets several events, and the audience is what changes the rules.

## Consequences

A context changes only what its evidence supports, and says so row by row. The extension contract needs no new mechanism.

The cost: no single context fits a talk to two audiences at once, such as a defence before a jury and guests.

## See also

[Decisions](README.md); [The contexts](../reader-styles/).
