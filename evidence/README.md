# Evidence

One literature review per topic, in the steps reader-ergonomics uses for its own
[evidence](https://github.com/Tewf/reader-ergonomics/tree/master/evidence): frame, review, state of the art, position, the
case against, baseline. Every work cited is listed once in the [bibliography](bibliography.md).

| Topic | Question |
|---|---|
| [academic-papers](academic-papers/) | how a research article is ordered, what the evidence says about that order, and what templates enforce |
| [mathematical-writing](mathematical-writing/) | how a mathematical article and each proof in it should be laid out for the reader |

## Method

Each topic is a **multivocal literature review**: research and **grey literature** (standards, company
practice, templates, practitioner books and sites) in one review, built to a written protocol after
Garousi 2019. Two files in each topic make the review checkable and rerunnable:

| File | What it holds |
|---|---|
| `protocol.md` | why grey literature is included, the questions, every search string with its date and count, the stopping rule, the selection criteria |
| `sources.md` | every included source, how it was found, and its quality: the evidence grade for research, a score out of 20 for grey literature |

A grey source is scored on Garousi's 20 criteria, in eight groups. The `sources.md` tables abbreviate them: A authority
(of 4), M methodology (6), O objectivity (4), D date (1), P position among related sources (1), N novelty (2), I impact
(1), T outlet tier (1). Below 10 of 20 it may illustrate what practice does, but it never supports a claim.

The formal search of these two topics was narrative, with snowballing; their protocol files record its terms
and counts after the fact, and say so. The grey search was run to the protocol.

## Audit

On 2026-10-28, every line of the evidence files and shapes that carries a number was checked against its primary
source, and every DOI in the bibliography was resolved. Of 72 numeric lines: 53 correct, 11 imprecise, 5 unverifiable,
3 repeating a checked claim, 0 wrong. A second audit, on 2026-10-28, checked the 70 numeric lines added after the first:
50 correct, 14 imprecise, 2 unverifiable, 4 repeats, 0 wrong, all corrected or narrowed.

Every imprecise or unverifiable line was corrected, narrowed to what the source supports, or marked "(secondary)" or
"not checked", here and in the shapes that repeat it. Claims without a number have not been audited this way, so such a
claim is only as good as the review that cites it.
