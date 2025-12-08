"""Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""

import re
from typing import Literal, TextIO, TypeAlias


Problem: TypeAlias = tuple[Literal["+", "*"], tuple[int, ...]]


REPLACE_SPACES_PATTERN = re.compile(r"\s+")


def parse_problems(strings: TextIO) -> list[Problem]:
    """Parse problems from a text."""
    rows = [
        re.sub(REPLACE_SPACES_PATTERN, " ", string).strip().split(" ")
        for string in strings
    ]
    values = zip(*[[int(number) for number in row] for row in rows[:-1]])
    return list(zip(rows[-1], values))


def main() -> None: ...


if __name__ == "__main__":
    main()
