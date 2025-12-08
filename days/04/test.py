"""Day 4: Printing Department

https://adventofcode.com/2025/day/4
"""

from io import StringIO
from typing import TextIO

import numpy as np
import pytest

from main import (
    count_accessible_scrolls,
    count_removable_scrolls,
    parse_diagram,
    remove_accessible_scrolls,
)


@pytest.mark.parametrize(
    ("diagram", "expected_array"),
    [
        (StringIO("..\n.."), np.array([[False, False], [False, False]])),
        (StringIO("@@\n@@"), np.array([[True, True], [True, True]])),
        (StringIO("@.\n.@"), np.array([[True, False], [False, True]])),
    ],
)
def test_parse_diagram(diagram: TextIO, expected_array: np.ndarray) -> None:
    assert np.all(parse_diagram(diagram) == expected_array)


@pytest.mark.parametrize(
    ("diagram", "threshold", "expected_count"),
    [
        (np.array([[False, False], [False, False]]), 4, 0),
        (np.array([[True, True], [True, True]]), 2, 0),
        (np.array([[True, False], [False, True]]), 4, 2),
    ],
)
def test_count_accessible_scrolls(
    diagram: np.ndarray, threshold: int, expected_count: int
) -> None:
    assert count_accessible_scrolls(diagram, threshold) == expected_count


@pytest.mark.parametrize(
    ("diagram", "threshold", "expected_diagram"),
    [
        (
            np.array([[False, False], [False, False]]),
            4,
            np.array([[False, False], [False, False]]),
        ),
        (
            np.array([[True, True], [True, True]]),
            2,
            np.array([[True, True], [True, True]]),
        ),
        (
            np.array([[True, False], [False, True]]),
            2,
            np.array([[False, False], [False, False]]),
        ),
    ],
)
def test_remove_accessible_scrolls(
    diagram: np.ndarray, threshold: int, expected_diagram: np.ndarray
) -> None:
    assert np.all(remove_accessible_scrolls(diagram, threshold) == expected_diagram)


@pytest.mark.parametrize(
    ("diagram", "threshold", "expected_count"),
    [
        (np.eye(2, dtype=bool), 1, 0),
        (np.eye(2, dtype=bool), 2, 2),
        (np.eye(3, dtype=bool), 2, 3),
    ],
)
def test_count_removable_scrolls(
    diagram: np.ndarray, threshold: int, expected_count: int
) -> None:
    assert count_removable_scrolls(diagram, threshold) == expected_count
