# Position

This file says what is known, what is not, and what this repository adds about figures and diagrams.

## Known

| Fact | Grade | Source |
|---|---|---|
| Fewer edge crossings help path finding in a node-link diagram | measured | Purchase 1997, Ware 2002, Störrle 2016b |
| When crossings remain, wide angles hurt less than narrow ones | supported with caveat | Huang 2008, Huang 2008b, Huang 2014 |
| Quantities are read more accurately by position on a common scale than by length, angle or circular area, in charts; angle was not worse than length | measured, for charts | Heer 2010 (Cleveland 1984 for the method) |
| Items inside one bounded region group together and can override proximity and similarity (not verified: whether measured or demonstrated; connectedness by a line not read) | convention | Palmer 1992 |
| Spatial compatibility between the data region and the legend shortened the time to read a graph (not verified: what compatible meant; not shown for direct labels) | supported with caveat | Huestegge 2011 |
| Beauty gives a small, uneven gain in task performance of interfaces | measured | Thielsch 2019, Schlamann 2026 |
| Holmes-style embellished charts were described as accurately and recalled better two to three weeks later (10 participants per recall condition, charts by one designer) | supported with caveat | Bateman 2010; Few 2011 restates it and criticises it |
| WCAG 2.2 treats ASCII art as non-text content, so it needs a text alternative; box-drawing characters fall under it only by extension of the glossary definition | convention | W3C 2023a, W3C 2023e |
| Mermaid can write an accessible title and description into its SVG | convention | Mermaid 2026c |
| GPT-4o answered most structure questions better from graph text than from an image alone (not cycle checks), on small random graphs | supported with caveat | Zhong 2024 |

## Not known

- Whether text art is read worse, or slower, than a drawn diagram by any reader. No study tests it.
- How screen-reader users fare on box-drawing diagrams; no test found.
- Which visual channels carry node type, link type and group best in a diagram.
- Whether alignment, proximity or a bounded region helps a node-link diagram, outside laboratory dot displays.
- Whether a flow direction (left to right or top to bottom) matters; one pilot found readers adapt.
- Whether appeal changes trust in a diagram; the trust studies use bar charts and infographics.
- Whether a language model reads a diagram better from source or from an image when the same authored diagram is given both ways (tested only on generated graphs, in Zhong 2024 and Das 2024).
- The gain from a diagram drawn from source over a typed one, for maintenance and for drift.

## Where practice runs ahead of the evidence

- Every style guide read (Urban 2025, FT 2026, Europa 2023, Rougier 2014) states rules on titles, labels, colour and decoration with no experiment behind most of them.
- "Remove decoration" is near-universal in guides, while the controlled studies are mixed on it.
- Diagrams as code are adopted widely (held: Mermaid and PlantUML counts), while the accessibility of what they emit is a documented option, not a tested one.
- Text art in code blocks is common in repositories; no source here measures its cost or benefit.

## Where the evidence is ignored by practice

- Wide crossing angles are measured results that none of the four guides read names; a common scale for quantities is named only through one Cleveland and McGill link in FT 2026.
- The accessibility standard already covers ASCII art; of the three tool pages read, GitHub 2026e and Quarto 2026 are silent on alt text for diagrams and Mermaid 2026c documents `accTitle` and `accDescr`.

## What this strand adds

- It joins four fields that are read apart: graph drawing aesthetics, graphical perception, appeal and trust, and accessibility of diagrams.
- It states that the case which triggered it, text art against a drawn diagram, has an accessibility argument (a standard and two advice pages) and no reading-speed evidence.
- It keeps what a program can check (contrast, alt text, crossings, text art) apart from what needs a reader.
- "Nobody has measured this" means none found in 31 searches on 2026-10-29. It does not mean no one has.
