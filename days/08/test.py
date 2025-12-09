"""Day 8: Playground

https://adventofcode.com/2025/day/8
"""

import pytest
from main import compute_distance, parse_position, Position


@pytest.mark.parametrize(
    ("string", "expected_position"),
    [
        ("1,2,3", (1, 2, 3)),
        ("12,34,56", (12, 34, 56)),
    ],
)
def test_parse_position(string: str, expected_position: Position) -> None:
    assert parse_position(string) == expected_position


@pytest.mark.parametrize(
    ("between_positions", "expected_distance"),
    [
        (((0, 0, 0), (1, 0, 0)), 1),
        (((0, 0, 0), (0, 1, 0)), 1),
        (((0, 0, 0), (0, 0, 1)), 1),
    ],
)
def test_compute_distance(
    between_positions: tuple[Position, Position], expected_distance: float
) -> None:
    assert compute_distance(*between_positions) == expected_distance
