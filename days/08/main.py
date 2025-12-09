"""Day 8: Playground

https://adventofcode.com/2025/day/8
"""

import sys
from typing import TypeAlias


Position: TypeAlias = tuple[int, int, int]


def parse_position(string: str) -> Position:
    """Parse a single position from a string."""
    return tuple(int(coordinate) for coordinate in string.split(","))


def compute_distance(from_position: Position, to_position: Position) -> float:
    """Compute the Euclidean distance between two points."""
    return sum(
        [
            (to_coord - from_coord) ** 2
            for from_coord, to_coord in zip(from_position, to_position)
        ]
    )


def main() -> None:
    positions = [parse_position(string) for string in sys.stdin]


if __name__ == "__main__":
    main()
