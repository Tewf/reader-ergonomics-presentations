# Review

This file reviews the literature on drawing figures and diagrams for a reader in strands: existing reviews first, then layout, encoding, appeal, typed diagrams against drawn ones, practice, and the evidence against.

Each row carries the grade of what its source shows, and "(secondary)" where a number was read only in a summary or a citing paper. The searches are in [protocol](protocol.md), and each source's score is in [sources](sources.md).

A **figure** is any drawn picture in a document. A **node-link diagram** is a figure of boxes joined by lines. **Text art** is a diagram typed from characters.

What the evidence covers, by outcome:

| Outcome | Studied | Not studied (none found) |
|---|---|---|
| Speed and accuracy of reading | node-link layouts, bar charts, bar embellishments | text art, diagrams in documentation |
| Memory | chart embellishment, memorability of charts | diagrams drawn from source |
| Trust and appeal | infographics, bar charts, interfaces | node-link diagrams |
| Access | rules in standards | tests with screen-reader users on box-drawing diagrams |
| Reading by a language model | graphs from random generators, Graphviz, flowcharts | text art |

## 0. Existing reviews

- No review joins formal and grey sources on how to draw figures and diagrams for a reader.
- Burch 2021 surveys 239 papers (1995 to 2020) of user studies of graph visualisation and sorts them into interpretation, memorability and creation. It names gaps. One author tagged each paper.
- Thielsch 2019 and Schlamann 2026 are meta-analyses of aesthetics and performance, for interfaces.
- The system-diagrams review holds the diagram theory and the layout studies (strand 0 there). They are linked, not reviewed again.

## 1. Layout (Q11a)

| Source | Claim | Grade |
|---|---|---|
| Purchase 1997 (abstract) | Of five aesthetics, fewer edge crossings had the largest effect on understanding (time and error counts, experiments run online); fewer bends and more symmetry had a smaller one; maximising the smallest angle between edges and fixing edges and nodes on an orthogonal grid were not significant. The minimum angle tested is the angle between edges at a node, not a crossing angle | measured (not verified: kind of graph and participants, abstract only) |
| Ware 2002, Störrle 2016b (held) | After path length, continuity and edge crossings cost most in path finding (Ware 2002, secondary); layout flaws correlate with score at r = -0.419 in UML diagrams (Störrle 2016b, checked in the system-diagrams audit) | measured (held) |
| Huang 2008 | 16 subjects, six drawings: small crossing angles slowed path search and added eye movements; crossings barely affected node locating | supported with caveat |
| Huang 2008b (abstract), Huang 2014 (secondary, via Burch 2021) | Path-tracing response time fell as the crossing angle grew and levelled off near 90 degrees (Huang 2008b, 22 participants per Burch 2021); a follow-up on general graphs with 37 participants agreed (Huang 2014, per Burch 2021) | supported with caveat |
| Burch 2021, on Huang and colleagues | With 26 participants, layouts with crossings were fastest for interpretation tasks; accuracy and effort did not differ; preference went to no crossings | supported with caveat |
| Figl 2015 (abstract) | Controlled pilot, 44 participants, four flow directions of process models: theory favours left to right, the preliminary results were less clear-cut, and readers adapted well to unusual directions | supported with caveat (pilot): no direction shown to read best |
| Figl 2014 (abstract) | Process models are drawn left to right or top to bottom by convention; standards and guidelines barely discuss it, and most recommendations on flow direction rest on neither scientific claims nor evidence | convention, untested (position paper) |

- Found, results not extracted: Pohl 2009 (36 subjects; force-directed, hierarchical and orthogonal layouts, eye tracking; abstract and introduction read).
- Not found: a controlled study of alignment, of proximity between linked nodes, or of grouping boxes in a node-link diagram.

## 2. Encoding and grouping (Q11b)

