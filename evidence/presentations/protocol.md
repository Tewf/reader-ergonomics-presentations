# Protocol

This file records how the pool of sources for this topic was built, so that the search can be repeated.

It follows Garousi 2019 for a multivocal literature review (MLR, defined in the [evidence README](../README.md)) in a lighter form.

Garousi 2019 was written for software engineering. Its guidelines are applied here to presentations, a field with a large teaching and speaking practice beside its research. The formal pool predates the protocol, and this file says so.

## 1. Why grey literature (Garousi Table 4, seven questions)

| # | Question | Answer for presentations |
|---|---|---|
| 1 | Complex subject, not solvable by the formal literature alone | yes: speaker, room and format rules are mostly practice |
| 2 | Lack of volume, quality or consensus of evidence | yes: few live-talk studies, bundled factors |
| 3 | Context matters | yes: audience, length, room, field |
| 4 | Goal to check research against practical experience | yes |
| 5 | Goal to challenge practice rules with research | yes: 30 point, 10 minutes, 3 seconds |
| 6 | Synthesis useful to both communities | yes |
| 7 | Many practitioner sources | yes: every grey string returned speaker guides and workshops |

Seven of seven are yes, so grey literature is included. The same seven answers hold for Q7 (motion) and Q8 (colour): palettes, builds, demos and video style are mostly practice, and the experiments are few and small.

## 2. Questions

- Q1 Does on-screen text that repeats the voice help or hurt, and which principles apply to a paced medium?
- Q2 Does showing slides help, and which slide design helps?
- Q3 What does the speaker add: gesture, face, enthusiasm?
- Q4 What makes slides legible and accessible in a room?
- Q5 How are talks built, and how do questions and discussion work?
- Q6 What does practice recommend and adopt, and how does it compare with Q1 to Q5?
- Q7 Motion in a talk: slide builds and transitions, animated diagrams, embedded video, explainer video in the style of mathematical animation, live demos and live coding, lecture-video design.
  - Its core: what changes when a speaker paces the motion.
- Q8 Colour: colour coding as a signal, emotional design with pleasant colours, colour in data figures, colour-vision deficiency and safe palettes, light against dark when projected, colour harmony, and what practice advises.

## 3. Existing reviews (Guideline 2)

| Id | String, as run | Results screened | Included |
|---|---|---|---|
| E1 | systematic review meta-analysis PowerPoint slides student learning outcomes | 10 | 0 |
| E2 | meta-analysis multimedia learning principles review of reviews Mayer | 10 | 2 (Noetel 2022, Cromley 2025) |
| E3 | systematic review scientific conference presentations oral presentation slides effectiveness | 9 | 1 (Blome 2017) |
| E4 | meta-analysis instructor visibility lecture video learning outcomes 2022 2023 2024 | 10 | 3 (Polat 2022, Zhu 2024, Heidig 2024) |
| E5 | scoping review slide design PowerPoint lectures higher education text density images | 9 | 0 (Le Blanc 2025 came through G4) |
| E6 | meta-analysis teacher gestures learning students instruction | 9 | 0 |
| E7 | `systematic review OR meta-analysis animation versus static slides presentation learning builds progressive disclosure` | 10 | 0 (animation reviews already held in the linked learning-science review) |
| E8 | `meta-analysis video lectures learning higher education systematic review lecture video design` | 9 | 1 (Noetel 2021) |
| E9 | `live coding versus static slides teaching programming study learning outcomes` | 9 | 2 (Shah 2023, Shah 2025) |
| E10 | `Live Coding: A Review of the Literature Selvaraj ITiCSE 2021` | 9 | 1 (Selvaraj 2021) |
| E11 | `systematic review color coding signaling multimedia learning color as cue meta-analysis` | 9 | 0 (Richter 2016, Schneider 2018 and Noetel 2022 already held) |
| E12 | `experiment sequential bullet points reveal versus all at once slides recall learning "build" animation PowerPoint study` | 10 | 2 (Ito 2026, Liu 2022) |
| E13 | `explainer video animation versus slides lecture learning engagement evidence whiteboard animation study` | 10 | 2 (Li 2023; Pichler 2023 as grey) |

