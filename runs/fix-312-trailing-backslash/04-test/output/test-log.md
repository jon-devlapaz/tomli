
$ ["sh", "-c", "PYTHONPATH=src python3 -m unittest"]
..............s......
----------------------------------------------------------------------
Ran 21 tests in 0.195s

OK (skipped=1)

# seed check seed-1
$ ["bash", "-c", "PYTHONPATH=src python3 -m unittest tests.test_trailing_backslash_position"]
cwd: .
expect (operator confirms): The new focused module passes assertions that trailing-backslash cases report pos == len(document), correct EOF lineno and colno, and an EOF displayed location across the shared callers, while unchanged-position controls retain their previous attributes and text.
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK

# seed check seed-2
$ ["bash", "-c", "PYTHONPATH=src python3 -m unittest tests.test_error"]
cwd: .
expect (operator confirms): The existing tests.test_error unittest module completes successfully with its displayed-location and public error-attribute assertions unchanged. Proposed check; not executed here.
.......
----------------------------------------------------------------------
Ran 7 tests in 0.004s

OK
