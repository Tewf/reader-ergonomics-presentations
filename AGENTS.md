# Contributing to this repository

For anyone changing this repository, person or language model. To give a talk, read [standard.md](standard.md)
instead; this file is about this repository only. It extends reader-ergonomics through the interface in that
repository's [extending.md](https://github.com/Tewf/reader-ergonomics/blob/v1.0.0/extending.md), and relies on
nothing else there.

## Before writing

1. Read reader-ergonomics' [standard.md](https://github.com/Tewf/reader-ergonomics/blob/v1.0.0/standard.md), then this
   repository's [standard.md](standard.md). A principle that reader-ergonomics holds is linked, never restated here.
2. A principle belongs here only when a talk changes it: the listener cannot set the pace, the room sets what is
   legible, the speaker is part of the medium.
3. An audience that changes a principle is a context in [reader-styles/](reader-styles/), not a new principle.

## Rules for claims

- The rules for claims are reader-ergonomics' own ([its AGENTS.md](https://github.com/Tewf/reader-ergonomics/blob/v1.0.0/AGENTS.md#rules-for-claims)):
  a grade on every principle, `Author Year` in the text, one entry in [evidence/bibliography.md](evidence/bibliography.md),
  evidence against kept in `against.md`, "(secondary)" for a number read in a summary.
- A new claim comes from the review in [evidence/presentations/](evidence/presentations/). A claim the review does not
  hold needs a review strand first, written to its protocol and audited.

## Before handing back

```sh
PYTHONPATH=<reader-ergonomics>/checks python3 -m unittest discover -s checks -p "test_*.py"   # the deck checks' tests
python3 <reader-ergonomics>/checks/run.py . --tiers program,meaning                           # the standard's checks and this repository's
python3 <reader-ergonomics>/checks/program/standard_card.py . --write                         # after a principle changes
```

- Fix every error. Fix every warning, or say in one line why it is a false match.
- Answer the judgment questions in `checks/judgments.toml`.
- A deck check lives in [checks/local/](checks/local/): a module with `NAME`, `EXACT` and `check(root, config)`, and a
  test in `checks/test_local_checks.py` that shows it fires on a deck breaking its rule and stays quiet on one keeping
  it. Its threshold goes in `checks/config.toml`, tagged PROVISIONAL until a study gives a number.

## The site

Every push to master renders the site with Quarto, with reader-ergonomics' stylesheet checked out at build time.
`standard.md` and `llms.txt` are built from the principle files; edit those, then rebuild.
