"""Day 5: Cafeteria

https://adventofcode.com/2025/day/5
"""

from dataclasses import dataclass
from typing import Self


@dataclass
class Range:
    """A range of ingredient IDs."""

    lower: int
    upper: int

    @property
    def bounds(self: Self) -> tuple[int, int]:
        """The bounds of the range."""
        return self.lower, self.upper

    @classmethod
    def from_string(cls: type[Self], string: str) -> Self:
        return cls(*[int(number) for number in string.split("-")])


def main() -> None: ...


if __name__ == "__main__":
    main()
