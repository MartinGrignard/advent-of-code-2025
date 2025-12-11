"""Day 8: Playground

https://adventofcode.com/2025/day/8
"""

import pytest
from main import (
    Circuit,
    PositionsPair,
    compute_distance,
    compute_pairwise_distances,
    join_boxes,
    parse_position,
    Position,
)


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


def test_compute_pairwise_distances() -> None:
    positions = [
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
    ]
    assert compute_pairwise_distances(positions) == [
        (((0, 0, 0), (1, 0, 0)), 1),
        (((0, 0, 0), (0, 1, 0)), 1),
        (((0, 1, 0), (1, 0, 0)), 2),
    ]


@pytest.mark.parametrize(
    ("circuits", "boxes", "expected_circuits", "expected_answer"),
    [
        ([], ((0, 0, 0), (1, 0, 0)), [{(0, 0, 0), (1, 0, 0)}], True),
        (
            [{(0, 0, 0), (1, 0, 0), (0, 1, 0)}],
            ((0, 0, 0), (1, 0, 0)),
            [{(0, 0, 0), (1, 0, 0), (0, 1, 0)}],
            False,
        ),
        (
            [{(0, 0, 0), (0, 1, 0)}],
            ((0, 0, 0), (1, 0, 0)),
            [{(0, 0, 0), (0, 1, 0), (1, 0, 0)}],
            True,
        ),
        (
            [{(0, 1, 0), (0, 0, 1)}],
            ((0, 0, 0), (1, 0, 0)),
            [{(0, 1, 0), (0, 0, 1)}, {(0, 0, 0), (1, 0, 0)}],
            True,
        ),
    ],
    ids=[
        "no_circuit",
        "existing_circuit",
        "joint_circuit",
        "disjoint_circuit",
    ],
)
def test_join_boxes(
    circuits: list[Circuit],
    boxes: PositionsPair,
    expected_circuits: list[Circuit],
    expected_answer,
) -> None:
    assert join_boxes(circuits, boxes) == expected_answer
    assert circuits == expected_circuits
