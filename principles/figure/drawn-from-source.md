# Drawn from source

**Claim:** a page read on GitHub or on a site draws its figures from source files, a Graphviz `.dot` kept beside each SVG, and does not type them as text art. Text figures stay only in files read in a terminal or by a model.

- **Grade:** convention, untested. The reasons are access and drift, not faster reading.
- **Evidence:** [review, strand 4](../../evidence/figures/review.md); [position, Known](../../evidence/figures/position.md); [decision 0007](../../decisions/0007-diagrams-are-drawn-with-graphviz.md).
- **Check:** `typed-figure` (exact): a code block of box-drawing characters outside the exempt files; `figure-source` (exact): each SVG drawn from a `.dot` names the hash of the source it was rendered from.
- **Reader styles:** none changes it.

## What it asks

- Write a diagram of relations in Graphviz's dot language, render it to SVG, and embed the SVG in the page.
- Keep the `.dot` beside the SVG, under the same name, beside the page that embeds it and named after it; a folder of figures would group files by type. A model, a terminal and a later editor read the source; a person reads the drawing.
- Keep a text figure only where no drawing can be shown: AGENTS.md, llms.txt, a comment in code, a commit message. The exempt files are listed in `checks/config.toml`.
- Render with `python3 checks/render_figure.py FILE.dot`, which stamps the SVG with the hash of its source.

## Why

WCAG 2.2 counts ASCII art as non-text content, which needs a text alternative like any image (W3C 2023a). Its glossary names the 95 printable ASCII characters, so box-drawing characters fall under it by extension. Screen readers read such a figure character by character (CUNY 2026).

A model reads a graph better from text than from an image: GPT-4o found an edge in 96.2% of cases from an adjacency list, against 74.6% from a picture (Zhong 2024). Turning a flowchart into Graphviz or Mermaid source before reasoning on it beat end-to-end models (Ye 2025). The `.dot` file gives a model that text form.

## Limits

- No study compares a text figure with a drawn one, for sighted readers or for screen-reader users.
- A drawn figure can drift from its source. The hash stamp catches that; a figure edited by hand cannot be checked.
- The rule was set by the maintainer on 2026-10-29, after reader-ergonomics argued that a text figure reads in a terminal and to a model exactly as it is drawn. The exempt files answer the first point and the `.dot` source the second.
