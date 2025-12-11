"""Day 9: Movie Theater

https://adventofcode.com/2025/day/9
"""

import pytest

from main import parse_tile, Tile


@pytest.mark.parametrize(
    ("string", "expected_tile"),
    [
        ("7,1", (7, 1)),
        ("11,1", (11, 1)),
    ],
)
def test_parse_tile(string: str, expected_tile: Tile) -> None:
    assert parse_tile(string) == expected_tile
