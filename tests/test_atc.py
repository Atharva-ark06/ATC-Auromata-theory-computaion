"""Regression tests for the three ATC assignment levels."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSIGNMENTS = ROOT / "assignment 1"


def load_module(name: str, filename: str):
    """Load an assignment module without requiring a package name with spaces."""
    spec = importlib.util.spec_from_file_location(name, ASSIGNMENTS / filename)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {filename}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


level1 = load_module("atc_level1", "Level1.py")
level2 = load_module("atc_level2", "Level2.py")
level3 = load_module("atc_level3", "Level3.py")


class IdentifierRecognitionTests(unittest.TestCase):
    def test_accepts_valid_identifiers(self):
        for value in ("x", "total1", "_var", "abc123", "with_under_score"):
            with self.subTest(value=value):
                self.assertTrue(level1.is_valid_identifier(value))

    def test_rejects_invalid_identifiers(self):
        for value in ("", "1x", "123", "ab-c", "a$b", "has space"):
            with self.subTest(value=value):
                self.assertFalse(level1.is_valid_identifier(value))


class LexerTests(unittest.TestCase):
    def test_classifies_miniatc_tokens(self):
        lexer = level2.Lexer("begin int count = 42; print(count); end")
        tokens = []
        while True:
            token = lexer.next_token()
            if token.type == level2.TOKEN_EOF:
                break
            tokens.append((token.type, token.value))

        self.assertEqual(tokens[0], (level2.TOKEN_KEYWORD, "begin"))
        self.assertIn((level2.TOKEN_IDENTIFIER, "count"), tokens)
        self.assertIn((level2.TOKEN_NUMBER, "42"), tokens)
        self.assertIn((level2.TOKEN_OPERATOR, "="), tokens)
        self.assertIn((level2.TOKEN_DELIMITER, ";"), tokens)
        self.assertEqual(tokens[-1], (level2.TOKEN_KEYWORD, "end"))

    def test_tracks_line_numbers(self):
        lexer = level2.Lexer("begin\nint x;")
        self.assertEqual(lexer.next_token().line, 1)
        self.assertEqual(lexer.next_token().line, 2)

    def test_unknown_character_is_reported(self):
        lexer = level2.Lexer("@")
        token = lexer.next_token()
        self.assertEqual(token.type, level2.TOKEN_UNKNOWN)
        self.assertEqual(token.value, "@")


class ParserTests(unittest.TestCase):
    def parse_without_console_output(self, source: str) -> int:
        parser = level3.Parser(source)
        with contextlib.redirect_stdout(io.StringIO()):
            parser.parse_program()
        return parser.errors

    def test_accepts_valid_program(self):
        source = "begin int x; x = 10 + 5 * (2 - 1); print(x); end"
        self.assertEqual(self.parse_without_console_output(source), 0)

    def test_rejects_missing_semicolon(self):
        source = "begin int x x = 10; end"
        self.assertGreater(self.parse_without_console_output(source), 0)

    def test_rejects_unexpected_character(self):
        source = "begin @ end"
        self.assertGreater(self.parse_without_console_output(source), 0)


if __name__ == "__main__":
    unittest.main()
