"""Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

from io import StringIO
import pytest

from main import parse_diagram, parse_positions, Positions, split_beams_and_count_splits


@pytest.mark.parametrize(
    ("string", "expected_positions"),
    [
        (".S.", {1}),
        (".^..^.", {1, 4}),
    ],
)
def test_parse_positions(string: str, expected_positions: Positions) -> None:
    assert parse_positions(string) == expected_positions
