"""Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

from typing import Iterable

import pytest

from main import get_bank_joltage, parse_joltages


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
    ("bank", "expected_joltage"),
    [
        (parse_joltages("987654321111111"), 98),
        (parse_joltages("811111111111119"), 89),
        (parse_joltages("234234234234278"), 78),
        (parse_joltages("818181911112111"), 92),
        (parse_joltages("818981911112111"), 99),
    ],
)
def test_get_bank_joltage(bank: Iterable[int], expected_joltage: int) -> None:
    assert get_bank_joltage(bank) == expected_joltage
