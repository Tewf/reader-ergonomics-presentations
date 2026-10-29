# Position

This file says what is known, what is not, and what this repository adds about presentations.

## Known

- Showing slides is neutral on average; design is where the effect lives (Baker 2018).
- Slides violate known principles in every field, academic talks included (Kosslyn 2012).
- On-screen text that repeats the voice word for word does not help over text alone, and key terms do better (Adesope 2012).
- A bundled design, sentence headline plus visual evidence plus less text, outperformed the default in one controlled study (Garner 2013).
- Gesture helps; a visible face has no consistent benefit (Dargue 2019, Henderson 2021).
- Conference talks are a genre with their own structure, not a spoken paper (Rowley-Jolivet 2005).
- Across 29 reviews, good multimedia design mattered more in system-paced settings such as lectures (Noetel 2022).
- Experts agree on talk advice, but experiments are scarce (Blome 2017).

- Key points shown in step with the voice help over the whole slide at once, in small recorded studies (Liu 2022, Ito 2026).
- Live coding taught no more than static code in one controlled study (Shah 2023); active live coding taught no more than traditional live coding but held engagement higher (Shah 2025).
- Video adds learning when it is added, less when it replaces teaching (Noetel 2021).
- Pleasant colours and faces together give a small gain (Brom 2018); colour coding that links text and picture helps (Ozcelik 2009).
- Rainbow-like maps distort data and defeat colour-vision deficiency (Crameri 2020).
- Dark text on a light ground was the most legible, projected too (Greco 2008).
- Harmony is a matter of preference (Schloss 2011).

## Not known

- Which element of the bundle does the work: the headline, the graphic, or the lower word count.
- Whether the effect holds for expert audiences, for hour-long talks, and for live speakers in a room.
- A minimum projected size that protects comprehension.
- What a Q&A should do for the listener's memory; the research is descriptive.
- Whether practice formats help understanding or only discipline the speaker: 20 by 20 has three small studies, mixed (Liao 2020, Warmuth 2021, Bakcek 2020); Lessig and memos have none found.
- Whether speaking every slide word aloud, as accessibility guides ask (Rector 2019), costs sighted listeners what Adesope 2012 predicts.

- Whether builds, transitions and Morph help a live audience; the three build studies used recorded narration.
- Whether an animated explainer teaches more than a good slide video; engagement differs, comprehension mostly does not.
- Whether a live demo teaches more than a recorded one; no study found.
- Whether a dark ground beats a light one at room distance in a dark room; advice says yes, the one projection experiment says no.
- Whether colour alone, apart from faces and shape, helps learning.
- Whether hue meaning (red as alarm) or wheel harmony changes what a listener keeps.

## Where practice runs ahead of the evidence

- Numeric rules: 30 point (Kawasaki), 17 point (Peyton Jones), 18 point (Microsoft), 6 or 7 items, 20 to 40 words (Beamer 2026). Each is a convention.
- Fixed pacing: PechaKucha and Ignite. Their own pages (examples only, 6 and 5.5 of 20) claim success; the one randomised trial found equal test scores (Bakcek 2020).
- Replacing slides with a memo (Bezos 2018). It removes the paced-medium problem by changing the medium, which the strand-1 results would predict to help; no outcome data.
- The glance test: three seconds, with no evidence on the page (Duarte 2026, 5 of 20, example only).
- Designer layouts at scale (Microsoft 2019): wide use without a comprehension study found.
- Live demos and live coding: recommended as best practice (Nederbragt 2016, LornaJane 2017) while the controlled studies found no learning gain over static code (Shah 2023). Active live coding did not beat traditional (Shah 2025).
- The 6-minute chunk for video comes from an observational study of watching time (Guo 2014), not from learning.
- Colour wheels and meaning lists (Ethos3 2026, 2.5 of 20, example only) teach complementary pairs as strong, while hue-pair preference research finds contrasting pairs less harmonious (Schloss 2011).

## Where evidence is ignored by practice

