"""Slide words: a slide that shows more than `max_words` words puts the script on screen.

The listener cannot read and listen at once (principle: no script on screen). Speaker notes are not counted, nor
numbers, nor the title and backup slides, which are not read during the talk.

Heuristic: the threshold is PROVISIONAL in config. Time O(deck).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _deck import decks, slides  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "slide-words"
EXACT = False


def check(root: Path, config: dict) -> list[Finding]:
    limit = config.get("slide_words", {}).get("max_words", 40)
    findings = []
    for path in decks(root, config):
        for number, slide in enumerate(slides((root / path).read_text(encoding="utf-8", errors="replace"))[0], 1):
            words = [word for word in slide.words if re.search(r"[^\W\d_]", word)]  # a number is not a word of script
            if not slide.classes & {"title", "backup"} and len(words) > limit:
                findings.append(Finding(NAME, path, slide.line, f"slide {number} shows {len(words)} words, past {limit}: "
                                        "keep the key terms on screen and say the rest", "warning"))
    return findings