Engine for E, F and G strings: a general web search tool (one engine, US-based, returns a summary and links), run on 2026-10-28. E7 to E13 screened 66 results.

## 4. Formal search

- The formal pool was built by a narrative search plus snowballing (frame.md lists the terms), not by screening database counts. The counts below only describe the terms.
- Query form: `https://api.openalex.org/works?filter=title_and_abstract.search:<terms>&per_page=1`, field `meta.count`, run 2026-10-28.
- These ten were run with the words unquoted, so each count is "all words anywhere in title or abstract", not a phrase. The count for assertion-evidence is mostly noise from the two common words.

| Terms | Count |
|---|---|
| multimedia learning principles | 4474 |
| cognitive theory of multimedia learning | 3223 |
| cognitive load theory | 12466 |
| redundancy effect | 17159 |
| assertion-evidence | 20927 |
| instructor presence | 5778 |
| gesture comprehension meta-analysis | 27 |
| conference presentation genre | 824 |
| conference presentation | 160781 |
| discussion sessions | 68325 |

- Not run: the other terms of frame.md (PowerPoint, slide design, pedagogical agent, split attention, modality, segmenting, the acronyms and the author names). The service answered HTTP 429 after these ten, with a retry delay of about five hours.
- Snowballing: forward from Garner 2013 (41 citing records when listed in an earlier session; 4 kept: Wolfe 2023, Wolfe 2025, Alzayed 2023, Sripradith 2023). In this round, backward from Bramble 2026 (strings F1, F2 below): 2 kept (Alley 2007, Root Kustritz 2014).

| Id | String, as run | Screened | Included |
|---|---|---|---|
| F1 | Diesel assertion-evidence geoscience lecture slides test scores study | 10 | 2 (Alley 2007, Root Kustritz 2014) |
| F2 | Wolfe assertion-evidence slides computer science course exam scores study | 9 | 0 (no computer science exam study found) |

### Formal search for Q7 and Q8 (2026-10-28)

- OpenAlex, the database of the first round, answered HTTP 429 (daily budget used) for every request of this round. The new strings were counted there on 2026-10-29 instead, as quoted phrases (the table after the one below).
- Two other databases that answer without an identity were used.
  - ERIC (`https://api.ies.ed.gov/eric/`, field `numFound`): phrase and Boolean search over all fields, education only.
  - The arXiv API (field `totalResults`): titles and abstracts, computer science and physics side. The first 10 results of each string, in the database's own order, were screened by title.
- Not run: Scopus and Web of Science (no access); a database of the psychology of colour or of visualization papers outside arXiv. Visualization and colour-science work reached the pool through the grey strings and through citations, not through a database count.

