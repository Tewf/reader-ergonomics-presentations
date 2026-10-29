# 0004: Pin reader-ergonomics at a release

**Decision:** CI checks out reader-ergonomics by the commit of a release, and the text links name the same release.

**Status:** accepted, 2026-10-29. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/v1.18.2/shapes/decision-record.md).

## Context

This repository runs reader-ergonomics' checks and links its principles. Both change upstream.

## Decision

A tag can be moved, so CI checks out reader-ergonomics by the commit of a release. Text links name the same release (blob/<tag>), since a tag is readable and is never moved after it is published. The release in use is named in .github/workflows/checks.yml.

## Alternatives rejected

- Following master: any upstream commit could turn CI red or break a link with nothing changed here.
- Copying the standard in: every principle would live twice and drift.

## Consequences

An upstream change breaks nothing here until the pin is raised on purpose, in one commit that changes CI and links together.

## See also

[Decisions](README.md); [The workflow](../.github/workflows/checks.yml), reader-ergonomics' [extending.md](https://github.com/Tewf/reader-ergonomics/blob/v1.18.2/extending.md).
