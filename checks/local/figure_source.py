"""Figure source: an SVG drawn from a `.dot` file was rendered from the source that sits beside it now.

For every `X.svg` with an `X.dot` beside it, the SVG must hold the comment `<!-- source-sha256: H -->`, where H is
the SHA-256 of the `.dot` file's bytes. `checks/render_figure.py X.dot` renders the SVG with Graphviz and writes that
comment, so an edit to the source that was not rendered, or a drawing edited by hand, fails here (principle drawn
from source). Graphviz is not needed to run the check.

Exact. Time O(figures).
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _svg import figures  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "figure-source"
EXACT = True
STAMP = re.compile(r"<!-- source-sha256: ([0-9a-f]{64}) -->")


def check(root: Path, config: dict) -> list[Finding]:
    findings = []
    for path in figures(root, config, config.get("figure_source", {}).get("exempt", [])):
        source = (root / path).with_suffix(".dot")
        if not source.exists():
            continue
        stamp = STAMP.search((root / path).read_text(encoding="utf-8", errors="replace"))
        wanted = hashlib.sha256(source.read_bytes()).hexdigest()
        if not stamp:
            findings.append(Finding(NAME, path, 1, f"no source stamp: render it with checks/render_figure.py {source.name}"))
        elif stamp.group(1) != wanted:
            findings.append(Finding(NAME, path, 1, f"rendered from another version of {source.name}: "
                                                   f"render it again with checks/render_figure.py"))
    return findings
