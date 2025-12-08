"""Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

from typing import Generator


def parse_joltages(string: str) -> Generator[int, None, None]:
    """Convert a string into its integer joltages."""
    return (int(joltage) for joltage in string)


def main() -> None: ...


if __name__ == "__main__":
    main()
