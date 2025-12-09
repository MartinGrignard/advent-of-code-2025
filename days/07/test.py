"""Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

from io import StringIO
import pytest

from main import parse_diagram, parse_positions, Positions, split_beams


@pytest.mark.parametrize(
    ("string", "expected_positions"),
    [
        (".S.", {1}),
        (".^..^.", {1, 4}),
    ],
)
def test_parse_positions(string: str, expected_positions: Positions) -> None:
    assert parse_positions(string) == expected_positions


def test_parse_diagram() -> None:
    strings = StringIO("..S..\n.....\n.^.^.\n")
    expected_diagram = (2, [set(), {1, 3}])
    assert parse_diagram(strings) == expected_diagram


@pytest.mark.parametrize(
    ("beam_positions", "splitter_positions", "expected_positions"),
    [
        ({1}, set(), {1}),
        ({1}, {1}, {0, 2}),
        ({1, 2}, {1}, {0, 2}),
    ],
)
def test_split_beams(
    beam_positions: Positions,
    splitter_positions: Positions,
    expected_positions: Positions,
) -> None:
    assert split_beams(beam_positions, splitter_positions) == expected_positions
