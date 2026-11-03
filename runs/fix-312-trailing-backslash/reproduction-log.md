$ ["sh", "-c", "PYTHONPATH=src python3 -m unittest tests.test_trailing_backslash_position"]
FFFFFF..
======================================================================
FAIL: test_trailing_backslash_reports_eof (tests.test_trailing_backslash_position.TestTrailingBackslashPosition.test_trailing_backslash_reports_eof) (document='v = "\\')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tinker/dev/worktrees/tomli/fix-312-trailing-backslash/tests/test_trailing_backslash_position.py", line 23, in test_trailing_backslash_reports_eof
    self.assertEqual(error.pos, len(document))
AssertionError: 7 != 6

======================================================================
FAIL: test_trailing_backslash_reports_eof (tests.test_trailing_backslash_position.TestTrailingBackslashPosition.test_trailing_backslash_reports_eof) (document='v = "abc\\')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tinker/dev/worktrees/tomli/fix-312-trailing-backslash/tests/test_trailing_backslash_position.py", line 23, in test_trailing_backslash_reports_eof
    self.assertEqual(error.pos, len(document))
AssertionError: 10 != 9

======================================================================
FAIL: test_trailing_backslash_reports_eof (tests.test_trailing_backslash_position.TestTrailingBackslashPosition.test_trailing_backslash_reports_eof) (document='v = """\\')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tinker/dev/worktrees/tomli/fix-312-trailing-backslash/tests/test_trailing_backslash_position.py", line 23, in test_trailing_backslash_reports_eof
    self.assertEqual(error.pos, len(document))
AssertionError: 9 != 8

======================================================================
FAIL: test_trailing_backslash_reports_eof (tests.test_trailing_backslash_position.TestTrailingBackslashPosition.test_trailing_backslash_reports_eof) (document='v = """\nabc\n\\')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tinker/dev/worktrees/tomli/fix-312-trailing-backslash/tests/test_trailing_backslash_position.py", line 23, in test_trailing_backslash_reports_eof
    self.assertEqual(error.pos, len(document))
AssertionError: 14 != 13

======================================================================
FAIL: test_trailing_backslash_reports_eof (tests.test_trailing_backslash_position.TestTrailingBackslashPosition.test_trailing_backslash_reports_eof) (document='"\\')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tinker/dev/worktrees/tomli/fix-312-trailing-backslash/tests/test_trailing_backslash_position.py", line 23, in test_trailing_backslash_reports_eof
    self.assertEqual(error.pos, len(document))
AssertionError: 3 != 2

======================================================================
FAIL: test_trailing_backslash_reports_eof (tests.test_trailing_backslash_position.TestTrailingBackslashPosition.test_trailing_backslash_reports_eof) (document='\n"abc\\')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/tinker/dev/worktrees/tomli/fix-312-trailing-backslash/tests/test_trailing_backslash_position.py", line 23, in test_trailing_backslash_reports_eof
    self.assertEqual(error.pos, len(document))
AssertionError: 7 != 6

----------------------------------------------------------------------
Ran 3 tests in 0.005s

FAILED (failures=6)
