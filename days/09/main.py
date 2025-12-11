"""Day 9: Movie Theater

https://adventofcode.com/2025/day/9
"""

import itertools
import sys
from typing import Generator, Iterable, TypeAlias


Tile: TypeAlias = tuple[int, int]


def parse_tile(string: str) -> Tile:
    """Parse a tile."""
    return tuple(map(int, string.strip().split(",")))


def compute_pairwise_area(
    tiles: Iterable[Tile],
) -> Generator[tuple[Tile, Tile, int], None, None]:
    """Compute the area of each pair of tiles."""
    pairs = itertools.combinations(tiles, 2)
    for from_tile, to_tile in pairs:
        area = (abs(to_tile[0] - from_tile[0]) + 1) * (
            abs(to_tile[1] - from_tile[1]) + 1
        )
        yield from_tile, to_tile, area


if __name__ == "__main__":
    main()
