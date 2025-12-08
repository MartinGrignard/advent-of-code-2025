"""Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

import sys
from typing import Generator, Iterable


def parse_joltages(string: str) -> Generator[int, None, None]:
    """Convert a string into its integer joltages."""
    return (int(joltage) for joltage in string.strip())


def get_bank_joltage(joltages: Iterable[int]) -> int:
    """Get the joltage of a bank."""
    joltages = list(joltages)
    highest = joltages[-2:]
    for joltage in reversed(joltages[:-2]):
        if joltage > highest[0]:
            highest = joltage, max(highest)
    return 10 * highest[0] + highest[1]


def main() -> None: ...


if __name__ == "__main__":
    main()
