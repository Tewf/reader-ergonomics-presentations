# Evidence

One literature review, on one topic, in the steps reader-ergonomics uses for its own
[evidence](https://github.com/Tewf/reader-ergonomics/tree/v1.4.1/evidence): frame, review, state of the art, position, the
case against, baseline. Every work cited is listed once in the [bibliography](bibliography.md).

| Topic | Question |
|---|---|
| [presentations](presentations/) | how slides and the spoken talk around them are built so a listener, who cannot set the pace, understands and remembers; since 2026-10-29 also business presentations (question 9) |

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

Each review keeps two records apart: **most adopted**, a practice record, and **best evidence**, a research record.
Practice counts as evidence only where a study measured its effect. The formal search of this topic was
narrative, with snowballing; their protocol files record its terms and counts after the fact, and say so. The grey
search was run to the protocol.

**Second rater.** A second rater re-scored, blind, every fifth grey source of the seven reviews then in this repository,
reader-ergonomics-academic and software-design-writing (38 of 175):

- inclusion: the raters agreed for 89.5% of the sample, Cohen's kappa 0.46, unstable at this size (bootstrap 0.00 to 0.87);
- totals: intraclass correlation ICC(A,1) 0.62, mean absolute difference 2.05 of 20, the second rater 1.8 points higher;
- four sources moved from below 10 to above it, and each stays an example of practice;
- the raters differed most on novelty, methodology and objectivity;
- outlet tier was not scored blind, and the first rater kept only the eight subtotals.

## Audit

The presentations review, its motion and colour questions included, was audited on 2026-10-28: 79 numeric lines,
54 correct, 9 imprecise, 10 unverifiable, 5 repeats and 1 wrong. Claims the audit could not verify were then read in
full text through a university's access; Savoy 2009 and Worthington 2015 were also confirmed by program against their
PDFs.

The business strand (question 9) was audited on 2026-10-29: 89 lines, 64 claims and 25 references, of which 67 correct,
16 imprecise, 5 unverifiable and 1 wrong. Ten of its sources wait for a reading in full text, since their full texts
are paywalled.

Every wrong, imprecise or unverifiable line was corrected, narrowed to what the source supports, or marked "(secondary)"
or "not verified". Claims without a number have not been audited this way, so such a claim is only as good as the review
that cites it.
