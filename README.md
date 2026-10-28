# Academic writing and presentations

[![Checks, master](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml/badge.svg?branch=master)](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml?query=branch%3Amaster)
[![Checks, papers and proofs](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml/badge.svg?branch=academic-papers-and-proofs)](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml?query=branch%3Aacademic-papers-and-proofs)
[![Checks, presentations](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml/badge.svg?branch=presentations)](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml?query=branch%3Apresentations)
[![Site](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/academic-writing-and-presentations/)

How to write research papers, mathematical articles and proofs, and how to build a presentation, so that they cost
the reader or the listener as little as possible.

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). The principles, their grades and the checks
live there and are not repeated here. This repository adds only what is particular to these genres: their evidence,
and the shapes of their documents.

> **Status:** not started. Master holds only this page; the work is on two branches, merged here once audited. It
> will be an informal reading of published research: not an official standard, not a peer-reviewed study, not a new
> result, and not a claim to the state of the art.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. AI agents draft the literature reviews; every reference is resolved by script, and a
> number read only in a summary is marked "(secondary)". Corrections are welcome as issues.

## Two branches, in parallel

| Branch | Will hold | State |
|---|---|---|
| `academic-papers-and-proofs` | how research papers and mathematical articles are structured and read, with templates for a paper, an article and a proof | drafted in reader-ergonomics and moved here with its history; its numbers are not audited yet |
| `presentations` | what the evidence says about slides and talks, and the shape of a deck | not started |

## What presentations add, and what they do not

What is new in a talk:

- the listener cannot set the pace or reread, which brings in the modality, redundancy and segmenting principles;
- the speaker is part of the medium;
- the room sets legibility, since slides are read from a distance.

What is already in reader-ergonomics, such as signalling, a figure next to its text and typography, is linked, never
copied.

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push to every branch, and a run fails on any error
([checks.yml](.github/workflows/checks.yml)). The badges at the top are the last result on each branch: the proof that
this repository obeys the standard it extends. Every push to master also renders the site,
[tewf.github.io/academic-writing-and-presentations](https://tewf.github.io/academic-writing-and-presentations/)
([pages.yml](.github/workflows/pages.yml)); it grows as the branches are merged.

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
