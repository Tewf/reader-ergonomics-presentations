"""Slide type size: a font size below `min_px` in a deck's stylesheets is hard to read from the back of a room.

Read in the deck's inline <style> and in the local stylesheets it links. Sizes in font-size or in the font shorthand, in px, pt (4/3 px) and vh (a hundredth of
`reference_height_px`, a 1080p projector by default) are compared; a `var(--name)` is resolved from the custom
properties the same stylesheets declare. em, rem and % are relative and left alone, as is text inside SVG. Rules for
speaker notes (selectors naming "notes") are left out.

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
SIZE = re.compile(r"([\d.]+)\s*(px|pt|vh)\b")
FONT_SIZE = re.compile(r"(?<![\w-])font(?:-size)?\s*:\s*([^;]+)")  # font-size, or the size in the font shorthand
CUSTOM = re.compile(r"(--[\w-]+)\s*:\s*([^;]+)")
VAR = re.compile(r"var\(\s*(--[\w-]+)\s*(?:,\s*([^)]+))?\)")


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("slide_type_size", {})
    minimum, height = settings.get("min_px", 24), settings.get("reference_height_px", 1080)
    per_unit = {"px": 1, "pt": 4 / 3, "vh": height / 100}
    findings = []
    for path in decks(root, config):
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        _, inline, links = slides(text)
        sheets = [(path, css) for css in inline]
        for link in links:
            local = (root / path).parent / link
            if not re.match(r"^[a-z]+:", link) and local.is_file():
                sheets.append((local.relative_to(root).as_posix(), local.read_text(encoding="utf-8", errors="replace")))
        custom = {name: value.strip() for _, css in sheets for name, value in CUSTOM.findall(css)}
        resolve = lambda text: VAR.sub(lambda m: custom.get(m.group(1), m.group(2) or ""), text)
        for where, css in sheets:
            for selector, body in RULE.findall(css):
                if "notes" in selector:
                    continue
                for declared in FONT_SIZE.findall(body):
                    sizes = SIZE.findall(resolve(resolve(declared)))
                    if not sizes or declared.strip().startswith(("clamp", "max(")):
                        continue  # a clamp or a max holds the type above its floor
                    value, unit = sizes[0]
                    pixels = float(value) * per_unit[unit]
                    if pixels < minimum:
                        findings.append(Finding(NAME, where, 0, f"'{selector.strip()}' sets {value}{unit}, under {minimum}px: "
                                                "too small for the back of a room", "warning"))
    return findings
