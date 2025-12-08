"""Day 1: Secret Entrance

https://adventofcode.com/2025/day/1
"""

from typing import Self


class Dial:
    """A circular dial."""

    def __init__(self: Self, size: int, position: int) -> None:
        self._size = size
        self._position = position

    @property
    def size(self: Self) -> int:
        return self._size

    @property
    def position(self: Self) -> int:
        return self._position

    def rotate(self: Self, clicks: int) -> None:
        """Rotate the dial."""
        rotation = clicks % self.size
        self._position = (self.size + self._position + rotation) % self.size


def parse_clicks(string: str) -> int:
    """Parse a string describing a rotation."""
    return (-1 + 2 * int(string[0] == "R")) * int(string[1:])


def main() -> None: ...


if __name__ == "__main__":
    main()