- Defaults: the template deck is a topic title over bullets, which Garner 2013 used as its weaker arm.
- Beamer 2026 advises phrases over sentences; Garner 2013 favoured sentence headlines. The two disagree on the headline, and agree on short slides.
- Peyton Jones 1993 says skip the outline slide and put a recap slide about a third of the way through; this is advice from experience, untested.
- Accessibility guides ask for slide text spoken aloud (Rector 2019); the redundancy result says verbatim text and voice do not help over text alone (Adesope 2012). The two have not been tested together.
- The accessibility checker tests structure (titles, order, contrast), not whether a listener understands.
- Dark ground in a dark room is the usual advice (Schwabish 2014, 5 of 20, example only); the one projection experiment found dark text on light best (Greco 2008). Practice also splits: TED 2026 says bold text on dark; Beamer 2026 warns against inverse video in bright rooms.
- Rainbow-like maps remain software defaults although the evidence is against them (Crameri 2020).
- Where they agree: colour never the only cue (W3C 2023c; Rector 2019; Microsoft 2026) matches the figure literature.

## Against the existing reviews

- Noetel 2022 and Cromley 2025 cover multimedia design in general; this review applies them to a talk and shows where they stop (no speaker, no room).
- Baker 2018 asks whether PowerPoint helps; this review asks which design helps and finds one bundled experiment.
- Blome 2017 gathers advice without testing it; this review sets the advice beside the experiments and the grey guides.
- Henderson 2021, Polat 2022 and Zhu 2024 cover the speaker on video; none covers a live room.
- No review found covers talk structure, legibility at distance, or practice formats.
- Brom 2018, Wong 2020, Mutlu-Bayraktar 2024 and Desiron 2026 cover emotional design in lessons; none covers a talk or a figure.
- Noetel 2021, Tharumalingam 2025 and Kuang 2023 cover video watched alone; none covers video inside a talk.
- Selvaraj 2021 reviews live coding; the controlled studies that followed found no learning gain.

## What this repository adds

- It ties talk advice to named evidence and says which results came from short lab lessons.
- It sets one named baseline (baseline.md) and a mechanical checklist whose items a program can test.
- It keeps the practice rules as tagged conventions, not findings.
- For motion and colour it separates what a speaker-paced room changes from what a self-paced page already settled, and names the studies still missing.
- It gives checklist items for builds, video, demos and colour with a grade each (baseline.md).

## The business context: candidate overrides (added 2026-10-29)

The base is "what a presentation is". The academic talk and the business presentation each override it, the way a reader style overrides the standard. This file lists what the business context changes, and what it leaves alone. Few rules change, and each says why.

### Overrides

| Base rule (academic talk) | Business override | Evidence | Grade |
|---|---|---|---|
| Build up: background, method, result; one thing to remember in the first minutes | Open with the answer and the ask: the recommendation, the decision wanted, then the support (pyramid, SCQ for the setup) | Britt 2003 (short arguments, full text); Minto 2026, Millerd 2025 (practice); Clark 2008 (angels judged clarity and structure) | convention for decks and talks; supported with caveat for short texts |
| The audience judges the claim by method and evidence | Content is chosen for the decider's criteria: the team, the preparedness behind the numbers, the market; show readiness to answer | Bernstein 2017 (team drove interest on average, full text); Chen 2009, Pollack 2012 (preparedness); DocSend 2022 (team slide in 100% of decks, successful or not: a prevalence count, not evidence that it decides) | measured for the screening stage; supported with caveat otherwise |
| The speaker's delivery is secondary to content | Treat the presenter as part of the pitch: angels weighed delivery without saying so (Clark 2008) and presenter gender and attractiveness moved choice (Brooks 2014); rehearse delivery as content | Clark 2008; Brooks 2014 | supported with caveat (angels); measured (Brooks 2014, US pitch competitions) |
| Plan the Q&A as questions about the work | Plan the Q&A as part of the decision; expect prevention-focused questions and prepare promotion-focused answers | Kanze 2018 | measured |
| Slides support a spoken talk; words on screen add to the voice, not repeat it | For a deck read without a speaker, the deck is a document: sentence headlines carry the claim for a reader who scans in about three minutes, and fuller text on a slide is allowed | Yates 2007 (secondary); Ginns 2005 and Adesope 2012 (held; system pacing only); DocSend 2022 (sample not stated) | inference, partly unread sources (Yates 2007 not verified; Ginns 2005 full text); untested on decks |
| A fixed slot (conference, defence) sets the length | The reader's or the room's time sets the length; design the first slides to stand alone | DocSend 2022 (just under three minutes; unsuccessful decks left at 2:13; sample not stated) | descriptive, owner's data, sample not stated |
| Slides are the default medium | A written narrative read at the start of the meeting is an accepted alternative for decision meetings | Bezos 2018 (held, 10.5); Tufte 2022 (5, example only) | convention, untested |
| Evidence is shown as the figure of the result | Pair the number with a short case where the aim is action; numbers for belief, story for intent | Zebregs 2015 (health setting); no business test | supported with caveat (health), untested in business |

