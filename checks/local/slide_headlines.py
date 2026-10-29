"""Slide headlines: a content slide whose headline is missing or shorter than `min_words` names a topic, not a claim;
one longer than `max_words` is a paragraph, not a headline.

Each slide's headline states its claim in a sentence (principle: claim headline with evidence). Title, backup and
questions slides are left out.

Heuristic: length stands for "is a sentence"; the threshold is PROVISIONAL in config. Time O(deck).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _deck import decks, is_aside, slides  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "slide-headlines"
EXACT = False


def check(root: Path, config: dict) -> list[Finding]:
    minimum = config.get("slide_headlines", {}).get("min_words", 4)
    maximum = config.get("slide_headlines", {}).get("max_words", 15)
    findings = []
    for path in decks(root, config):
        for number, slide in enumerate(slides((root / path).read_text(encoding="utf-8", errors="replace"))[0], 1):
            if number == 1 or is_aside(slide, config):
                continue
            words = slide.title.split()
            if len(words) < minimum:
                shown = f'"{slide.title}"' if words else "no headline"
                findings.append(Finding(NAME, path, slide.line, f"slide {number} has {shown}: state the slide's claim "
                                        f"in a sentence of at least {minimum} words", "warning"))
            elif len(words) > maximum:
                findings.append(Finding(NAME, path, slide.line, f"slide {number}'s headline has {len(words)} words, past "
                                        f"{maximum}: one sentence the room reads at a glance", "warning"))
    return findings
