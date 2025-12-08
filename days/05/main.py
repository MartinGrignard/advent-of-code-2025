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

    def __contains__(self: Self, value: int) -> bool:
        """Check if a value lies within the range."""
        return self.lower <= value <= self.upper

    @property
    def bounds(self: Self) -> tuple[int, int]:
        """The bounds of the range."""
        return self.lower, self.upper

    @classmethod
    def from_string(cls: type[Self], string: str) -> Self:
        """Parse a range from a string."""
        return cls(*[int(number) for number in string.split("-")])


@dataclass
class Ranges:
    """A set of ranges."""

    ranges: list[Range]

    def __contains__(self: Self, value: int) -> bool:
        """Checks if a value lies within a set of ranges."""
        for id_range in self.ranges:
            if value in id_range:
                return True
        return False


def main() -> None: ...


if __name__ == "__main__":
    main()
