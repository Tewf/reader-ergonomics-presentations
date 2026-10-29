"""Figure width: a text figure wider than `max_columns` overflows the page column and hides its right side.

A fenced block marked `text`, or with no language, is a figure drawn in characters (a tree, a flow, a map). Past the
width of the text around it, a site shows it behind a horizontal scrollbar and a phone cuts it off: the reader sees
half the relation the figure was drawn to show. Code blocks with a language are left alone, since code cannot be
reflowed. The usual fix keeps the figure: put each node's description on the line under the node, not beside it.

Heuristic: the width is PROVISIONAL in config; no study gives one for figures, so it sits at the narrow end of
reader-ergonomics' readable measure (45 to 75 characters), so a figure fits wherever its text fits. Time O(text).
"""
from __future__ import annotations

import re
from pathlib import Path

from framework.check_api import MARKDOWN_SUFFIXES, Finding, files_in_scope, matches_any

NAME = "figure-width"
EXACT = False
FENCE = re.compile(r"^(`{3,}|~{3,})[ \t]*([\w-]*)[^\n]*\n(.*?)^\1[`~]*[ \t]*$", re.MULTILINE | re.DOTALL)


def check(root: Path, config: dict) -> list[Finding]:
    settings = config.get("figure_width", {})
    limit, exempt = settings.get("max_columns", 60), settings.get("exempt", [])
    findings = []
    for path in files_in_scope(root, config, MARKDOWN_SUFFIXES):
        if matches_any(path, exempt):
            continue
        text = (root / path).read_text(encoding="utf-8", errors="replace")
        for fence in FENCE.finditer(text):
            if fence.group(2) not in ("", "text"):
                continue
            width = max((len(line.rstrip()) for line in fence.group(3).splitlines()), default=0)
            if width > limit:
                line = text.count("\n", 0, fence.start()) + 1
                findings.append(Finding(NAME, path, line, f"a text figure {width} columns wide, past {limit}: it overflows "
                                        "the column; put each description under its node", "warning"))
    return findings
