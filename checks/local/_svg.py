"""Shared reading of SVG figures for this repository's figure judgment: which files it asks about.

Not a check: it defines no NAME. reader-ergonomics holds the program checks of figures (checks/figures/); only the
judgment, which rests on this repository's figure principles, stays here. Time O(files).
"""
from __future__ import annotations

from pathlib import Path

from framework.check_api import files_in_scope, matches_any


def figures(root: Path, config: dict, exempt: list[str]) -> list[str]:
    """Every SVG file in scope that is not exempt."""
    return [path for path in files_in_scope(root, config, {".svg"}) if not matches_any(path, exempt)]
