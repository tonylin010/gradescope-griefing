# Challenge 0: Tutorial Level

## Autograder
This is a diabolically insecure autograder. It stores the contents-to-be of [results.json](https://gradescope-autograders.readthedocs.io/en/latest/specs/) in a Python dictionary called `d` then uses `exec()` to evaluate Python code run from a file; effictively copy-pasting the code in lieu of the function call. Feel free to review the autograder code in [grade.py](grade.py).

## Constraints
Submission should be valid Python code in a file `main.py`. Go crazy.

## Solution
- [Grade change](change_grade/main.py) simply access `d["score"]` and change grades that way.
- [Crash autograder](crash/main.py): Use the `subprocess` module to call `pkill python3`.
