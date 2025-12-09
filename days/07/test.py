"""Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

import pytest

from main import parse_positions


@pytest.mark.parametrize(
    ("string", "expected_positions"),
    [
        (".S.", {1}),
        (".^..^.", {1, 4}),
    ],
)
def test_parse_positions(string: str, expected_positions: set[int]) -> None:
    assert parse_positions(string) == expected_positions