- Weakest rows: the memo and the story-with-number rows. Each has no test in business.
- Strongest row: the team and preparedness content, with a randomised field experiment behind it (Bernstein 2017), though it concerns the first screen of an email.
- The order row is the one the practice sources agree on and no business study tests.

### Rules that do not change

| Base rule | Why it holds in business |
|---|---|
| Sentence headline stating the claim, a figure as the evidence | Garner 2013 (held). Consulting action titles already agree; nothing in Q9 contradicts it |
| One claim per slide; no decorative images | Held (Sundararajan 2020); Millerd 2025 says the same as practice |
| Contrast, colour not the only cue, legible type | Held (W3C 2023, Rector 2019); an investor's screen is still a screen |
| Say the evidence and where it is weak | A buyer or an investor also asks; preparedness is what persuaded in Chen 2009 and Pollack 2012 |
| Rehearse; test the room and the file | Preparedness is the best supported cue in Q9b |
| A handout is a document of its own, not the slides read as notes | Said to agree with Yates 2007 (not verified: only a bibliographic record was reached): the leave-behind is a genre, built for reading |
| Gesture and pointing | No business test; the held evidence (Hostetter 2011) is not specific to academic talks |
| Segment long material | Held (Rey 2019); no business test |

### Not overridden, because no evidence was found

- Executive and board briefings: no study; practice sources are an Army standard that could not be read and a company letter.
- Sales presentations: one owner account of a call study, no result on presenting.
- Colour, motion and font size for business: no difference found against the base.

## The casual context: candidate overrides (added 2026-10-29)

The base is "what a presentation is", and the casual talk is its third context, after the academic and the business ones.

This section lists what the casual context changes and what it leaves alone. Few rules change; each says why, and the weakest are marked.

What a casual talk is: see [the review, section 10](review.md).

### Overrides

| Base rule (academic talk) | Casual override | Evidence | Grade |
|---|---|---|---|
| The audience shares the field's terms; prior knowledge is assumed | Assume none: say who the talk is for, define every term before its first use, and prefer a plain word to a technical one | McCarthy 2025 (audience seldom defined, "general public" framing); Rakedzon 2017 (lay summaries still above the 2% limit; the tool was also validated on lecture transcripts); Kalyuga 2014 (held; a chapter on redundancy, not on expertise reversal) | supported with caveat; the jargon limit comes from reading research; no source tests assuming none |
| The audience stays; the talk starts with the problem and its background | The audience can leave and chose to come: open with why a non-specialist should care, in the first minute, before any background | Childers 2021 (attendees came for learning and company); Dahlstrom 2014 (narrative raises interest); no test of an opening | convention, untested |
| Evidence is a result with its method; narrative is a framing device | A story is a legitimate carrier of the content for a lay audience: a person, a problem, what happened | Dahlstrom 2014 (recall, comprehension and reading time, full text; the health narratives it cites gave mixed results); Zebregs 2015 (held; health only; narrative moved intention, statistics moved belief) | supported with caveat |
| Material not on the point is cut (coherence) | Humour or an anecdote is allowed when it is tied to the point; unrelated humour is cut like any other detail | Zhou 2025 (related humour helps perceived learning, rapport); Kaplan 1977, Suzuki 2014 (secondary; delayed retention, recognition); Garner 2006 (one experiment: related humour raised recall); Sundararajan 2020 (held) | supported with caveat; affect is clear, learning mixed |
| The slot is fixed by the conference; the talk fills it | The slot may be very short (3 to 10 minutes) and is a hard limit: one idea, no outline slide, nothing that needs a second idea to be understood | Bakcek 2020 (held; equal test scores); the competition rules and four guides (all examples); no test against a longer talk | convention, untested |
| Slides support the talk | Slides are optional: none, one, or a few; a live demo is a choice with a stated risk | TED 2026; Baker 2018 (held; slides neutral on average, g = 0.067 with a CI through zero; K-12 gained); Savoy 2009 (not verified: abstract never reached); Shah 2023 (held; live code taught no more than static); PyCon 2026 (example; never do a live demo) | convention, untested for none; measured for "neutral on average" (Baker 2018) |
| Questions come at the end | In a small room, questions may be taken during the talk, as discussion; the speaker repeats each question | Hunsu 2016 (classes; the questions, not the device, carry the gain); Hilton 2022, PyCon 2026 (examples) | supported with caveat (classes); convention for talks |