| Source | Claim | Grade |
|---|---|---|
| Cleveland 1984 (abstract) | Experiments test a set of elementary perceptual tasks ordered by accuracy, and the ordering is the guideline for graph construction. The abstract states no ranking; Heer 2010 is the source for the ranks below | measured, for charts |
| Heer 2010 | The replication (experiment 1A, 82 workers; 186 workers across all the paper's experiments) preserved the ranking of the five original judgment types; position still significantly beat length; angle and circular area were added: area did worse than angle, both worse than position, and angle was not worse than length | measured, for charts |
| Talbot 2014 (abstract) | Four experiments on bar chart configurations broadly confirm Cleveland and McGill's ranking of those configurations (aligned bars over stacked, adjacent bars over separated ones); not a ranking of position, length, angle and area | measured, for bar charts |
| Palmer 1992 (abstract), Palmer 1994 (not read) | Items inside one bounded region group together and this can override proximity and similarity (Palmer 1992; the record read describes demonstrations). Grouping by a joining line (uniform connectedness) is Palmer and Rock 1994; its abstract was not reached | measured (not verified: the record read for Palmer 1992 describes demonstrations; Palmer 1994 not read) |
| Huestegge 2011 (abstract) | Four experiments with bar and line graphs and eye tracking: spatial compatibility between the data region and the legend shortened the time to understand a graph and to retrieve its content from memory. What "compatible" meant (order of entries or distance) was not read, so the result is not shown for direct labels | supported with caveat |
| Borkin 2016 (abstract) | 393 visualisations, eye movements of 33 participants and their text descriptions: titles and supporting text should convey the message; pictograms, used appropriately, did not harm understanding; visualisations memorable at a glance also conveyed their message. That viewers spend most of their time on the title is from a news write-up (secondary) | supported with caveat |

- All the ranking evidence is for quantities in charts. No study ranks channels for nodes, links or regions in a diagram.
- Gestalt evidence is from the laboratory. Two studies of grouping in UML class diagrams were named in summaries and could not be retrieved.
- The Points of View columns on salience and layout (Wong) could not be opened.

## 3. Appeal (Q11c)

| Source | Claim | Grade |
|---|---|---|
| Thielsch 2019 | 25 studies, 101 effects, 3,025 participants: g = 0.12 for aesthetics on user performance; high heterogeneity; no moderator was significant | measured, for interfaces |
| Schlamann 2026 | 31 studies, 234 effects, 18,794 participants: g = 0.29; high unexplained heterogeneity; device and typography moderate it | measured, for interfaces |
| Bateman 2010 | 20 students; 14 Holmes charts, each with a plain version, and each participant saw one version of each chart (12 charts scored): description of subject, categories and trend did not differ; value messages were described better for the Holmes charts (t19 = 3.37, p = .003). Recall: with 10 participants per recall condition and one-tailed tests, immediate recall differed only for the value message, and recall after two to three weeks was better on all four measures; participants preferred the Holmes charts | measured, for the charts of one designer |
| Borgo 2012 (abstract) | Embellishments helped recall and slowed visual search; the effect on grasping concepts was mixed | measured |
| Skau 2015 (abstract; results from Kosara's summary, secondary) | Most bar embellishments lowered accuracy when comparing bars; quadratically scaled triangles were worst; absolute-value estimates were mostly unaffected | measured |
| Borkin 2013 (abstract) | Of 2,070 visualisations, colour and recognisable human objects raised memorability; common graph types were remembered less well than unusual ones | measured |
| Harrison 2015 | 1,278 participants rated infographics after 500 ms: first impressions were reliable; colourfulness predicted appeal more than visual complexity; age, gender and education moved the preferred level (the results text gives 34% of the variance to the model with them; the conclusion gives 34% to colourfulness and complexity, so the paper is inconsistent) | measured, for ratings of appeal |
| Lindgaard 2006, Tractinsky 2000 (abstracts) | Appeal ratings of web pages formed in 50 ms matched ratings at 500 ms; perceived beauty correlated with perceived usability in an ATM simulation, and the degree of actual usability did not move post-use perceptions | supported with caveat |
| Elhamdadi 2023 (abstract) | Trust in a visualisation has cognitive and affective parts; visual complexity was one tested antecedent | supported with caveat |
| Song 2025 | Participants were 15.37 times more likely to choose plain over cartoon-style bars for credibility (CI 5.93 to 39.83); plain against image-style showed no significant difference; in the second experiment hand-drawn type lowered and colour raised credibility | supported with caveat, preprint |
| Cheng 2026 (held) | Interesting but irrelevant material lowers learning, g = -0.16 over 50 studies | measured (held) |
| Hullman 2011 (abstract) | Difficulty that forces processing may help learning; argued from earlier studies | convention, untested |

- Song 2025 contradicts itself on image-style bars: the abstract says they raised credibility, a figure caption says they lowered it. The numbers above are from the results text.
- Nothing found tests appeal for a node-link diagram.

## 4. Text art against drawn diagrams (Q11d)

| Source | Claim | Grade |
|---|---|---|
| W3C 2023f | WCAG 2.2 counts ASCII art as non-text content; its glossary defines ASCII art as a picture made by arranging characters, typically the 95 printable ASCII ones, so box-drawing characters fall under it only by extension | convention (a standard) |
| W3C 2023e | A chart or diagram needs a short text alternative and a long one; the long one states type, summary, trends, and the data in a table where practical; a filename as alternative is a failure | convention (a standard) |
| W3C 2026a | Complex images, flow charts among them, need a two-part alternative: a short description and a long description; the page shows three approaches to attach the long one (a link, a pointer in the alt text, a figure with a caption) and an aria-describedby example; the page has no flow chart example | convention (a standard) |
| W3C 2023g | Parts of a graphic needed to understand it need 3:1 contrast against adjacent colours; text carrying the same information, decoration and essential presentation are exempt | convention (a standard) |
| CUNY 2026 | ASCII art (the page is about memes and social posts) is not accessible to screen-reader users; turn it into an image with alt text | convention, untested |
| Accessible Social 2026 (example only) | Assistive technology reads characters at face value and cannot tell a picture from text | convention, untested |
| Mermaid 2026c | `accTitle` (one line) and `accDescr` (one or several lines) add SVG `title` and `desc` and the ARIA attributes, for every diagram type | convention (documented output, not tested with users) |
| GitHub 2026d | Mermaid, GeoJSON, TopoJSON and ASCII STL render from fenced blocks in issues, discussions, pull requests, wikis and Markdown files; the page gives authors no alt-text guidance | convention |
| Quarto 2026 | Mermaid and Graphviz cells render natively for HTML and to PNG for print; the page lists label, caption and size options and no alt-text option | convention |
| Zou 2024 | GPT-4 averaged 78% on TikZ and the text reports about 83% on TikZ and Graphviz, at least 17% above SVG; a different model, LLaVA-1.5-13b, reached 50.1% on rasterised Graphviz images (and 84.1% on rasterised SVG). The models differ, so it says nothing about text against image for one model | supported with caveat, different models |
| Zhong 2024 | GPT-4o on 500 random graphs of 5 to 20 nodes, zero-shot, text (adjacency) against image alone: edge existence 96.2 against 74.6, node degree 75.8 against 55.8, shortest path 69.0 against 53.0, cycle check 96.2 against 97.0; the image together with the text scored close to the text alone on edge existence (96.4) and the authors report that visualisations can help, unevenly | supported with caveat, one drawing style |
| Das 2024 | With vision-language models, the image form beats the text form when token limits bind | supported with caveat |
| Ye 2025 | Turning a flowchart image into text first (Graphviz, Mermaid or PlantUML) and reasoning on that beats end-to-end models on two benchmarks | supported with caveat |
| Singh 2024 (abstract) | FlowVQA holds 2,272 flowchart images and 22,413 question-answer pairs; the flowcharts are generated as Mermaid.js diagrams | measured, descriptive |

- Not found: any test with screen-reader users on box-drawing diagrams, and any comparison of text art against a rendered image or diagram source for the same model.

## 5. Practice (Q11e)

| Source | Claim | Grade |
|---|---|---|
| Rougier 2014 | Ten rules: know the audience, fix the message, fit the medium, write a caption, tune defaults, use colour with purpose, stay faithful to the data, drop decoration, put clarity before appeal, pick the right tool; no experiment | convention, untested |
| Urban 2025 | Concise active titles; specifics in a subtitle; a source line on every figure; directly label the data and omit the legend when possible (otherwise a legend across the top); fewer than seven categories; annotate; WCAG 2.0 AA contrast for text and alt text on web charts; no study cited | convention, untested |
| FT 2026 | Chart types grouped in nine families by what they show; the related reading links Cleveland and McGill once; the page calls itself a work in progress | convention, untested |
| Europa 2023 | Minimalism and embellishment form a continuum chosen by medium and audience; remove only the junk that hides the data | convention, untested |
| Datawrapper 2022 (example only) | State the data in the title or description and omit most axis labels; supported by examples from newsrooms, not studies | convention, untested |
| Few 2011, Europa 2023, Inbar 2007 (secondary for the rule) | Tufte's data-ink rule asks that ink show data; the book was not read | convention, untested |

- Not found: a written newsroom graphics guide for the New York Times (one summary says there is none), the Guardian or the BBC. The BBC page opened truncated.
- Adoption counts for these guides were not found.

## 6. Against (Q11f)

| Source | Claim | Grade |
|---|---|---|
| Bateman 2010, Few 2011, Kosara 2010 | Embellished charts were described as accurately and remembered better after two to three weeks; Few restates the result for one-sentence messages with relevant embellishment and criticises the study (20 students, charts by one designer); Kosara notes that values were not read and that the charts were extreme examples, and that minimal charts still suit analysis | supported with caveat |
| Skau 2015, Borgo 2012 (abstracts) | Other embellishments lowered accuracy or slowed search | measured |
| Inbar 2007 (abstract), Hill 2018 (secondary: a search summary of the abstract) | 87 students preferred a standard bar graph to a minimalist one (Inbar); respondents rated charts with lower data-ink ratios better on beauty, clarity, effectiveness and simplicity (Hill); preference, not performance | supported with caveat |
| Burch 2021 on Huang | A study found layouts with crossings fastest to interpret | supported with caveat |
| Thielsch 2019, Schlamann 2026 | The estimated gain from beauty is g = 0.12 in the first (25 studies) and g = 0.29 in the second (31 studies, which kept only studies whose aesthetic manipulation was confirmed by ratings); both are heterogeneous | measured, for interfaces |

Details are in against.md.
