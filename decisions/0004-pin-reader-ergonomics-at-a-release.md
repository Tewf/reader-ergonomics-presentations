# Pin reader-ergonomics at a release

**Decided:** 2026-10-29, the maintainer.

## Context

This repository runs reader-ergonomics' checks and links its principles. Both change upstream.

## Decision

CI checks out reader-ergonomics by the commit of a release (v1.0.0, 40cd9fb), since a tag can be moved. Text links name the same release (blob/v1.0.0), since a tag is readable and is never moved after it is published.

## Consequences

An upstream change breaks nothing here until the pin is raised on purpose, in one commit that changes CI and links together.

## Alternatives rejected

- Following master: any upstream commit could turn CI red or break a link with nothing changed here.
- Copying the standard in: every principle would live twice and drift.
