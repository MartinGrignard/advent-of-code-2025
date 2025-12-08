"""Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

from typing import Iterable

import pytest

from main import Index, parse_joltages


@pytest.mark.parametrize(
    ("string", "expected_joltages"),
    [
        ("1", [1]),
        ("12345", [1, 2, 3, 4, 5]),
    ],
)
def test_parse_joltages(string: str, expected_joltages: Iterable[int]) -> None:
    assert list(parse_joltages(string)) == list(expected_joltages)


@pytest.mark.parametrize(
    ("joltages", "expected_index"),
    [
        ([1], {1: [0]}),
        ([1, 2, 3], {1: [0], 2: [1], 3: [2]}),
        ([1, 2, 2], {1: [0], 2: [1, 2]}),
    ],
)
def test_index_init(
    joltages: Iterable[int], expected_index: dict[int, list[int]]
) -> None:
    assert Index(joltages).to_dict() == expected_index
