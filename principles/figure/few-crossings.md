# Few crossings

**Claim:** in a node-link diagram, links cross as little as possible, and crossings that remain meet near a right angle.

- **Grade:** supported with caveat (small samples; one study against).
- **Evidence:** [review, strand 1](../../evidence/figures/review.md); [against, Crossings](../../evidence/figures/against.md).
- **Check:** `figure-judgment` (judgment): do links cross where a layout could avoid it?
- **Reader styles:** none changes it.

## What it asks

- Let a layered layout place the nodes; Graphviz's `dot` orders them to reduce crossings.
- Where a crossing remains, make it meet near 90 degrees.
- Split a diagram that cannot be drawn without many crossings.

## Why

Of five layout aesthetics, fewer crossings had the largest effect on understanding (Purchase 1997). After path length, continuity and crossings cost most in path finding (Ware 2002). Path tracing slowed as the crossing angle narrowed and levelled off near 90 degrees (Huang 2008b, 22 participants; Huang 2014, 37 participants, both per Burch 2021).

## Limits

- One study of 26 participants found layouts with crossings fastest for interpretation tasks, while readers preferred none (Burch 2021).
- The studies use students and small graphs; none tests a diagram in documentation.