| Id | String, as run | Database | Count | Screened | New included |
|---|---|---|---|---|---|
| H1 | `"color coding" AND "multimedia learning"` | ERIC | 3 | 3 | 1 (Ozcelik 2009) |
| H2 | `"emotional design" AND ("multimedia learning" OR "color" OR "colour")` | ERIC | 28 | 10 | 4 (Mutlu-Bayraktar 2024, Desiron 2026, Um 2012, Meusel 2024) |
| H3 | `"pleasant colors" OR "warm colors" OR "aesthetic colors" OR "warm colours"` | ERIC | 17 | 10 | 0 |
| H4 | `"video production" AND "engagement" AND (lecture OR MOOC OR "instructional video")` | ERIC | 4 | 4 | 0 (Guo 2014 already known) |
| H5 | `"color" AND "signaling" AND ("meta-analysis" OR "systematic review")` | ERIC | 1 | 1 | 0 |
| H6 | `("color vision deficiency" OR "color blindness" OR "colour blindness" OR "color-blind") AND (slides OR presentation OR visualization OR learning)` | ERIC | 75 | 10 | 0 (race-equity papers and single-course notes) |
| H7 | `"background color" AND (learning OR slides OR presentation OR multimedia)` | ERIC | 14 | 10 | 1 (Clariana 2009) |
| H8 | `"color" AND ("presentation slides" OR PowerPoint) AND (legibility OR contrast OR readability OR polarity)` | ERIC | 2 | 2 | 0 |
| H9 | `"color harmony" OR "colour harmony"` | ERIC | 9 | 9 | 0 (art-class and interior-design items) |
| H10 | `("dark mode" OR "dark background" OR "negative polarity") AND (reading OR slides OR presentation)` | ERIC | 4 | 4 | 0 |
| M1 | `PowerPoint AND (animation OR animations OR "slide transitions" OR "progressive disclosure")` | ERIC | 58 | 10 | 2 (Miller 2011, Meij 2021) |
| M2 | `"video lectures" AND ("systematic review" OR "meta-analysis")` | ERIC | 2 | 2 | 2 (Tharumalingam 2025, Kuang 2023) |
| M3 | `"lecture video" AND (production OR "talking head" OR "picture-in-picture" OR "Khan Academy" OR "pen tablet")` | ERIC | 5 | 5 | 0 |
| M4 | `"live coding"` | ERIC | 12 | 10 | 2 (Shah 2025, Lin 2022) |
| M5 | `("live demonstration" OR "live demo" OR "classroom demonstration") AND lecture` | ERIC | 10 | 10 | 0 (classroom science demonstrations, no talk) |
| M6 | `animation AND "meta-analysis" AND (multimedia OR learning)` | ERIC | 13 | 10 | 0 (animation reviews already held, linked) |
| M7 | `"mathematical animation" OR "3Blue1Brown" OR "Manim"` | ERIC | 4 | 4 | 3 (Bos 2025, Voorde 2024, Radmehr 2024) |
| M8 | `live AND recorded AND lecture AND (learning OR performance)` | ERIC | 38 | 10 | 1 (Zureick 2017) |
| M9 | `animation AND pacing AND "learner control"` | ERIC | 5 | 5 | 2 (Tabbers 2009, Hatsidimitris 2012) |
| M10 | `"embedded video" OR "video clips" AND (lecture OR presentation) AND learning` | ERIC | 38 | 10 | 1 (Ljubojevic 2014) |
| V1 | `ti:"color map" OR abs:"rainbow colormap" OR abs:"rainbow color map"` | arXiv | 23 | 8 | 0 (mathematics and vision papers) |
| V2 | `abs:"color vision deficiency" AND abs:visualization` | arXiv | 11 | 8 | 2 (Nunez 2018 through its preprint, Petroff 2021) |
| V3 | `abs:"perceptually uniform" AND abs:colormap` | arXiv | 3 | 3 | 0 |

The same strings in OpenAlex, counted on 2026-10-29 (H1 to H10 and M1 at 00:06 UTC, M2 to V3 at 10:12 UTC), each phrase quoted:

| Id | OpenAlex count |
|---|---|
| H1 | 11 |
| H2 | 279 |
| H3 | 775 |
| H4 | 43 |
| H5 | 172 |
| H6 | 969 |
| H7 | 413 |
| H8 | 305 |
| H9 | 1 340 |
| H10 | 489 |
| M1 | 1 384 |
| M2 | 35 |
| M3 | 39 |
| M4 | 1 220 |
| M5 | 457 |
| M6 | 66 |
| M7 | 262 |
| M8 | 1 225 |
| M9 | 15 |
| M10 | 824 |
| V1 | 4 613 |
| V2 | 83 |
| V3 | 23 |

The first-round terms were counted again the same day as quoted phrases, which a phrase count must be compared with; the
counts in the first table are loose words and stay as they were:

| Terms | OpenAlex count as a phrase |
|---|---|
| multimedia learning principles | 245 |
| cognitive theory of multimedia learning | 1 428 |
| cognitive load theory | 6 148 |
| redundancy effect | 223 |
| assertion-evidence | 78 |
| instructor presence | 568 |
| gesture AND comprehension AND meta-analysis | 27 |
| conference presentation genre | 5 |
| conference presentation | 26 127 |
| discussion sessions | 3 302 |

