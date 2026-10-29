"""Deck judgment: what a program cannot see in a deck is asked, once per deck, of whoever judges.

Three questions (principles: motion adds, never replaces; colour as a signal; gesture with the words). The answers go
to checks/judgments.toml like every judgment of the standard, and hold until the deck changes.

Judgment. Time O(decks).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _deck import decks  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "deck-judgment"
EXACT = False
QUESTIONS = (
    "Does any animation, video or live demo replace an explanation instead of adding to one?",
    "Is colour anywhere the only cue that tells two things apart, or does a data colour map run out of perceptual order?",
    "Do the speaker notes plan gestures that point at what is said, rather than a reading of the slides?",
)


def check(root: Path, config: dict) -> list[Finding]:
    return [Finding(NAME, path, 0, question, "judgment") for path in decks(root, config) for question in QUESTIONS]
