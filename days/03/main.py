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
        self._length = position

    def __len__(self: Self) -> int:
        """The length of the index."""
        return self._length

    def to_dict(self: Self) -> dict[int, list[int]]:
        """Convert the index into a dictionary."""
        return {
            value + 1: positions
            for value, positions in enumerate(self._index)
            if positions
        }

    def get_nth_highest(self: Self, nth: int) -> int:
        """Retrieve the n-th highest voltage."""
        before = 0
        for joltage in range(9, 0, -1):
            before += len(self._index[joltage - 1])
            if before > nth:
                return joltage

    def get_n_highest(self: Self, n: int) -> list[int]:
        """Retrieve the n highest voltages in order."""
        highests: list[tuple[int, int]] = []
        before = 0
        current = 0
        nth = 0
        for joltage in range(9, 0, -1):
            positions = self._index[joltage - 1]
            current = len(positions)
            while before + current > nth:
                index = len(highests) - before
                highests.append((positions[index], joltage))
                nth += 1
                if nth == n:
                    return [joltage for _, joltage in sorted(highests)]
            before += current
            current = 0


def parse_joltages(string: str) -> Generator[int, None, None]:
    """Convert a string into its integer joltages."""
    return (int(joltage) for joltage in string)


def main() -> None: ...


if __name__ == "__main__":
    main()
