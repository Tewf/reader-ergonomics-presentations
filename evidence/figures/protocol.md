# Protocol

This file records every search behind the figures topic so that anyone can run it again: each string, with its date and count.

String numbers continue those of the presentations topic, from E27, F15 and G44. So one label names one string across both protocols.

The terms and the six questions are in the [frame](frame.md).

## Table 4 for Q11 (Garousi seven questions)

| # | Question | Answer for figures and diagrams |
|---|---|---|
| 1 | Complex subject, not solvable by the formal literature alone | yes: style guides, tool documentation and accessibility standards decide daily practice |
| 2 | Lack of volume, quality or consensus of evidence | yes: layout studies use 16 to 44 participants, chart studies use 20 to 87 students or crowdsourced chart tasks; none tests text art |
| 3 | Context matters | yes: a README, a report and a slide differ in medium, reader and tooling |
| 4 | Goal to check research against practical experience | yes |
| 5 | Goal to challenge practice rules with research | yes: "remove all decoration", "legend at the top", "use less ink" |
| 6 | Synthesis useful to both communities | yes |
| 7 | Many practitioner sources | yes: newsroom and institute guides, vendor documentation, standards |

Seven of seven are yes, so [grey literature](../README.md#method) is included.


## Engine and date

- E, F and G strings: the engine of the presentations [protocol](../presentations/protocol.md), run on 2026-10-29.
- A **result block** is one link with its title. A "screened" count is the number of blocks returned; some calls returned two or three lists, and all are counted.
- Screening used the title and the engine's summary. A page was **opened** when fetched with an extraction tool; a number is then primary. A number read only in a summary is "(secondary)".
- Where the extraction tool could not read a PDF, the file was converted to text locally and read. Heer 2010, Bateman 2010, Burch 2021, Harrison 2015, Song 2025, Zou 2024 and Few 2011 were read that way.
- DOIs were checked with the public Crossref REST API, called with no identity and no `mailto`, one request at a time.
- No sign-in, no CAPTCHA, no identity. Two publisher pages were not followed: a Springer authorisation redirect (Huestegge 2011) and a certificate error (Hill 2018, jisar.org).
- OpenAlex counts were not attempted: the daily budget was reported spent for Q10.

## E: existing reviews (Guideline 2)

| Id | String, as run | Screened | Included |
|---|---|---|---|
| E27 | `systematic review graph drawing aesthetics empirical studies edge crossings readability` | 9 | 1 (Purchase 1997 via summaries); a 2024 review of layout evaluation named in a summary, not identified |
| E28 | `survey of user studies node-link diagram layout human comprehension Purchase Ware Huang` | 9 | 2 (Burch 2021, full text; Pohl 2009, secondary) |
| E29 | `systematic review aesthetics usability effect perceived beauty performance meta-analysis` | 10 | 2 (Thielsch 2019; Schlamann 2026) |
| E30 | `visualization aesthetics survey review literature visual appeal data visualization effects on engagement memorability` | 9 | 1 (Harrison 2015); BeauVis seen, not used (scale, not a review) |

## F: formal

| Id | String, as run | Screened | Included |
|---|---|---|---|
| F15 | `Cleveland McGill graphical perception replication Heer Bostock crowdsourcing ranking visual channels` | 10 | 3 (Cleveland 1984, Heer 2010, Talbot 2014) |
| F16 | `Gestalt principles proximity common region connectedness experiment grouping perception Palmer Rock` | 10 | 2 (Palmer 1992, Palmer 1994, both secondary) |
| F17 | `Bateman 2010 useful junk? effects of visual embellishment on comprehension and memorability of charts` | 9 | 1 (Bateman 2010, full text) |
| F18 | `Borkin Bylinskii 2016 beyond memorability visualization recognition and recall` | 10 | 1 (Borkin 2016) |
| F19 | `large language models understand diagrams as code versus image Mermaid Graphviz benchmark text-based graph vs rendered image` | 19 | 3 (Zou 2024, Das 2024, Zhong 2024 found later) |
| F20 | `data-ink ratio Tufte critique empirical study chartjunk Inbar Tractinsky minimalism` | 10 | 2 (Inbar 2007, abstract; Hill 2018, secondary) |
| F21 | `Huang Eades Hong effects of edge crossings eye tracking graph drawing comprehension; Huang 2008 crossing angle` | 19 | 3 (Huang 2008, Huang 2008b, Huang 2014) |
| F22 | `flowchart direction top-to-bottom versus left-to-right comprehension experiment directed graph layout flow direction readability` | 9 | 2 (Figl 2014, Figl 2015) |
| F23 | `Skau Harrison Kosara evaluation of the impact of visual embellishments in bar charts EuroVis 2015` | 10 | 1 (Skau 2015) |
| F24 | `Borgo empirical study on using visual embellishments in visualization TVCG 2012 Hullman visual difficulties` | 19 | 2 (Borgo 2012, Hullman 2011) |
| F25 | `visual appeal trust credibility data visualization experiment aesthetics trust in charts Elhamdadi` | 10 | 2 (Elhamdadi 2023, Song 2025) |
| F26 | `Purchase 1997 "Which aesthetic has the greatest effect on human understanding" edge crossings bends symmetry abstract` | 10 | 0 new (Purchase 1997 already included) |
| F27 | `Borkin 2013 "What makes a visualization memorable" 2,070 single-panel visualizations Mechanical Turk results` | 10 | 1 (Borkin 2013) |
| F28 | `Tractinsky 2000 "what is beautiful is usable" aesthetics perceived usability ATM Lindgaard 50 milliseconds first impression` | 19 | 2 (Tractinsky 2000, Lindgaard 2006) |
| F29 | `direct labeling versus legend chart comprehension experiment spatial contiguity labels near elements diagram` | 9 | 1 (Huestegge 2011) |
| F30 | `diagram readability guidelines software architecture diagrams visual hierarchy grouping proximity common region experiment comprehension` | 19 | 0 (UML class diagram studies of proximity and hierarchy named in summaries; not retrievable, see sources) |
| F31 | `LLM read ASCII diagram text art versus image flowchart question answering vision language model FlowVQA diagram understanding` | 19 | 2 (Singh 2024, Ye 2025); no study of ASCII found |

## G: grey

| Id | String, as run | Screened | Included |
|---|---|---|---|
| G44 | `ASCII art box drawing characters screen reader accessibility text diagram alt text` | 10 | 2 (Accessible Social 2026, CUNY 2026) |
| G45 | `WCAG 2.2 1.4.11 non-text contrast understanding graphical objects diagrams` | 9 | 1 (W3C 2023g) |
| G46 | `Ten simple rules for better figures Rougier Droettboom Bourne` | 10 | 1 (Rougier 2014) |
| G47 | `Urban Institute data visualization style guide OR Financial Times Visual Vocabulary OR Economist style guide charts` | 27 | 2 (Urban 2025, FT 2026) |
| G48 | `Mermaid accTitle accDescr accessibility diagram GitHub renders alt text` | 19 | 1 (Mermaid 2026c); the first list of 10 was unrelated |
| G49 | `Quarto figures diagrams Mermaid Graphviz fig-alt alt text accessibility` | 18 | 1 (Quarto 2026) |
| G50 | `BBC Visual and Data Journalism cookbook OR Guardian OR New York Times graphics style guide chart design principles` | 27 | 0 (BBC page opened, truncated; NYT and Guardian only in summaries) |
| G51 | `Stephen Few critique "Useful Junk" Bateman validity embellishment charts response` | 18 | 2 (Few 2011, Kosara 2010) |
| G52 | `Nature Methods Points of View Bang Wong salience OR layout OR "design of data figures" visualization column` | 19 | 0 (columns seen in summaries only) |
| G53 | `Economist "Mistakes, we've drawn a few" chart mistakes graphic detail OR Datawrapper chart design principles annotate title direct labels` | 19 | 1 (Datawrapper 2022) |

Opened by their known address, outside any string: W3C 2023e, W3C 2023a (the WCAG 2.2 text), W3C 2026a, GitHub 2026e. Europa 2023 and Zhong 2024 were named in the F17 and F19 result lists, and Singh 2024 and Ye 2025 in F31.

## Stopping rule, applied

- Stated before searching: saturation (two strings in a row add nothing) or about 120 result blocks.
- The 120-block bound was passed at F21 (124 blocks counted from the E and F rows above). I kept going because Q11d to Q11f still had gaps the brief requires answered.
- Total: 31 strings and 434 result blocks screened (counted from the rows above). Pages opened: (not verified: no list of opened pages was kept).
- Saturation was met for Q11a (F26 added no new source after F21) and for Q11c (F27 and F28 only completed known lines).
- Saturation was not met for Q11e: G53 still added a new producer. Q11e is a first pass; newsroom guides (BBC, NYT, Guardian, Economist) are not opened.

## Existing reviews placed

- No review of figure and diagram drawing for readers, joining formal and grey sources, was found.
- Held as strand 0: the system-diagrams review (Moody 2009a, Purchase 2002, Störrle layout studies, diagrams as code).
- New strand-0 reviews: Burch 2021 (graph visualisation user studies), Thielsch 2019 and Schlamann 2026 (aesthetics and performance).

## Selection

- Include: a controlled study, a meta-analysis or a survey on figure layout, perception, appeal or accessibility; a standard; a style guide or documentation page from a named producer.
- Exclude: tutorials without a producer; AI image-tool blogs; template marketplaces; pages that only repeat Tufte without a source.
- Quality: grey sources scored on the 20 criteria of section 8 of the presentations [protocol](../presentations/protocol.md); below 10 of 20 serves as an example of practice only.

## Limits

- One reviewer, no second rater.
- One personalising search engine; results of 2026-10-29 may not repeat.
- Three of the 35 formal sources are secondary (Huang 2014, Palmer 1994, Hill 2018); most of the others were read as abstracts only; sources.md marks each.
- The studies of layout use students and small samples; the studies of charts use crowdsourced workers.
- No study found tests a figure for a reader of documentation, which is the case this strand serves.
