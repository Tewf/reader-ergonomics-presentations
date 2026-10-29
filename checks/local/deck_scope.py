"""Deck scope: the config names deck files, and none is in scope, so every deck check read nothing.

A clean run that read no deck looks like a pass. Files in a git-ignored folder are out of scope, which is the usual
cause; run the checks on a copy outside git, or name the decks in `[decks] files`.

Exact. Time O(files).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _deck import decks  # noqa: E402
from framework.check_api import Finding  # noqa: E402

NAME = "deck-scope"
EXACT = True


def check(root: Path, config: dict) -> list[Finding]:
    globs = config.get("decks", {}).get("files", [])
    if globs and not decks(root, config):
        return [Finding(NAME, "checks/config.toml", 0, f"no deck matches [decks] files {globs}: the deck checks read "
                        "nothing (a git-ignored folder is out of scope)")]
    return []
