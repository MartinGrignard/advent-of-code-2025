"""Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""

from io import StringIO

import pytest

from main import (
    Assessment,
    execute_problem,
    parse_problems,
    parse_problem_horizontally,
    Problem,
    split_assessments,
)


def test_split_assessments() -> None:
    strings = StringIO(
        "123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  \n"
    )
    expected_assessments = [
        ("123", " 45", "  6", "*  "),
        ("328", "64 ", "98 ", "+  "),
        (" 51", "387", "215", "*  "),
        ("64 ", "23 ", "314", "+  "),
    ]
    res = list(split_assessments(strings))
    print(res)
    assert res == expected_assessments


@pytest.mark.parametrize(
    ("assessment", "expected_problem"),
    [
        (("123", " 45", "  6", "*  "), ("*", (123, 45, 6))),
        (("328", "64 ", "98 ", "+  "), ("+", (328, 64, 98))),
        ((" 51", "387", "215", "*  "), ("*", (51, 387, 215))),
        (("64 ", "23 ", "314", "+  "), ("+", (64, 23, 314))),
    ],
)
def test_parse_problem_horizontally(
    assessment: Assessment, expected_problem: Problem
) -> None:
    assert parse_problem_horizontally(assessment) == expected_problem


@pytest.mark.parametrize(
    ("problem", "expected_result"),
    [
        (("*", (123, 45, 6)), 33210),
        (("+", (328, 64, 98)), 490),
    ],
)
def test_execute_problem(problem: Problem, expected_result: int) -> None:
    assert execute_problem(problem) == expected_result
