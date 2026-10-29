# Baseline: what the presentation rules are compared against

This file names the deck a proposed presentation design must beat, and how the two would be compared.

## The named baseline

**The default deck:** a template slide with a topic-phrase headline over a bulleted list, about 40 words per slide, shown while the speaker narrates. It is the "common practice" arm of Garner 2013 (41.5 words per slide, topic phrase over bullets).

The stronger comparator is the **assertion-evidence deck** of the same study: a sentence headline of at most two lines, a graphic that is the evidence, 21.2 words per slide.

Two further reference points, for practice:

- Beamer 2026 defaults and its advice (20 to 40 words, phrases over sentences).
- The built-in checks of Microsoft (titles, reading order, contrast, 18 point text; Microsoft 2026d scores 8.5 of 20, an example of practice).
- A society limit for contrast (SSP 2026, 9 of 20, example only): a title of at most 6 words and 6 lines of 7 words. It disagrees with the sentence headline of two lines.

## How a comparison would be measured

| Item | Choice | Prior study that used it |
|---|---|---|
| Design | random assignment of listeners to decks; same script, same speaker or same recording | Garner 2013 |
| Talk | a technical talk of 8 minutes or longer, on a topic new to the audience | Garner 2013 |
| Outcome 1 | essay of the process, scored with an analytic rubric by two raters, misconceptions counted | Garner 2013 |
| Outcome 2 | immediate multiple choice split into facts, process, inference | Garner 2013 |
| Outcome 3 | delayed sentence completion after about one week, unannounced | Garner 2013 |
| Outcome 4 | retention and transfer at 1 and 4 weeks | Issa 2013 |
| Load | self-rated mental effort, 7 points | Garner 2013 |
| Statistic | Cohen's d with an interval; report d for each outcome | Garner 2013 |
| Check on preference | rating of appropriateness of text on slides | Garner 2013 |
| Motion arm | the same narration with key points shown in step against the whole slide at once; eye tracking where possible | Liu 2022; Ito 2026 |
| Engagement beside comprehension | rate both, since they can diverge | Li 2023 (secondary); Guo 2014 |
| Colour arm | the same slide with colour coding against monochrome, or one palette against another, in the same words | Ozcelik 2009; Brom 2018 |
| Control for prior knowledge | self-rating or pre-test | Garner 2013 |

- Not yet run by this repository: no comparison of its own rules against the baseline exists.
- Isolating one factor needs a design with more arms (headline form, text amount, graphic), which no prior study was found to have done.

## Checklist (rules a program can test)

Grades: **convention** means a number agreed by a body or by practice, **measured** means a study found the effect.

| Rule | Source | Grade |
|---|---|---|
| Every slide has a unique, non-empty title | Access Board 2017 (via WCAG); Microsoft 2026d (example only) | convention |
| Text contrast at least 4.5:1, or 3:1 for text of 18 point or larger | W3C 2023b (WCAG 2.2) | convention |
| Body text 18 point or larger on a 16:9 slide, or at most 20 lines per slide | Beamer 2026; Microsoft 2026d and ACM 2026 (examples only); SSP 2026 differs (1/40 of slide height) | convention, untested at distance |
| At most about 40 words per slide, 80 as a ceiling | Beamer 2026; Garner 2013 (21 against 41) | convention; one study measured |
| Not more than one slide per minute | Beamer 2026 | convention |
| Headline states the claim as a sentence of at most two lines | Garner 2013; Alley 2013 | supported with caveat |
| Each slide has a figure or table that is the evidence | Garner 2013; [draw relations](https://github.com/Tewf/reader-ergonomics/blob/v1.13.0/principles/page/draw-relations.md) | supported with caveat |
| Words beside the figure they explain | [figure next to its text](https://github.com/Tewf/reader-ergonomics/blob/v1.13.0/principles/page/figure-next-to-its-text.md) | measured |
| No decorative images without a purpose | Sundararajan 2020 | measured |
| Alt text on every figure; reading order set | Rector 2019 (text equivalents for informative graphics); Microsoft 2026d (example only) | convention |
| Colour is never the only cue: the slide stays readable in greyscale | W3C 2023c; Rector 2019; Microsoft 2026d | convention |
| No rainbow or jet map for ordered data; a perceptually uniform map instead | Crameri 2020; Borland 2007; Matplotlib 2026 | convention, argued; one model finds a use for rainbow (Reda 2021) |
| A palette of at most 4 to 6 colours, one colour per category, in a fixed order | ScotGov 2024; Bramble 2026 (three colours) | convention |
| Dark text on a light ground by default | Greco 2008; Beamer 2026 | measured (three experiments); advice for dark rooms differs |
| No movement that starts alone, lasts over 5 seconds and sits beside other content without a way to stop it | W3C 2023d | convention |
| No transition other than none or one plain kind used throughout | Beamer 2026 | convention, untested |

## Checklist (rules a person judges)

1. One thing to remember is stated in the first minutes (Peyton Jones 1993; TED 2026, example only).
2. On-screen text adds to the voice instead of repeating it; key terms on screen, not the script (Adesope 2012, Yue 2013).
3. Long material is split into segments (Rey 2019).
4. Point at what you discuss; gesture to the figure (Hostetter 2011, Dargue 2019).
5. Say what the evidence is and where it is weak.
6. Leave time to take questions; a Q&A needs its own plan (Xu 2022).
7. Handout: the paper or a document of its own, not the slides read as notes (Worthington 2015).
8. Test the room: read the farthest seat in rehearsal (TED 2026, example only).
9. Describe a diagram aloud when its content is not in your words (Rector 2019); untested against the redundancy result (Adesope 2012).
10. Show key points in step with what you say, and animate a change, not decoration (Liu 2022, Ito 2026; Beamer 2026).
11. Check the deck for colour-vision deficiency with a simulator or a greyscale view (ACM 2026, Microsoft 2026d).
12. Demo only what shows moving parts; script it, and keep a recording ready (Nederbragt 2016; LornaJane 2017, example only). Live coding has not been shown to teach more than static code (Shah 2023).
13. Keep embedded clips short and put an educational one in the middle (Ljubojevic 2014); test the file on the room computer.
