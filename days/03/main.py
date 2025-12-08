"""Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

from typing import Generator, Iterable, Self


class Index:
    """An index of the joltages."""

    def __init__(self: Self, joltages: Iterable[int]) -> None:
        self._index = [list() for _ in range(9)]
        for position, joltage in enumerate(joltages):
            self._index[joltage - 1].append(position)

    def to_dict(self: Self) -> dict[int, list[int]]:
        """Convert the index into a dictionary."""
        return {
            value + 1: positions
            for value, positions in enumerate(self._index)
            if positions
        }


def parse_joltages(string: str) -> Generator[int, None, None]:
    """Convert a string into its integer joltages."""
    return (int(joltage) for joltage in string)


def main() -> None: ...


if __name__ == "__main__":
    main()
