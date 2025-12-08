"""Day 5: Cafeteria

https://adventofcode.com/2025/day/5
"""

import pytest

from main import Range


@pytest.mark.parametrize(
    ("string", "expected_range"),
    [
        ("3-5", (3, 5)),
        ("10-14", (10, 14)),
    ],
)
def test_range_from_string(string: str, expected_range: tuple[int, int]) -> None:
    assert Range.from_string(string).bounds == expected_range
