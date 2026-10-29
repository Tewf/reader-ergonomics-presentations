"""Talk structure: a deck says its plan early, ends on the point it opened with, and prepares for questions.

Three findings, one per missing part (principles: a talk is not a paper; plan the questions):
- no plan in the first `plan_within` slides: a slide with the class "plan", or a list of 2 to 5 points; a deck that
  declares a slot of `short_slot_minutes` or less (`<html data-minutes="5">`) needs none, as the casual context says;
- the last content slide shares no word of four letters or more with the first slide's headline, and is not marked "point";
- no slide for questions or backup: the class "questions" or "backup", or a headline naming questions, backup or an appendix.

Heuristic: word overlap stands for "the same point". Time O(deck).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _deck import decks, is_aside, slides, slot_minutes  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "talk-structure"
EXACT = False
QUESTIONS = re.compile(r"\b(questions?|backup|appendix|annexes?)\b", re.IGNORECASE)


def content_words(text: str) -> set[str]:
    return {word.lower() for word in re.findall(r"[\w'’-]{4,}", text)}


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("talk_structure", {})
    within, short = settings.get("plan_within", 3), settings.get("short_slot_minutes", 10)
    findings = []
    for path in decks(root, config):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        shown, minutes = slides(text)[0], slot_minutes(text)
        if not shown:
            continue
        short_slot = minutes is not None and minutes <= short
        if not short_slot and not any("plan" in slide.classes or 2 <= slide.items <= 5 for slide in shown[:within]):
            findings.append(Finding(NAME, path, shown[0].line, f"no plan in the first {within} slides: say the parts of the "
                                    "talk early (a slide with the class \"plan\", or a list of 2 to 5 points)", "warning"))
        content = [slide for slide in shown[1:] if not is_aside(slide, config)]
        if content and "point" not in content[-1].classes and not content_words(shown[0].title) & content_words(content[-1].title):
            findings.append(Finding(NAME, path, content[-1].line, "the last slide does not come back to the opening point: "
                                    "end on it, or mark the closing slide with the class \"point\"", "warning"))
        if not any(slide.classes & {"questions", "backup"} or QUESTIONS.search(slide.title) for slide in shown):
            findings.append(Finding(NAME, path, shown[-1].line, "no slide for questions or backup: prepare the likely "
                                    "questions, with backup slides", "warning"))
    return findings
