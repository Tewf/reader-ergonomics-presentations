# Presentations

[![Checks against reader-ergonomics](https://github.com/Tewf/reader-ergonomics-presentations/actions/workflows/checks.yml/badge.svg?branch=master)](https://github.com/Tewf/reader-ergonomics-presentations/actions/workflows/checks.yml?query=branch%3Amaster)
[![Site](https://github.com/Tewf/reader-ergonomics-presentations/actions/workflows/pages.yml/badge.svg)](https://tewf.github.io/reader-ergonomics-presentations/)

How to build a presentation so that the listener, or the reader of a deck, follows and remembers it at the least cost.

It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics). The principles, their grades and the checks
live there and are not repeated here. This repository adds only what is particular to presentations.

> **Status:** work in progress. The [standard](standard.md) has nine principles, three contexts and the shape of a
> talk, with an example deck and seven checks that run on decks. It has been tested on two real talks, an academic and a
> business one, which changed the checks; a casual test is under way. It is an informal reading of
> published research and practice: not an official standard, not a peer-reviewed study, not a new result, and not a
> claim to the state of the art.
>
> **How it is made:** with Claude, an AI assistant by Anthropic, under the maintainer's direction, the way
> reader-ergonomics was made. AI agents draft the literature reviews; every reference is resolved by script, and a
> number read only in a summary is marked "(secondary)". Corrections are welcome as issues.

## Scope

One base, and contexts that override it, the way a reader style overrides the standard. Anyone's own way of
presenting is a style of its own, kept by them, that overrides this standard in turn.

```text
presentations
 ├─ the base: what a presentation is
 │    a paced medium, a speaker, a room
 └─ contexts that override the base
    ├─ the academic talk
    │    conference, seminar, defence
    ├─ the business presentation
    │    pitch, sale, executive briefing
    └─ the casual talk
         meetup, club, friends
```

## Contents

| Part | Holds | State |
|---|---|---|
| [standard.md](standard.md) | the card: how to use the standard, and every principle with its grade | written |
| [principles/](principles/) | nine principles in three groups: pace, slide, talk | written; not yet tested on a real talk |
| [reader-styles/](reader-styles/) | the contexts, as audiences: academic, business, casual | written |
| [shapes/](shapes/) | the talk shape, and an example deck in HTML that obeys it | written |
| [checks/](checks/) | seven checks that run on HTML decks, with their tests | written |
| [decisions/](decisions/) | the choices that shaped this repository, one record each | five records |
| [evidence/](evidence/) | one multivocal review in nine questions, from the voice and the slide to motion, colour and business presentations; 172 works | written, audited |

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
