# State of the art, per sub-question

Two records are kept apart ([method](../README.md#method)): best evidence (a research record) and most adopted (a practice record). They have different holders.

## Best evidence

| Sub-question | Record holder | Measured how |
|---|---|---|
| Q1 Redundancy of on-screen text and speech | Adesope 2012 | meta-analysis, 57 studies, retention and transfer |
| Q1 Modality, segmenting | Ginns 2005; Rey 2019 | meta-analyses, system-paced lab lessons |
| Q1 Coherence, signalling | Sundararajan 2020; Schneider 2018 | meta-analyses (see learning science) |
| Q1 Does design matter more when pacing is fixed | Noetel 2022 | overview of 29 reviews, 1,189 studies; moderator "system-paced" |
| Q2 Does showing slides help | Baker 2018 | meta-analysis, 48 studies, no average difference |
| Q2 Which slide design | Garner 2013 | randomised experiment, n = 110, essay and delayed test, d about 0.8 to 0.9 |
| Q2 How common are slide faults | Kosslyn 2012; Le Blanc 2025 | three studies of slideshows; an audit of one medical school's lectures |
| Q3 Gesture | Dargue 2019; Hostetter 2011 | meta-analyses, 83 and 63 samples |
| Q3 Instructor visible in video | Henderson 2021; Polat 2022 | systematic reviews, 12 and 41 studies, no consistent learning effect |
| Q6 Does fixed pacing (20 by 20) raise learning | Bakcek 2020 | randomised trial, n = 134, test scores equal |
| Q4 Contrast floor | WCAG 2.2 (W3C 2023b) | standard (a convention), not an experiment |
| Q5 How talks are built | Rowley-Jolivet 2005 | move analysis of 44 talks in three fields |
| Q7 Build steps that follow the voice | Liu 2022; Ito 2026 | randomised, n = 99; n = 40 with eye tracking, d = 0.49; both recorded narration |
| Q7 Who sets the pace | Tabbers 2009 | learner-paced beat system-paced on transfer, at a large cost in time |
| Q7 Does video help | Noetel 2021 | 105 randomised trials, g = 0.28 as a substitute and 0.80 as an addition |
| Q7 Live coding against static code | Shah 2023; Shah 2025 | static code: two remote sections, no learning difference (Shah 2023); active against traditional live coding: about 530 students, no learning difference (Shah 2025) |
| Q7 Animated explainer against slides | Pichler 2023; Li 2023 | groups of 29 to 42; n = 290; engagement differs, comprehension mostly does not |
| Q8 Colour as a signal | Ozcelik 2009 | one eye-tracking experiment, n = 52 |
| Q8 Pleasant colours and faces | Brom 2018; Wong 2020 | meta-analyses, 33 samples and 28 articles, d+ 0.33 to 0.39 (Brom 2018), g+ 0.27 to 0.35 (Wong 2020) on retention and transfer |
| Q8 Colour maps for data | Crameri 2020; Liu 2018 | an argued guide with a distortion measure; a user study of colormaps |
| Q8 Light or dark when projected | Greco 2008 | three experiments, dark text on light best |
| Q8 Harmony | Schloss 2011 | preference experiments only |

## Most adopted

| Sub-question | Practice holder | Evidence of use |
|---|---|---|
| Slide template | PowerPoint, with Designer | Designer: over 1 billion slides, owner's claim (Microsoft 2019) |
| Typeset talks in computer science and mathematics | Beamer | a CTAN package with a long user guide; a usage count was not found |
| Short talks | TED and TEDx guidance; PechaKucha; Ignite | formats run in many cities; counts are the owners' claims (TED 2026, PechaKucha 2026 and Ignite 2026 score 9.5, 6 and 5.5 of 20: examples only) |
| Accessible talks | Rector 2019 and the conference guides derived from it | three conference pages seen citing it; no evidence cited by the guide |
| Replacing slides | Amazon narrative memo | one company's own report (Bezos 2018) |
| Headlines as sentences | Assertion-evidence workshops; consulting action titles | no count of users found |
| Build steps and Morph | PowerPoint's animation pane and Morph | a vendor page with no learning claim (Microsoft 2026e, 6 of 20: example only); no count of users |
| Live coding in teaching | Software Carpentry style workshops | a practice guide that says it is taught in instructor training (Nederbragt 2016, 11.5) |
| Animated maths videos | 3Blue1Brown and its Manim library | over 3.3 million views of one video (Radmehr 2024); the owner's aim (Sanderson 2026, 8: example only) |
| Colour defaults | the viridis family as a library default; the Okabe-Ito eight colours | a software manual (Matplotlib 2026, 14.5); the palette is copied from a column (Wong 2011) |
| Colour accessibility | WCAG 1.4.1 and the guides built on it | a standard (W3C 2023c, 17 of 20) |

## Upper bounds (achieved)

- Key points shown in step with the narration beat the whole slide in one randomised study (Liu 2022).
- Pleasant colours and faces gave small gains in retention and transfer across 33 samples (Brom 2018).
- A perceptually uniform map keeps data variation honest where a jet-like map distorts over 7% of it (Crameri 2020).

- A bundle of principles in a slide set raised delayed recall and essay quality in one lab setting (Garner 2013).
- Gesture helps comprehension across many samples (Dargue 2019).
- Verbatim text on screen with speech does not beat text alone (Adesope 2012).

## Lower bounds (not shown)

- No independent randomised replication of the assertion-evidence effect was found in this search. Closest: a non-randomised veterinary course with better retention at one month (Root Kustritz 2014), a bundled geology course (Alley 2007), and small studies (Alzayed 2023, Sripradith 2023) or pilots (Wolfe 2023).
- No study was found that varies one slide factor (headline form, text amount, graphic) in isolation within a live talk.
- No study was found of projected text size and comprehension in a room.
- No controlled comparison of a memo-first meeting against a slide meeting was found.
- The 20 by 20 and 15-second pacing rules have three small outcome studies (Liao 2020, Warmuth 2021, Bakcek 2020); the one randomised trial found no test-score gain. None tests Ignite's 15 seconds.
- No study was found of accessibility advice (say every slide word aloud) against the redundancy result for blind or low-vision listeners.
- No study was found of slide transitions, of an embedded clip in a live conference talk, of a live demo, or of build steps in front of a live audience.
- No live-coding study found a learning gain over static code (Shah 2023); active live coding did not beat traditional live coding (Shah 2025).
- Colour alone, without faces or shape, is 5 samples of 33 in the emotional-design meta-analysis (Brom 2018, Table 3); no isolated effect is established.
- No study of colour harmony and learning, of hue meaning on slides, or of projected colour at room distance was found.
