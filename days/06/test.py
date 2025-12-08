"""Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""

from io import StringIO

from main import parse_problems


def test_parse_problems() -> None:
    strings = StringIO("1 2\n345 678\n+ *")
    expected_problems = [
        ("+", (1, 345)),
        ("*", (2, 678)),
    ]
    assert parse_problems(strings) == expected_problems
