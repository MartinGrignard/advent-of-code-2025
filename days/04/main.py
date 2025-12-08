"""Day 4: Printing Department

https://adventofcode.com/2025/day/4
"""

from typing import TextIO

import numpy as np


def parse_diagram(diagram: TextIO) -> np.ndarray:
    """Convert a diagram into an array."""
    return np.array(
        [[character == "@" for character in row.strip()] for row in diagram]
    )


def main() -> None: ...


if __name__ == "__main__":
    main()
