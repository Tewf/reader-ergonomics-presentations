# Contexts are written as audiences

**Decided:** 2026-10-29, the maintainer.

## Context

An academic talk and a business pitch follow the same base with a few changes. reader-ergonomics already has a format for what overrides it: the reader style.

## Decision

Each context is a file in reader-styles/, named by its audience (academic audience, business decision maker, casual audience), with the format of reader-ergonomics' template: who, overrides, thresholds, open questions.

## Consequences

A context changes only what its evidence supports, and says so row by row. The extension contract needs no new mechanism.

## Alternatives rejected

- A principle per context: it would copy the base and blur what changes.
- Contexts named by event (pitch, defence, meetup): one audience meets several events, and the audience is what changes the rules.
