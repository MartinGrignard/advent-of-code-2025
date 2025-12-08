"""Day 4: Printing Department

https://adventofcode.com/2025/day/4
"""

from io import StringIO
from typing import TextIO

import numpy as np
import pytest

from main import parse_diagram


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
