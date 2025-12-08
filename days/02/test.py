"""Day 2: Gift Shop

https://adventofcode.com/2025/day/2
"""

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
