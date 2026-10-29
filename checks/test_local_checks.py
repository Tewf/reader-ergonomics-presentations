"""Tests of the deck checks in local/: each fires on a deck that breaks its rule and stays quiet on one that keeps it.

Run with the standard's checks on the path, as CI does:
    PYTHONPATH=<reader-ergonomics>/checks python3 -m unittest discover -s checks -p "test_*.py"
"""
from __future__ import annotations

import importlib.util
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG = tomllib.loads((HERE / "config.toml").read_text(encoding="utf-8"))
GOOD = (HERE.parent / "shapes" / "example-talk.html").read_text(encoding="utf-8")


def load(name: str):
    sys.path.insert(0, str(HERE / "local"))
    spec = importlib.util.spec_from_file_location(f"local_{name}", HERE / "local" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(check: str, files: dict[str, str]) -> list:
    """Run one check on a folder holding the given files (outside git, so every file is in scope)."""
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        for name, text in files.items():
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(text, encoding="utf-8")
        return load(check).check(root, CONFIG)


def deck(*sections: str, style: str = "") -> str:
    return f"<html><head><style>{style}</style></head><body>{''.join(sections)}</body></html>"


TITLE = '<section class="title"><h1>Every slide should state its claim</h1></section>'
PLAN = '<section class="plan"><h2>This talk makes three points today</h2><ul><li>a</li><li>b</li><li>c</li></ul></section>'
QUESTIONS = '<section class="questions"><h2>Questions</h2></section>'


class TestDeckChecks(unittest.TestCase):
    def test_example_deck_passes_every_program_check(self):
        css = (HERE.parent / "shapes" / "example-talk.css").read_text(encoding="utf-8")
        for check in ("slide_words", "deck_builds", "slide_headlines", "slide_type_size", "talk_structure"):
            with self.subTest(check=check):
                self.assertEqual(run(check, {"shapes/example-talk.html": GOOD, "shapes/example-talk.css": css}), [])

    def test_slide_words_flags_a_script(self):
        script = " ".join(["word"] * 60)
        found = run("slide_words", {"a.deck.html": deck(TITLE, f"<section><h2>A long slide with a script</h2><p>{script}</p></section>")})
        self.assertEqual(len(found), 1)

    def test_slide_words_ignores_speaker_notes(self):
        notes = " ".join(["word"] * 60)
        found = run("slide_words", {"a.deck.html": deck(TITLE, f'<section><h2>A short slide</h2><aside class="notes">{notes}</aside></section>')})
        self.assertEqual(found, [])

    def test_deck_builds_flags_five_points_at_once(self):
        points = "".join(f"<li>point {n}</li>" for n in range(5))
        self.assertEqual(len(run("deck_builds", {"a.deck.html": deck(TITLE, f"<section><h2>Five points shown at once</h2><ul>{points}</ul></section>")})), 1)

    def test_deck_builds_accepts_fragments(self):
        points = "".join(f'<li class="fragment">point {n}</li>' for n in range(5))
        self.assertEqual(run("deck_builds", {"a.deck.html": deck(TITLE, f"<section><h2>Five points shown in step</h2><ul>{points}</ul></section>")}), [])

    def test_slide_headlines_flags_a_topic_label(self):
        found = run("slide_headlines", {"a.deck.html": deck(TITLE, "<section><h2>Results</h2></section>", QUESTIONS)})
        self.assertEqual(len(found), 1)

    def test_slide_type_size_flags_small_type(self):
        self.assertEqual(len(run("slide_type_size", {"a.deck.html": deck(TITLE, style="p { font-size: 12pt; }")})), 1)

    def test_slide_type_size_skips_notes(self):
        self.assertEqual(run("slide_type_size", {"a.deck.html": deck(TITLE, style="aside.notes { font-size: 12px; }")}), [])

    def test_talk_structure_flags_each_missing_part(self):
        body = "<section><h2>The solver finds short tours fast</h2></section>"
        found = run("talk_structure", {"a.deck.html": deck(TITLE, body, body, body)})
        self.assertEqual(len(found), 3)  # no plan, no return to the point, no questions slide

    def test_talk_structure_takes_a_long_list_for_a_plan(self):
        """Known limit: a list of 2 to 5 points in the first slides counts as a plan, whatever it says."""
        points = "".join(f"<li>{n}</li>" for n in range(5))
        found = run("talk_structure", {"a.deck.html": deck(TITLE, f"<section><h2>Methods we compared today</h2><ul>{points}</ul></section>", QUESTIONS)})
        self.assertFalse(any("no plan" in finding.message for finding in found))

    def test_deck_judgment_asks_three_questions_per_deck(self):
        found = run("deck_judgment", {"a.deck.html": deck(TITLE)})
        self.assertEqual([finding.kind for finding in found], ["judgment"] * 3)


if __name__ == "__main__":
    unittest.main()
