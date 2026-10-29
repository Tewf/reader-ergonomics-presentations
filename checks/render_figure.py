"""Render a Graphviz source to the SVG beside it, stamped with the hash of the source.

Usage: python3 checks/render_figure.py FIGURE.dot [...]

Writes FIGURE.svg next to FIGURE.dot, with `<!-- source-sha256: H -->` after the XML prolog, H being the SHA-256 of
the .dot file's bytes; the check figure-source compares the two. Needs Graphviz's `dot` on the PATH.
"""
import hashlib
import subprocess
import sys
from pathlib import Path


def render(source: Path) -> Path:
    svg = subprocess.run(["dot", "-Tsvg", str(source)], capture_output=True, text=True, check=True).stdout
    stamp = f"<!-- source-sha256: {hashlib.sha256(source.read_bytes()).hexdigest()} -->\n"
    head, _, rest = svg.partition("?>\n") if svg.startswith("<?xml") else ("", "", svg)
    target = source.with_suffix(".svg")
    target.write_text((head + "?>\n" if head else "") + stamp + rest, encoding="utf-8")
    return target


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for name in sys.argv[1:]:
        print(render(Path(name)))
