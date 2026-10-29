# Presentations

[![Checks against reader-ergonomics](https://github.com/Tewf/reader-ergonomics-presentations/actions/workflows/checks.yml/badge.svg?branch=master)](https://github.com/Tewf/reader-ergonomics-presentations/actions/workflows/checks.yml?query=branch%3Amaster)
[![Site](https://github.com/Tewf/reader-ergonomics-presentations/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-presentations/)

How to build a presentation so that the listener, or the reader of a deck, follows and remembers it at the least cost.

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). The principles, their grades and the checks
live there and are not repeated here. This repository adds only what is particular to presentations.

> **Status:** parked. The evidence is written and audited. The principles, the two contexts and the shape of a deck
> are not started, and nothing more is built until the maintainer settles the scope. It is an informal reading of
> published research and practice: not an official standard, not a peer-reviewed study, not a new result, and not a
> claim to the state of the art.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. AI agents draft the literature reviews; every reference is resolved by script, and a
> number read only in a summary is marked "(secondary)". Corrections are welcome as issues.

## Scope

One base, and two contexts that override it, the way a reader style overrides the standard:

```text
presentations
 ├─ the base: what a presentation is      a paced medium, a speaker, a room
 └─ contexts that override the base
    ├─ the academic talk                  conference, seminar, defence
    └─ the business presentation          pitch, sale, executive briefing
```

## Contents

| Part | Holds | State |
|---|---|---|
| [evidence/](evidence/) | one multivocal review in nine questions, from the voice and the slide to motion, colour and business presentations; 171 works | written, audited |
| principles and contexts | the base, and what each context overrides | not started; candidate overrides in [position.md](evidence/presentations/position.md) |
| shape of a deck | the skeleton of a talk's slides | not started |

## What a presentation adds, and what it does not

What is new in a talk:

- the listener cannot set the pace or reread, which brings in the modality, redundancy and segmenting principles;
- the speaker is part of the medium;
- the room sets legibility, since slides are read from a distance.

What is already in reader-ergonomics, such as signalling, a figure next to its text and typography, is linked, never
copied.

## Where it came from

It began on 2026-10-28 as the talk half of reader-ergonomics-academic, and moved here on 2026-10-29 with its history. The two
halves had grown apart: when they split, their reviews cited 147 and 225 works, and shared 2.

## Check it

```sh
git clone https://github.com/Tewf/reader-ergonomics
python3 reader-ergonomics/checks/run.py path/to/this/repository
```

CI runs the same checks on every push, and a run fails on any error
([checks.yml](https://github.com/Tewf/reader-ergonomics-presentations/blob/master/.github/workflows/checks.yml)). The badge at the top is
the last result on master. Every push to master also renders the site,
[tewf.github.io/reader-ergonomics-presentations](https://tewf.github.io/reader-ergonomics-presentations/)
([pages.yml](https://github.com/Tewf/reader-ergonomics-presentations/blob/master/.github/workflows/pages.yml)).

## Licence

Code under the [Apache License 2.0](LICENSE); prose under [CC BY 4.0](LICENSES/CC-BY-4.0.txt). Reuse it as you wish, with
credit to this repository; [CITATION.cff](CITATION.cff) gives a citation if you need one.
