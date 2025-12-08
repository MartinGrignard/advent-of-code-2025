"""Day 5: Cafeteria

https://adventofcode.com/2025/day/5
"""

from dataclasses import dataclass
import sys
from typing import Iterable, Self


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


def count_fresh_ingredients(ranges: Ranges, ingredients: Iterable[int]) -> int:
    """Count fresh ingredients."""
    count = 0
    for ingredient in ingredients:
        if ingredient in ranges:
            count += 1
    return count


def main() -> None:
    ranges = []
    while string := next(sys.stdin).strip():
        ranges.append(Range.from_string(string))
    ranges = Ranges(ranges)

    ingredients = (int(string) for string in sys.stdin)
    print(count_fresh_ingredients(ranges, ingredients))


if __name__ == "__main__":
    main()
