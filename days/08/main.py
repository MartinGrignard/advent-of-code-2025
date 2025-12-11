"""Day 8: Playground

https://adventofcode.com/2025/day/8
"""

import itertools
import sys
from typing import Iterable, TypeAlias


Position: TypeAlias = tuple[int, int, int]
PositionsPair: TypeAlias = tuple[Position, Position]


def parse_position(string: str) -> Position:
    """Parse a single position from a string."""
    return tuple(int(coordinate) for coordinate in string.split(","))


def compute_distance(from_position: Position, to_position: Position) -> float:
    """Compute the squarred Euclidean distance between two points."""
    return sum(
        [
            (to_coord - from_coord) ** 2
            for from_coord, to_coord in zip(from_position, to_position)
        ]
    )


def compute_pairwise_distances(
    positions: Iterable[Position],
) -> list[tuple[PositionsPair, float]]:
    """Compute the pairwise distances between a series of positions."""
    distances: list[tuple[PositionsPair, float]] = []
    for from_position, to_position in itertools.combinations(positions, 2):
        from_position, to_position = (
            min(from_position, to_position),
            max(from_position, to_position),
        )
        distances.append(
            ((from_position, to_position), compute_distance(from_position, to_position))
        )
    return distances


def main() -> None:
    positions = [parse_position(string) for string in sys.stdin]
    distances = sorted(compute_pairwise_distances(positions), key=lambda it: it[1])


if __name__ == "__main__":
    main()
