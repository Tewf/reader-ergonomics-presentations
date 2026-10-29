"""Figure judgment: what a program cannot see in a figure is asked, once per SVG figure, of whoever judges.

Two questions (principles few crossings, label in place, group by region, one message, position for quantities,
appeal after clarity). The answers go to checks/judgments.toml and hold until the figure changes.

Judgment. Time O(figures).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _svg import figures  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "figure-judgment"
EXACT = False
QUESTIONS = (
    "Layout and labels: do links cross where another layout would avoid it, is any part named only through a "
    "legend that labels could replace, and is membership shown by colour alone anywhere?",
    "Message and decoration: does the caption or alt text state the figure's one message, is a quantity shown by "
    "area or angle where position would do, and does any decoration distort a quantity or compete with the message?",
)


def check(root: Path, config: dict) -> list[Finding]:
    exempt = config.get("figure_judgment", {}).get("exempt", [])
    return [Finding(NAME, path, 0, question, "judgment") for path in figures(root, config, exempt) for question in QUESTIONS]
