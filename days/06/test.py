"""Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""

from io import StringIO

import pytest

from main import execute_problem, parse_problems, Problem


def test_parse_problems() -> None:
    strings = StringIO("1 2\n345 678\n+ *")
    expected_problems = [
        ("+", (1, 345)),
        ("*", (2, 678)),
    ]
    assert parse_problems(strings) == expected_problems


@pytest.mark.parametrize(
    ("problem", "expected_result"),
    [
        (("*", (123, 45, 6)), 33210),
        (("+", (328, 64, 98)), 490),
    ],
)
def test_execute_problem(problem: Problem, expected_result: int) -> None:
    assert execute_problem(problem) == expected_result
