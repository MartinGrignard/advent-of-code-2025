"""Day 9: Movie Theater

https://adventofcode.com/2025/day/9
"""

from typing import TypeAlias


Tile: TypeAlias = tuple[int, int]


def parse_tile(string: str) -> Tile:
    """Parse a tile."""
    return tuple(map(int, string.strip().split(",")))


def main() -> None: ...


if __name__ == "__main__":
    main()