- Totals for H, M, V: 158 results screened, 21 formal sources included.
- Found by other routes: Brom 2018, Wong 2020, Plass 2014, Harrower 2003, Borland 2007, Crameri 2020 and Guo 2014 (all named in the question).
- Also found by other routes: Brame 2016, Liu 2018, Reda 2021, Birch 2012, Wong 2011, Schloss 2011, Palmer 2010, Bramao 2011 and Greco 2008 (from grey strings and citations).
- With E7 to E13 and the strings above, 43 formal sources were added in this round.
- Snowballing: backward from Brom 2018 (read in the author's copy of the accepted manuscript) for the colour-only subgroup and the exclusions; backward from Crameri 2020 for the prevalence estimate. Forward snowballing was not run (no citation index without an identity).

## 5. Grey search

Types and producers, with the reason for each (Guideline 6):

| Type | Producers | Why |
|---|---|---|
| Speaker guidance | TED and TEDx | the largest talk programme |
| Conference and society speaker guides | scientific societies, ACM events, USENIX | the rules authors of papers receive |
| Accessibility guides | ACM SIGACCESS, ACM events | access to a paced medium |
| University teaching centres | UNB, others | rules for lecturers |
| Practitioner books and sites | Duarte, Reynolds, Leonhard Center | the most read design advice |
| Formats | PechaKucha, Ignite, Lessig method | pace fixed by rule |
| Company practice | Amazon memos | replacing slides |

Strings, N = 10 results screened per string (title and the engine's summary); pages opened in full are counted apart.

| Id | String, as run | Screened | Opened | New included |
|---|---|---|---|---|
| G1 | TEDx speaker guide slides presentation tips | 9 | 1 | 0 (TED 2026 re-found) |
| G2 | scientific conference oral presentation guidelines for speakers slides society | 10 | 1 | 1 (SSP 2026); IEEE guide not read, certificate error |
| G3 | accessible presentation guidelines slides conference speakers | 10 | 1 | 1 (ACM 2026) |
| G4 | teaching center lecture slides design principles evidence-based | 10 | 2 | 2 (Bramble 2026, Le Blanc 2025) |
| G5 | assertion-evidence slide design workshop guide scientists | 10 | 1 | 0 (Leonhard Center 2026 re-found) |
| G6 | Amazon six-page narrative memo meetings instead of PowerPoint study hall | 10 | 0 | 0 (Bezos 2018 re-found) |
| G7 | how to give a good talk slides advice computer science researchers guide | 10 | 0 | 0 |
| G8 | PechaKucha Ignite 20 slides format presentation learning effectiveness study | 10 | 3 | 3 formal (Liao 2020, Warmuth 2021, Bakcek 2020) |
| G9 | Rector accessible presentation guide SIGACCESS slides speakers | 10 | 1 | 1 (Rector 2019) |
| G10 | Lessig method presentation style one word per slide origin Takahashi | 10 | 0 | 0 |
| G11 | ACM SIGPLAN OR USENIX OR NeurIPS conference talk instructions for speakers slides guidance | 40 | 0 | 0 |
| G12 | Garr Reynolds Presentation Zen design principles restraint simplicity naturalness slides | 10 | 0 | 0 |
| G13 | `colorblind safe palette slides presentation accessible colors guide` | 9 | 0 | 0 (a science-communication palette PDF was not reachable) |
| G14 | `best colors for presentation slides dark background versus light background projector room lighting` | 9 | 1 | 1 (Schwabish 2014); a Tufte page on projection backgrounds returned HTTP 403, unread |
| G15 | `color theory harmony complementary analogous palette for presentation slides designer advice` | 10 | 1 | 1 (Ethos3 2026) |
| G16 | `rainbow colormap harmful viridis perceptually uniform scientific visualization guide` | 10 | 1 | 1 (EU 2023); Liu 2018 and Reda 2021 found |
| G17 | `Okabe Ito colorblind friendly palette color universal design guide scientific figures` | 9 | 0 | 0 (the original page is gone; Wong 2011 found) |
| G18 | `data visualisation colour guidance government analysis function palette categorical sequential diverging` | 9 | 1 | 1 (ScotGov 2024) |
| G19 | `PowerPoint animation best practices presentation builds Morph transition when to use evidence` | 9 | 1 | 1 (Microsoft 2026b) |
| G20 | `live demo conference talk advice pre-recorded video versus live demonstration technical presentation` | 10 | 2 | 2 (LornaJane 2017, Mozilla 2026) |
| G21 | `Brame effective educational videos principles guidelines Vanderbilt Center for Teaching` | 10 | 0 | 0 (Brame 2016 taken as formal) |
| G22 | `Grant Sanderson 3Blue1Brown Manim animation explain mathematics why animate talk interview process` | 10 | 1 | 1 (Sanderson 2026) |
| G23 | `live coding in lectures and talks tips font size zoom practice typos instructors guide` | 9 | 1 | 1 (Nederbragt 2016) |
| G24 | `embedding video clips in a conference presentation tips autoplay backup audio codec speaker guide` | 9 | 0 | 0 |
| G25 | `slide transitions and animations distract audience presentation advice avoid fly-in effects` | 9 | 0 | 0 |
| G26 | `lecture capture live versus recorded lectures advice for instructors recording talks pre-record` | 9 | 0 | 0 |
| G27 | `color psychology meaning red green blue presentation slides evidence debunked cultural` | 10 | 0 | 0 |
| G28 | `how many colors in a chart limit categorical palette direct labeling legend advice` | 10 | 0 | 0 (vendor design-system pages repeating one another) |
| G29 | `legibility projected slides text and background color combinations study yellow on blue white on dark` | 9 | 0 | 0 (Greco 2008 found) |
| G30 | `color blindness simulator tools Color Oracle Coblis check slides and figures before presenting` | 10 | 0 | 0 |
| G31 | `use one accent color to highlight on slides gray everything else emphasis color presentation design` | 9 | 0 | 0 |

- Added directly, not through a string: Wilke 2019 and Matplotlib 2026 (named practitioner references for colour in figures).
- Also added directly: W3C 2023b and W3C 2023c (the WCAG criteria on moving content and on colour).
- Pichler 2023 and Simpleshow 2021 came through E13.
- Totals for G13 to G31: 179 results screened, 15 pages opened in full, 15 new grey sources (7 under 10 of 20). The advice on colour and animation in already scored sources was read again.
  - Beamer 2026, Bramble 2026, Rector 2019, ACM 2026, Microsoft 2026, SSP 2026 and TED 2026 carry some.
  - The pages of Duarte 2026 and Leonhard Center 2026 carry none.
- Totals for G1 to G12: 149 results screened, 10 pages or abstracts opened in full, 8 new sources (4 grey, 4 formal). Duarte 2026 was also opened, for scoring only. E1 to E6 screened 57 results and F1, F2 19; the E and F strings added 8 formal sources.
- Excluded without opening, by type: coach and template-vendor blogs (tier 3, repeating TED or Duarte); event listings and logistics pages; satire and course notes without authority; the same page found twice.
- Seen, not retrieved: two IEEE conference guides (TLS certificate could not be verified; no workaround attempted); a Tufte page on projection backgrounds (HTTP 403); a science-communication colour PDF (no connection).

## 6. Stopping rule (stated before the search)

- **Effort bounded:** the top 10 results of each string (N = 10).
- **Saturation:** stop after 3 consecutive strings that add no new concept (k = 3).
- Applied: G10, G11 and G12 added no new concept (concepts: numeric size or text limits, sentence headlines, no slides, pacing, accessibility, handouts, Q&A, timing), so the search stopped after G12.
- Q7 and Q8 round (G13 to G31): the rule was applied per question. Colour: G29, G30 and G31 added no new concept, so colour searching stopped after G31. Motion: G24, G25 and G26 added none, so it stopped after G26. Concepts found, in order:
  - Colour, first part: lightness not hue (G13), room-light rule (G14), harmony wheels (G15), perceptually uniform maps (G16).
  - Colour, second part: the Okabe-Ito palette (G17), palette limits and 3:1 for graphics (G18), meaning lists (G27), number of colours and direct labels (G28).
  - Motion: Morph for meaning (G19), staged and recorded demos (G20), lecture-video design (G21), animation-led explanation (G22), live-coding mechanics (G23).
- New concepts by string, first round:
  - G2: limits on title and line length.
  - G3: speak slide text aloud, describe visuals.
  - G4: note-taking handouts.
  - G8: outcome studies of fixed pacing.
  - G9: share slides a week ahead, avoid animation.

## 7. Selection

- Include: a source that states a rule or gives evidence on Q1 to Q6, in English, a talk or lecture with slides as its unit.
- Exclude: sources about posters or online meetings; pages that repeat another page; sources unreadable here. Video production is excluded as a craft (cameras, lighting) but included as design research (Guo 2014, Brame 2016).
- For Q7 and Q8 also: colour-only studies of web pages, packaging or marketing (no listener, no slide); animation of pedagogical agents (covered under Q3 in the first round); sources that are vendor templates.
- A grey source is scored (section 8); one under 10 is kept only as an example of practice.

## 8. Quality of grey sources (Guideline 11, Table 7)

- 20 criteria, each 1, 0.5 or 0: authority of the producer (4), methodology (6), objectivity (4), date (1), position among related sources (1), novelty (2), impact (1), outlet type (1).
- Impact is read here as 1 when a count or derived guides were seen, 0.5 for evident wide use or an owner's claim, 0 otherwise.
- Outlet is 1 for books, standards and reports, 0.5 for owner guides and annual reports, 0 for blogs.
- Books known from a catalogue page only are scored on what that page shows; sources.md says so.
- Threshold 10 of 20 (Garousi): 19 of 39 grey sources are under it (12 of 24 before the Q7 and Q8 round, 7 of 15 in it).

## 9. Extraction and synthesis

- Per source: producer, date, claim, number, evidence cited, limits.
- Synthesis is narrative by question; each claim traces to a row of sources.md.

## 10. Limits

- A second rater re-scored 5 of this topic's grey sources blind ([method](../README.md#method)), before Q7 and Q8 were added: 4 of 5 decisions agree. The TEDx organiser guide scores 9.5 and 12.5, as the raters weighed an owner's account of its own format differently; it stays an example of practice. The sources added for Q7 and Q8 were scored by one rater only.
- One search engine that personalises and changes; results of 2026-10-28 may not repeat.
- Screening used titles and engine summaries; secondary numbers are marked "(secondary)".
- Formal side: ten of the frame terms counted in the first round, the pool not screened from them. In the Q7 and Q8 round the counts come from ERIC and arXiv, not from OpenAlex, so they are not comparable with the first table.
- Many Q7 and Q8 papers sit behind publisher paywalls; where only the abstract was read, sources.md says so, and numbers carried only by a search summary are marked "(secondary)".
- Whether Richter 2016 and Schneider 2018 test colour as a moderator could not be settled: their full texts were not reachable, and only the abstracts and an archive description were read.

## Q9 business presentations (added 2026-10-29)

Rows to append to protocol.md. Numbering continues the strands E (E14 on), F (F3 on) and G (G32 on).

### Table 4 for Q9 (Garousi seven questions)

| # | Question | Answer for business presentations |
|---|---|---|
| 1 | Complex subject, not solvable by the formal literature alone | yes: slide conventions of firms, accelerators and sales methods are practice |
| 2 | Lack of volume, quality or consensus of evidence | yes: investor decisions have a literature; slide form, memo against deck and executive briefings have almost none |
| 3 | Context matters | yes: investor, buyer, executive and board decide on different things |
| 4 | Goal to check research against practical experience | yes |
| 5 | Goal to challenge practice rules with research | yes: passion, "answer first", "no slides" |
| 6 | Synthesis useful to both communities | yes |
| 7 | Many practitioner sources | yes: consulting guides, accelerator guides, deck-hosting data, sales training firms |

Seven of seven are yes, so grey literature is included.

### Q9 questions

- Q9a Structure: answer first (pyramid principle, BLUF, action titles, the SCQ frame) against the academic build-up. What is measured, what is only practice?
- Q9b Decision audiences: what investors, buyers and executives decide on; perceived passion and preparedness; the presenter against the content.
- Q9c Formats: slide deck against written memo; the deck read without a speaker; how pitch decks are read.
- Q9d Persuasion and attention: what the evidence on persuasion, storytelling and data storytelling supports in a business setting.
- Q9e Practice: consulting conventions, sales methods, accelerator guides, design-firm guides.
- Q9f Against: critiques of slides in organisations, and where business practice contradicts Q1 to Q8.

### Engine and date

- E, F and G strings: a general web search tool (one engine, US-based, returns a summary and links), run on 2026-10-29. A "screened" count is the number of result blocks returned; each block was read as a title plus the engine's summary.
- Metadata and DOI checks: the public Crossref REST API (`api.crossref.org/works`), called with no identity and no `mailto`. Its answers confirm title, authors, journal, year and pages; they carry no abstract in most cases.
- Pages opened one at a time. Eight opens failed (listed in section "Seen, not retrieved" of sources-q9.md). No sign-in, no CAPTCHA, no bypass was tried.

### Seed checks (not counted in the screening bound)

Each seed was looked up, then its page or abstract opened where open.

| Seed | Exists | Says what was cited | Read how |
|---|---|---|---|
| Clark 2008 | yes, Venture Capital 10(3), 257-279 | yes: 24 UK angels rated 3 pitches on 32 aspects; delivery factors weighed most; angels unaware | abstract (IDEAS page) |
| Chen 2009 | yes, AMJ 52(1), 199-214 | yes, with a twist: preparedness, not passion, went with funding | abstract (indexed copy) |
| Pollack 2012 | yes, ETP 36(5), 915-939 | yes: televised pitches, preparedness to legitimacy to funding | abstract (Crossref record text) |
| Brooks 2014 | yes, PNAS 111(12), 4427-4431 | yes, and it adds attractiveness: helped men, not women | abstract and full text (author copy, MIT DSpace) |
| Huang 2015 | yes, ASQ 60(4), 634-670 | partly: it is about investors' gut feel, not about presentations | abstract (Crossref record text) |
| Kosslyn 2012 | yes, already held | yes: 140 slideshows, 137 rules; research slides no better than business slides overall | abstract and results summary (open access page, first 100,000 characters) |

Seed searches returned 59 result blocks (Chen two strings of 10, Clark 10, Brooks 10, Pollack 9, Huang 10).

### E: existing reviews (Guideline 2)

| Id | String, as run | Engine | Screened | Included |
|---|---|---|---|---|
| E14 | `systematic review entrepreneurial pitch investor decision making pitch presentation literature review` | web search | 9 | 2 (Kalvapalle 2024, Ferrati 2021) |
| E15 | `meta-analysis narrative persuasion versus statistical evidence storytelling effect size` | web search | 10 | 1 (Zebregs 2015); Shen, Braddock and Allen meta-analyses seen, not opened |
| E16 | `Kernbach Eppler Bresciani PowerPoint constraining qualities literature review organizations decision making` | web search | 10 | 0 (wrong query: unrelated pages) |
| E17 | `Kernbach Bresciani Eppler "Slip-sliding-away" review literature constraining qualities PowerPoint Business and Professional Communication Quarterly` | web search | 10 | 1 (Kernbach 2015) |
| E18 | `data storytelling narrative visualization review Segel Heer genres; Kosara Mackinlay storytelling next step visualization evidence` | web search | 20 | 2 (Segel 2010, Kosara 2013) |

E16 returned nothing useful; E17 is the same query done correctly (zero results meant the query was wrong).

### F: formal

| Id | String, as run | Engine | Screened | Included |
|---|---|---|---|---|
| F3 | `Clingingsmith Shane training aspiring entrepreneurs to pitch experienced investors field experiment results` | web search | 9 | 1 (Clingingsmith 2018) |
| F4 | `Bernstein Korteweg Laws attracting early-stage investors randomized field experiment team traction` | web search | 10 | 1 (Bernstein 2017) |
| F5 | `Kanze Huang Conley Higgins "We ask men to win and women not to lose" venture capitalists questions Academy of Management Journal` | web search | 9 | 1 (Kanze 2018) |
| F6 | `experiment conclusion first versus conclusion last message order comprehension recall business writing inverted pyramid bottom line up front study` | web search | 18 | 1 (Britt 2003, through a summary) |
| F7 | `Yates Orlikowski PowerPoint presentation and its corollaries: how genres shape communicative action in organizations` | web search | 20 | 1 (Yates 2007) |
| F8 | `experiment written narrative memo versus bullet slides executives decision quality comprehension study business PowerPoint` | web search | 19 | 0 (opinion pieces only; no experiment found) |

Also found, and not included, since only a title or a summary was read:

- Allen and Preiss: a meta-analysis of narrative against statistics (1997);
- Shen and colleagues: a meta-analysis of narrative in health messages (2015; 25 studies, N = 9,330);
- Braddock and Dillard: a meta-analysis of narrative persuasion (2016);
- Elsbach and Kramer: a study of Hollywood pitch meetings (2003);
- Mitteness and colleagues: a study of angels and perceived passion (2012).

 Cardon 2017 (full text, read 2026-10-29) and Yang 2021 (abstract reading) are included for the passion debate.

Forward and backward snowballing: not run (no citation index without an identity). Cardon 2017 and Yang 2021 came from the summary of the Chen 2009 string.

### G: grey

Types and producers (Guideline 6):

| Type | Producers | Why |
|---|---|---|
| Deck-hosting data | DocSend (Dropbox) | the only large count of how decks are read |
| Investor guides | Sequoia, Y Combinator | what founders are told to show |
| Consulting practice | StrategyU, Minto International | action titles, storyline, pyramid |
| Company practice | Amazon letter, Tufte's page on it | memo instead of slides |
| Sales methods | Huthwaite (SPIN), Challenger | what sellers present and ask |
| Military writing standard | US Army correspondence regulation | origin of BLUF |

| Id | String, as run | Engine | Screened | Opened | Included |
|---|---|---|---|---|---|
| G32 | `DocSend pitch deck interest study how long investors spend reading pitch deck seconds` | web search | 9 | 3 | 2 (DocSend 2022, DocSend 2026) |
| G33 | `Army Regulation 25-50 bottom line up front BLUF correspondence writing standard` | web search | 10 | 2 | 0 (the regulation itself was not reachable) |
| G34 | `consulting slide conventions action title ghost deck storyline McKinsey Bain BCG how consultants write slides` | web search | 10 | 1 | 1 (Millerd 2025); no firm's own document found |
| G35 | `Bryar Carr Working Backwards Amazon narrative six-page memo silent reading meeting PowerPoint banned` | web search | 9 | 2 | 1 (Tufte 2022); Bezos 2018 re-found |
| G36 | `Sequoia Capital pitch deck template Y Combinator how to build your seed round pitch deck guide` | web search | 9 | 2 | 1 (Sequoia 2019); the Y Combinator page returned a title only |
| G37 | `Rackham SPIN Selling research 35,000 sales calls Huthwaite; Challenger Sale Gartner research buyers` | web search | 18 | 1 | 1 (Huthwaite 2026); Challenger figures stayed secondary |

Added directly, not through a string: Minto 2026 (the author's site, opened to check the pyramid and SCQ claims).

Totals: E 59, F 85, G 65 = 209 result blocks screened, plus 59 for the seeds.

### Stopping rule (stated before the search, applied after)

- Effort bound: about 80 results screened in all.
- Saturation: stop a family after two consecutive strings add no new included source.
- Applied:
  - E: E16 added none, E17 added one. Not saturated.
  - F: F8 added none, F7 added one. Not saturated.
  - G: G33 added none, G34 added one. Not saturated.
- The effort bound was exceeded (209 against 80), because each string returns about ten result blocks and 21 strings were needed to touch six sub-questions. No family stopped on saturation. Each stopped when every sub-question Q9a to Q9f had at least one source or a recorded "none found".
- Consequence: Q9 is a first pass. A second pass on consulting firms' own documents and on accelerator guides would likely add sources.

### Selection

- Include: a source that states a rule or gives evidence on Q9a to Q9f, in English, about a pitch, a sales or executive presentation, a deck or a memo as its unit.
- Exclude: entrepreneurship studies of crowdfunding pages or business plans read without a presentation; template vendors and AI slide-tool blogs repeating one another; pages with no producer.
- Quality: grey sources scored on the 20 criteria of section 8 of protocol.md; a source under 10 serves as an example of practice only.

### Limits

- One reviewer, no second rater for these scores.
- One personalising search engine; results of 2026-10-29 may not repeat.
- Screening used titles and the engine's summaries. Numbers read only in a summary are marked "(secondary)".
- Three of the formal sources (Chen 2009, Pollack 2012, Huang 2015) are paywalled; only abstracts were read. Brooks 2014's PNAS page sits behind a bot check that was not bypassed; the author copy in MIT DSpace was read in full.
- Most investor studies are of US or UK angels, venture capitalists and televised pitches. Executive and board briefings have no study in this pool.