- Weakest rows: the opening, the short slot and slides-optional. Each has no test on a casual talk.
- Strongest rows: assume no prior knowledge, and humour tied to the point. Each rests on reviews, though of text, recordings or posts.
- The story row is the one practice and the evidence agree on, and the evidence is from text and health messages.

### Rules that do not change

| Base rule | Why it holds in a casual talk |
|---|---|
| One claim per slide; sentence headline stating the claim; a figure as the evidence | Garner 2013 (held); the guides above ask for the same, less text and one thought per slide |
| Words on screen add to the voice, not repeat it | Adesope 2012 (held; spoken plus written text beat spoken alone only for low prior knowledge, system-paced and picture-free material, and equalled written alone; it did not test adding against repeating), Noetel 2022 (held); nothing in Q10 contradicts it |
| Contrast, legible type, colour never the only cue | A cafe or a classroom is still a room with a back row; W3C 2023, Rector 2019 (held) |
| Say where the evidence is weak | A lay audience cannot check; McCarthy 2025 counts a "general public" framing as simplistic |
| Rehearse aloud and time it; test the room and the file | Guides agree (PyCon 2026, WooCommerce 2026); preparedness was the best supported cue in Q9 |
| A conversational, first-person voice | Ginns 2013 (lessons on computer or paper, no live talk: applied here by analogy) and Mayer 2014c (held); the base already asks for a spoken, personal tone, so the casual talk differs in degree only |
| Segment long material | Rey 2019 (held); a casual slot is short, so the rule rarely applies |
| Gesture and pointing | Dargue 2019, Hostetter 2011 (held); no casual-specific test |

### Not overridden, because no evidence was found

- A talk with no slides: no study compares it with slides.
- A lightning talk against a longer talk for the same content: no study.
- Talks among friends or classmates: no study found beyond classroom PechaKucha trials.
- Colour, motion and font size for casual talks: no difference found against the base.
- Popularity as a goal: neither Segal 2026 nor Sugimoto 2013 measures learning.

## What this review did not verify

- Cromley 2025 and Zhu 2024 numbers come from a summary (secondary). Books Duarte 2008, Duarte 2010, Reynolds 2008, Anderson 2016, Minto 1987 and Tufte 2003 were scored from catalogue pages or not read.
- Works described by title or abstract only: Alley 2005, Alley 2006, Dubois 1980, Hood 2005, Rowley-Jolivet 2002, Alon 2009, Minto 1987, Duarte 2008 and 2010, Reynolds 2008, Anderson 2016.
- Effect sizes read in abstracts or secondary pages are marked "(secondary)".
- Q7 and Q8: many numbers come from abstracts or search summaries, marked in sources.md. Not read beyond titles and listings: Plass 2014, Nunez 2018, Petroff 2021, Birch 2012, Wong 2011 and Selvaraj 2021.
- Full texts of Richter 2016 and Schneider 2018 were not read, so colour as a moderator is unsettled.
- A Tufte page on projection and a colour PDF were unreachable.
- OpenAlex answered HTTP 429, so formal counts for the new strings come from ERIC and arXiv.
- This is a lighter MLR (protocol.md): the grey search was run to a stated rule, the formal pool was not. Absence of a study means this search did not find it.
