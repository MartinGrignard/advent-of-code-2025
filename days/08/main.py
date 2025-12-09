"""Day 8: Playground

https://adventofcode.com/2025/day/8
"""

from typing import TypeAlias


Position: TypeAlias = tuple[int, int, int]


def parse_position(string: str) -> Position:
    """Parse a single position from a string."""
    return tuple(int(coordinate) for coordinate in string.split(","))


def main() -> None: ...


if __name__ == "__main__":
    main()
