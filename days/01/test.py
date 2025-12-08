"""Day 1: Secret Entrance

https://adventofcode.com/2025/day/1
"""

import pytest

from main import Dial, parse_clicks


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


@pytest.mark.parametrize(
    ("dial", "clicks", "expected_position"),
    [
        (Dial(2, 0), 0, 0),
        (Dial(2, 0), 1, 1),
        (Dial(2, 1), -1, 0),
        (Dial(2, 0), -1, 1),
        (Dial(2, 1), 1, 0),
        (Dial(2, 0), 3, 1),
    ],
)
def test_dial_rotate(dial: Dial, clicks: int, expected_position: int) -> None:
    dial.rotate(clicks)
    assert dial.position == expected_position
