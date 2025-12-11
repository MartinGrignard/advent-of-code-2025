"""Day 9: Movie Theater

https://adventofcode.com/2025/day/9
"""

import itertools
import sys
from typing import Generator, Iterable, TypeAlias


Tile: TypeAlias = tuple[int, int]
Loop: TypeAlias = list[Tile]


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


def create_loop(tiles: Iterable[Tile]) -> Loop:
    """Create a loop with only non-aligned segments."""

    def are_aligned(tiles: list[Tile]) -> bool:
        """Check whether three points for a line."""
        for axis in range(len(tiles[0])):
            coordinates = [tile[axis] for tile in tiles]
            if (
                sum(
                    abs(to_coord - from_coord)
                    for from_coord, to_coord in itertools.pairwise(coordinates)
                )
                == 0
            ):
                return True
        return False

    tiles = iter(tiles)
    first_tile = next(tiles)
    loop: Loop = [first_tile, next(tiles)]
    for tile in itertools.chain(tiles, [first_tile]):
        if are_aligned(loop[-2:] + [tile]):
            loop[-1] = tile
        else:
            loop.append(tile)
    return loop[:-1]


def main() -> None:
    tiles = itertools.tee((parse_tile(string) for string in sys.stdin), 2)
    tiles_and_areas = compute_pairwise_area(tiles[0])
    print(max(area for _from, _to, area in tiles_and_areas))
    loop = create_loop(tiles[1])


if __name__ == "__main__":
    main()
