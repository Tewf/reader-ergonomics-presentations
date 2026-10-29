"""Deck builds: a slide with `min_items` points or more, none of them revealed one at a time.

Points shown in step with the voice help over a whole slide at once (principle: reveal with the voice). A point is
revealed when it, or an element inside the slide, carries the class "fragment". A plan slide is shown whole, on purpose.

Heuristic: the threshold is PROVISIONAL in config. Time O(deck).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _deck import decks, is_aside, slides  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "deck-builds"
EXACT = False


def check(root: Path, config: dict) -> list[Finding]:
    minimum = config.get("deck_builds", {}).get("min_items", 4)
    findings = []
    for path in decks(root, config):
        for number, slide in enumerate(slides((root / path).read_text(encoding="utf-8", errors="replace"))[0], 1):
            if slide.items >= minimum and not slide.fragments and not is_aside(slide, config) and "plan" not in slide.classes:
                findings.append(Finding(NAME, path, slide.line, f"slide {number} shows {slide.items} points at once: "
                                        "reveal them as you say them (class \"fragment\")", "warning"))
    return findings
