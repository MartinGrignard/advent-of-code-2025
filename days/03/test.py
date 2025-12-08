"""Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

from typing import Iterable

import pytest

from main import parse_joltages


@pytest.mark.parametrize(
    ("string", "expected_joltages"),
    [
        ("1", [1]),
        ("12345", [1, 2, 3, 4, 5]),
    ],
)
def test_parse_joltages(string: str, expected_joltages: Iterable[int]) -> None:
    assert list(parse_joltages(string)) == list(expected_joltages)
