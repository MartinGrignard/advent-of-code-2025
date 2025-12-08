"""Day 2: Gift Shop

https://adventofcode.com/2025/day/2
"""

from typing import Iterable
import pytest

from main import Range


@pytest.mark.parametrize(
    ("string", "expected_ends"),
    [
        ("1-10", (1, 10)),
        ("10-100", (10, 100)),
    ],
)
def test_range_from_string(string: str, expected_ends: tuple[int, int]) -> None:
    assert Range.from_string(string).ends == expected_ends


@pytest.mark.parametrize(
    ("range", "expected_invalid_ids"),
    [
        (Range(11, 22), [11, 22]),
        (Range(95, 115), [99]),
        (Range(998, 1012), [1010]),
        (Range(1188511880, 1188511890), [1188511885]),
    ],
)
def test_range_get_invalid_ids(
    range: Range, expected_invalid_ids: Iterable[int]
) -> None:
    assert list(range.get_invalid_ids()) == list(expected_invalid_ids)
