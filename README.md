# Academic writing and presentations

[![Checks against reader-ergonomics](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml/badge.svg?branch=master)](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/checks.yml?query=branch%3Amaster)
[![Site](https://github.com/Tewf/academic-writing-and-presentations/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/academic-writing-and-presentations/)

How to write research papers, mathematical articles and proofs, and how to build a presentation, so that they cost
the reader or the listener as little as possible.

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). The principles, their grades and the checks
live there and are not repeated here. This repository adds only what is particular to these genres: their evidence,
and the shapes of their documents.

> **Status:** work in progress. Three multivocal reviews are written in [evidence/](evidence/), and their numbers were
> audited on 2026-10-28; the shapes of a paper, an article and a proof exist, and the shape of a deck is not
> started. It is an informal reading of published research and practice: not an official standard, not a
> peer-reviewed study, not a new result, and not a claim to the state of the art.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. AI agents draft the literature reviews; every reference is resolved by script, and a
> number read only in a summary is marked "(secondary)". Corrections are welcome as issues.

## Contents

| Part | Holds | State |
|---|---|---|
| [evidence/](evidence/) | three reviews: research papers, mathematical writing, presentations | written, audited |
| [shapes/](shapes/) | the skeletons of a research paper, a mathematical article and a proof | written |
| shape of a deck | the skeleton of a talk's slides | not started |

The two parts were written on two branches in parallel and merged once each was audited.

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

CI runs the same checks on every push, and a run fails on any error ([checks.yml](https://github.com/Tewf/academic-writing-and-presentations/blob/master/.github/workflows/checks.yml)).
The badge at the top is the last result on master: the proof that this repository obeys the standard it extends. Every push to master also renders the site,
[tewf.github.io/academic-writing-and-presentations](https://tewf.github.io/academic-writing-and-presentations/)
([pages.yml](https://github.com/Tewf/academic-writing-and-presentations/blob/master/.github/workflows/pages.yml)).

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
