"""Day 8: Playground

https://adventofcode.com/2025/day/8
"""

import itertools
from math import prod
import sys
from typing import Iterable, TypeAlias


Position: TypeAlias = tuple[int, int, int]
PositionsPair: TypeAlias = tuple[Position, Position]
Circuit: TypeAlias = set[Position]


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


def join_boxes(circuits: list[Circuit], boxes: PositionsPair) -> bool:
    """Add boxes to the circuits and returns if it results in an update."""
    new_circuit = set(boxes)
    for circuit_id, circuit in enumerate(circuits):
        intersection = circuit & new_circuit
        if len(intersection) == 2:
            return False
        if len(intersection) == 1:
            circuits[circuit_id] = circuit | new_circuit
            return True
    circuits.append(new_circuit)
    return True


def join_n_closest_boxes(
    sorted_junctions: Iterable[PositionsPair], n: int
) -> list[Circuit]:
    """Create circuits using the n first closest pairs of boxes."""
    n_junctions = 0
    circuits: list[Circuit] = []
    junctions = iter(sorted_junctions)
    while n_junctions < n:
        if join_boxes(circuits, next(junctions)):
            n_junctions += 1
            continue
    return circuits


def main() -> None:
    from pprint import pprint as print
    positions = [parse_position(string) for string in sys.stdin]
    distances = sorted(
        compute_pairwise_distances(positions),
        key=lambda junction_distance: junction_distance[1],
    )
    n_junctions = 10 if len(positions) == 20 else 1000
    circuits = sorted(
        join_n_closest_boxes((junction for junction, _ in distances), n_junctions),
        key=lambda circuit: len(circuit),
        reverse=True,
    )
    print(list((len(circuit), circuit) for circuit in circuits[:3]))
    print(prod(len(circuit) for circuit in circuits[:3]))


if __name__ == "__main__":
    main()
