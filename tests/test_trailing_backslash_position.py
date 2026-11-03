# SPDX-License-Identifier: MIT
# Licensed to PSF under a Contributor Agreement.

import unittest

from . import tomllib


class TestTrailingBackslashPosition(unittest.TestCase):
    def test_trailing_backslash_reports_eof(self):
        for document in (
            'v = "\\',
            'v = "abc\\',
            'v = """\\',
            'v = """\nabc\n\\',
            '"\\',
            '\n"abc\\',
        ):
            with self.subTest(document=document):
                with self.assertRaises(tomllib.TOMLDecodeError) as caught:
                    tomllib.loads(document)
                error = caught.exception
                self.assertEqual(error.pos, len(document))
                self.assertEqual(error.lineno, document.count("\n") + 1)
                self.assertEqual(error.colno, len(document.rsplit("\n", 1)[-1]) + 1)
                self.assertEqual(error.doc, document)
                self.assertEqual(
                    str(error), "Unescaped '\\' in a string (at end of document)"
                )

    def test_unchanged_error_positions(self):
        for document, pos, lineno, colno, message, location in (
            ('v = "abc', 8, 1, 9, "Unterminated string", "end of document"),
            ('v = """\nabc', 11, 2, 4, "Unterminated string", "end of document"),
            ('"abc', 4, 1, 5, "Unterminated string", "end of document"),
            ('v = "\\q"', 7, 1, 8, "Unescaped '\\' in a string", "line 1, column 8"),
            (
                'v = """\n\\q"""',
                10,
                2,
                3,
                "Unescaped '\\' in a string",
                "line 2, column 3",
            ),
            ('"\\q" = 1', 3, 1, 4, "Unescaped '\\' in a string", "line 1, column 4"),
            ('v = "\\uZZZZ"', 7, 1, 8, "Invalid hex value", "line 1, column 8"),
            (
                'v = """\\ x"""',
                9,
                1,
                10,
                "Unescaped '\\' in a string",
                "line 1, column 10",
            ),
        ):
            with self.subTest(document=document):
                with self.assertRaises(tomllib.TOMLDecodeError) as caught:
                    tomllib.loads(document)
                error = caught.exception
                self.assertEqual(
                    (error.pos, error.lineno, error.colno), (pos, lineno, colno)
                )
                self.assertEqual(str(error), f"{message} (at {location})")

    def test_valid_neighboring_escapes(self):
        self.assertEqual(tomllib.loads('v = "\\u0041\\U00000042"'), {"v": "AB"})
        self.assertEqual(tomllib.loads('v = """a\\ \n  b"""'), {"v": "ab"})
