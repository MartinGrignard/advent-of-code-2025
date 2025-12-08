"""Day 2: Gift Shop

https://adventofcode.com/2025/day/2
"""

from typing import Iterable
import pytest

from main import Range, sum_invalid_ids


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
    ("range", "allow_more_than_twice", "expected_invalid_ids"),
    [
        (Range(11, 22), False, [11, 22]),
        (Range(95, 115), False, [99]),
        (Range(998, 1012), False, [1010]),
        (Range(1188511880, 1188511890), False, [1188511885]),
        (Range(11, 22), True, [11, 22]),
        (Range(95, 115), True, [99, 111]),
        (Range(998, 1012), True, [999, 1010]),
        (Range(1188511880, 1188511890), True, [1188511885]),
    ],
)
def test_range_get_invalid_ids(
    range: Range, allow_more_than_twice: bool, expected_invalid_ids: Iterable[int]
) -> None:
    assert list(range.get_invalid_ids(allow_more_than_twice)) == list(expected_invalid_ids)


@pytest.mark.parametrize(
    ("ranges", "expected_sum"),
    [
        ([Range(0, 1)], 0),
        ([Range(11, 22)], 33),
        ([Range(0, 1), Range(11, 22)], 33),
    ],
)
def test_sum_invalid_ids(ranges: Iterable[Range], expected_sum: int) -> None:
    assert sum_invalid_ids(ranges) == expected_sum
