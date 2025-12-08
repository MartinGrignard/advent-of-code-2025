"""Day 5: Cafeteria

https://adventofcode.com/2025/day/5
"""

import pytest

from main import Range, Ranges


@pytest.mark.parametrize(
    ("string", "expected_range"),
    [
        ("3-5", (3, 5)),
        ("10-14", (10, 14)),
    ],
)
def test_range_from_string(string: str, expected_range: tuple[int, int]) -> None:
    assert Range.from_string(string).bounds == expected_range


@pytest.mark.parametrize(
    ("value", "expected_answer"),
    [
        (1, True),
        (3, True),
        (0, False),
        (4, False),
    ],
)
def test_range_contains(value: int, expected_answer: bool) -> None:
    assert (value in Range(1, 3)) == expected_answer


@pytest.mark.parametrize(
    ("value", "expected_answer"),
    [
        (1, True),
        (8, True),
        (5, False),
    ],
)
def test_ranges_contains(value: int, expected_answer: bool) -> None:
    assert (value in Ranges([Range(1, 3), Range(8, 10)])) == expected_answer
