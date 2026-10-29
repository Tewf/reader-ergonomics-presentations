# The presentations standard

What any presentation shares, as far as the evidence goes: the rules for a talk given to a room, with slides or
without. It extends [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/v1.0.0/standard.md), the
standard for any reader: read that one first. This page adds only what a talk changes, since a listener cannot set
the pace or read again.

## How to use it

```text
 who listens?
  ├─ a known audience ──▶ open its context in reader-styles/
  │                            │
  └─ unknown ──────────────────┤
                               ▼
                     start from the talk shape
                               ▼
                    build the deck to the principles
                               ▼
               python3 <reader-ergonomics>/checks/run.py .
                               ├─▶ error     certain: fix it
                               ├─▶ warning   fix it, or say why it is a false match
                               └─▶ judgment  answer it in checks/judgments.toml
```

1. **Name the audience.** A context overrides the base for its room: [academic audience](reader-styles/academic-audience.md)
   (a conference, a seminar, a defence), [business decision maker](reader-styles/business-decision-maker.md) or
   [casual audience](reader-styles/casual-audience.md) (a meetup, a club, friends).
2. **Start from the [talk shape](shapes/talk.md)**, or from its example deck, [example-talk.html](shapes/example-talk.html).
3. **Build to the principles** below, and to those of reader-ergonomics, which still hold.
4. **Check:** the deck checks of `checks/local/` run with the standard's own, on every HTML deck named in
   `checks/config.toml`.

Grades mean what they mean in [reader-ergonomics](https://github.com/Tewf/reader-ergonomics/blob/v1.0.0/standard.md#grades):
measured, supported with caveat, convention, not supported. Each principle states its grade and never claims more.

## Principles

<!-- principles:start -->

### Pace: the listener cannot reread

| Principle | Claim | Grade |
|---|---|---|
| [Motion adds, never replaces](principles/pace/motion-adds-never-replaces.md) | animation, video and live demos are added to an explanation, never in place of it. | supported with caveat |
| [No script on screen](principles/pace/no-script-on-screen.md) | words on screen do not repeat the voice: show key terms and the evidence, and say the rest. | measured |
| [Reveal with the voice](principles/pace/reveal-with-the-voice.md) | points appear as they are spoken, not a whole slide at once. | supported with caveat (recorded narration only) |

### Slide: what the room sees

| Principle | Claim | Grade |
|---|---|---|
| [Claim headline with evidence](principles/slide/claim-headline-with-evidence.md) | each slide's headline is a sentence stating its claim, and the slide shows the evidence. | supported with caveat (one controlled study of a bundle) |
| [Colour as a signal](principles/slide/colour-as-a-signal.md) | colour links what belongs together and is never the only cue; data colour maps are perceptually ordered. | measured for colour coding and for colour maps |
| [Legible in the room](principles/slide/legible-in-the-room.md) | text is readable from the back of the room: dark on light, high contrast, large type. | measured for polarity; the minimum size is a convention |

### Talk: the speaker and the hour

| Principle | Claim | Grade |
|---|---|---|
| [A talk is not a paper](principles/talk/a-talk-is-not-a-paper.md) | a talk is its own genre: it says its point and plan early, returns to them, and ends on the point. | supported with caveat (descriptive genre research) |
| [Gesture with the words](principles/talk/gesture-with-the-words.md) | the speaker gestures at what is said; a visible face adds nothing consistent. | measured |
| [Plan the questions](principles/talk/plan-the-questions.md) | the questions are part of the talk: the likely ones are prepared, with backup slides. | convention (the research is descriptive) |

<!-- principles:end -->

## Where the evidence is

Every principle links to the review in [evidence/presentations/](evidence/presentations/), and every work cited is
listed once in the [bibliography](evidence/bibliography.md).
