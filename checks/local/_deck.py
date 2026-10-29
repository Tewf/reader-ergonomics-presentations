"""Read an HTML deck into slides: one slide per innermost <section>, speaker notes left out.

A deck is an HTML file whose slides are <section> elements, the convention of reveal.js and of plain HTML decks.
Text inside <aside class="notes">, <script> and <style> is not shown to the room, so it is not counted. Shared by the
deck checks in this folder; it has no NAME, so the runner does not take it for a check.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

from framework.check_api import files_in_scope, matches_any

HIDDEN = {"script", "style", "template"}
HEADINGS = {"h1", "h2", "h3"}
MEDIA = {"img", "svg", "canvas", "video", "figure", "picture", "iframe"}
VOID = {"img", "br", "hr", "meta", "link", "input", "source", "area", "base", "col", "embed", "track", "wbr"}


class Slide:
    """One slide: where it starts, its classes, its headline, the words it shows, its points, reveals and media.

    A plain class, not a dataclass: the runner loads this file without registering it as a module, which a dataclass needs.
    """

    def __init__(self, line: int, classes: set[str]) -> None:
        self.line, self.classes, self.title, self.words = line, classes, "", []
        self.items = self.fragments = self.media = 0
        self.has_child_section = False


class _DeckParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides: list[Slide] = []
        self.open_slides: list[Slide] = []
        self.hidden_depth = 0
        self.notes_depth = 0
        self.heading_depth = 0
        self.stack: list[str] = []
        self.styles: list[str] = []
        self.links: list[str] = []
        self.inline: list[str] = []  # style attributes, read by the type-size check
        self.minutes: float | None = None  # the slot, from data-minutes on <html> or <body>
        self._in_style = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = set((attributes.get("class") or "").split())
        if tag in ("html", "body") and attributes.get("data-minutes"):
            try:
                self.minutes = float(attributes["data-minutes"])
            except ValueError:
                pass
        if attributes.get("style") and not self.notes_depth:
            self.inline.append(attributes["style"])
        if tag == "link" and "stylesheet" in (attributes.get("rel") or ""):
            self.links.append(attributes.get("href") or "")
        if tag in VOID:
            self._count(tag, classes)
            return
        self.stack.append(tag)
        if tag == "style":
            self._in_style = True
        if tag in HIDDEN:
            self.hidden_depth += 1
        if tag == "aside" and "notes" in classes:
            self.notes_depth += 1
        if tag == "section":
            if self.open_slides:
                self.open_slides[-1].has_child_section = True
            slide = Slide(line=self.getpos()[0], classes=classes)
            self.open_slides.append(slide)
            self.slides.append(slide)
        if tag in HEADINGS and self.open_slides and not self.open_slides[-1].title:
            self.heading_depth += 1
        self._count(tag, classes)

    def _count(self, tag, classes):
        if not self.open_slides or self.notes_depth:
            return
        slide = self.open_slides[-1]
        slide.items += tag == "li"
        slide.media += tag in MEDIA
        slide.fragments += "fragment" in classes

    def handle_endtag(self, tag):
        if tag in VOID or tag not in self.stack:
            return
        while self.stack:
            closed = self.stack.pop()
            if closed == "style":
                self._in_style = False
            if closed in HIDDEN:
                self.hidden_depth -= 1
            if closed == "aside" and self.notes_depth:
                self.notes_depth -= 1
            if closed in HEADINGS and self.heading_depth:
                self.heading_depth -= 1
            if closed == "section" and self.open_slides:
                self.open_slides.pop()
            if closed == tag:
                break

    def handle_data(self, data):
        if self._in_style:
            self.styles.append(data)
        if self.hidden_depth or self.notes_depth or not self.open_slides:
            return
        slide = self.open_slides[-1]
        words = re.findall(r"[\w'’-]+", data)
        slide.words.extend(words)
        if self.heading_depth:
            slide.title = (slide.title + " " + " ".join(words)).strip()


def slides(text: str) -> tuple[list[Slide], list[str], list[str]]:
    """The slides a room sees (innermost sections), the inline stylesheets, and the linked stylesheet paths.

    The style attributes of elements come in as rules of a selector named "style attribute".
    """
    parser = _DeckParser()
    parser.feed(text)
    parser.close()
    shown = [slide for slide in parser.slides if not slide.has_child_section]
    styles = parser.styles + [f"style attribute {{{declarations}}}" for declarations in parser.inline]
    return shown, styles, parser.links


def slot_minutes(text: str) -> float | None:
    """The length of the slot a deck declares, `<html data-minutes=\"5\">`, in minutes; None when it declares none."""
    parser = _DeckParser()
    parser.feed(text)
    parser.close()
    return parser.minutes


def decks(root: Path, config: dict) -> list[str]:
    """The deck files in scope: the globs of [decks] files, minus [decks] exempt."""
    settings = config.get("decks", {})
    globs, exempt = settings.get("files", []), settings.get("exempt", [])
    return [path for path in files_in_scope(root, config, {".html", ".htm"})
            if matches_any(path, globs) and not matches_any(path, exempt)]


def is_aside(slide: Slide, config: dict) -> bool:
    """A title, plan, backup or questions slide is not a content slide."""
    return bool(slide.classes & set(config.get("decks", {}).get("aside_classes", ["title", "backup", "questions"])))
