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

    def __eq__(self: Self, other: Self) -> bool:
        """Check whether two ranges are equal."""
        return self.bounds == other.bounds

    def __len__(self: Self) -> int:
        """The number of IDs lying within the range."""
        return self.upper - self.lower + 1

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

    def __len__(self: Self) -> int:
        return sum(len(id_range) for id_range in self.ranges)


def collapse_ranges(ranges: Iterable[Range]) -> list[Range]:
    """Collapse a series of ranges."""
    ranges = sorted(ranges, key=lambda id_range: id_range.bounds)
    collapsed_ranges: list[Range] = [ranges[0]]
    for current_range in ranges[1:]:
        last_range = collapsed_ranges[-1]
        if current_range.lower in last_range:
            collapsed_ranges[-1] = Range(
                min(last_range.lower, current_range.lower),
                max(last_range.upper, current_range.upper),
            )
        else:
            collapsed_ranges.append(current_range)
    return collapsed_ranges


def count_fresh_ingredients(ranges: Ranges, ingredients: Iterable[int]) -> int:
    """Count fresh ingredients."""
    count = 0
    for ingredient in ingredients:
        if ingredient in ranges:
            count += 1
    return count


def count_possibly_fresh_ingredients(ranges: Ranges) -> int:
    """Count the number of ingredients that are potentially fresh."""
    return len(ranges)


def main() -> None:
    ranges = []
    while string := next(sys.stdin).strip():
        ranges.append(Range.from_string(string))
    ranges = Ranges(collapse_ranges(ranges))

    ingredients = (int(string) for string in sys.stdin)
    print(count_fresh_ingredients(ranges, ingredients))
    print(count_possibly_fresh_ingredients(ranges))


if __name__ == "__main__":
    main()
