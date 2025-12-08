"""Day 4: Printing Department

https://adventofcode.com/2025/day/4
"""

import sys
from typing import TextIO

import numpy as np
from scipy.signal import convolve2d


def parse_diagram(diagram: TextIO) -> np.ndarray:
    """Convert a diagram into an array."""
    return np.array(
        [[character == "@" for character in row.strip()] for row in diagram]
    )


def get_accessible_scrolls(diagram: np.ndarray, threshold: int) -> np.ndarray:
    """Get a map of the available scrolls."""
    kernel = np.array(
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
    )
    return np.bitwise_and(convolve2d(diagram, kernel, mode="same") < threshold, diagram)


def count_accessible_scrolls(diagram: np.ndarray, threshold: int) -> np.ndarray:
    """Count the scrolls with less than a specific amount of adjacent scrolls."""
    return np.count_nonzero(get_accessible_scrolls(diagram, threshold))


def remove_accessible_scrolls(diagram: np.ndarray, threshold: int) -> np.ndarray:
    """Remove the accessible scrolls."""
    accessible_scrolls = get_accessible_scrolls(diagram, threshold)
    return np.bitwise_xor(diagram, accessible_scrolls)


def count_removable_scrolls(diagram: np.ndarray, threshold: int) -> np.ndarray:
    """Count the scrolls that can be removed."""
    scrolls_count = np.count_nonzero(diagram)
    previous_diagram = diagram
    diagram = remove_accessible_scrolls(diagram, threshold)
    while np.any(previous_diagram != diagram):
        previous_diagram = diagram
        diagram = remove_accessible_scrolls(diagram, threshold)
    return scrolls_count - np.count_nonzero(diagram)


def main() -> None:
    diagram = parse_diagram(sys.stdin)
    print(count_accessible_scrolls(diagram, 4))


if __name__ == "__main__":
    main()
