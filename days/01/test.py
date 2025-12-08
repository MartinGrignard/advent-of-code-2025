"""Day 1: Secret Entrance

https://adventofcode.com/2025/day/1
"""

import pytest

from main import parse_clicks


@pytest.mark.parametrize(
    ("string", "expected_clicks"),
    [
        ("L1", -1),
        ("L10", -10),
        ("R1", 1),
        ("R10", 10),
    ],
)
def test_parse_clicks(string: str, expected_clicks: int) -> None:
    assert parse_clicks(string) == expected_clicks
