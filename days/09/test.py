"""Day 9: Movie Theater

https://adventofcode.com/2025/day/9
"""

import pytest

from main import compute_pairwise_area, parse_tile, Tile


@pytest.mark.parametrize(
    ("string", "expected_tile"),
    [
        ("7,1", (7, 1)),
        ("11,1", (11, 1)),
    ],
)
def test_parse_tile(string: str, expected_tile: Tile) -> None:
    assert parse_tile(string) == expected_tile


def test_compute_pairwise_area() -> None:
    tiles: list[Tile] = [
        (0, 0),
        (1, 0),
        (0, 1),
    ]
    expected_areas = [
        ((0, 0), (1, 0), 2),
        ((0, 0), (0, 1), 2),
        ((1, 0), (0, 1), 4),
    ]
    areas = list(compute_pairwise_area(iter(tiles)))
    print(areas)
    assert areas == expected_areas
