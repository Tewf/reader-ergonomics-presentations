"""Slide type size: a font size below `min_px` in a deck's stylesheets is hard to read from the back of a room.

Read in the deck's inline <style> and in the local stylesheets it links. Sizes in px and pt are compared (1pt = 4/3 px);
relative sizes are left alone. Rules for speaker notes (selectors naming "notes") are left out.

Heuristic: the minimum is a convention, PROVISIONAL in config, since no study gives one. Time O(stylesheets).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _deck import decks, slides  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "slide-type-size"
EXACT = False
RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")
SIZE = re.compile(r"font-size\s*:\s*([\d.]+)\s*(px|pt)\b")


def check(root: Path, config: dict) -> list[Finding]:
    minimum = config.get("slide_type_size", {}).get("min_px", 24)
    findings = []
    for path in decks(root, config):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        _, inline, links = slides(text)
        sheets = [(path, css) for css in inline]
        for link in links:
            local = (root / path).parent / link
            if not re.match(r"^[a-z]+:", link) and local.is_file():
                sheets.append((local.relative_to(root).as_posix(), local.read_text(encoding="utf-8", errors="replace")))
        for where, css in sheets:
            for selector, body in RULE.findall(css):
                if "notes" in selector:
                    continue
                for value, unit in SIZE.findall(body):
                    pixels = float(value) * (4 / 3 if unit == "pt" else 1)
                    if pixels < minimum:
                        findings.append(Finding(NAME, where, 0, f"'{selector.strip()}' sets {value}{unit}, under {minimum}px: "
                                                "too small for the back of a room", "warning"))
    return findings
