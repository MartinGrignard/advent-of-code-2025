"""Day 2: Gift Shop

https://adventofcode.com/2025/day/2
"""

from dataclasses import dataclass
import itertools
import re
from typing import Generator, Iterable, Self


REPEATING_TWICE_PATTERN = re.compile(r"^(\d+)\1$")
REPEATING_PATTERN = re.compile(r"^(\d+)\1+$")


@dataclass
class Range:
    """A product IDs range."""

    start: int
    end: int

    @property
    def ends(self: Self) -> tuple[int, int]:
        """The ends of the range."""
        return self.start, self.end

    @classmethod
    def from_string(cls: type[Self], string: str) -> Self:
        """Parse a range form a string."""
        return cls(*[int(part) for part in string.split("-")])

    def get_invalid_ids(
        self: Self, allow_more_than_twice: bool = False
    ) -> Generator[int, None, None]:
        """Extract the invalid product IDs of the range."""
        pattern = REPEATING_TWICE_PATTERN
        if allow_more_than_twice:
            pattern = REPEATING_PATTERN
        for product_id in range(self.start, self.end + 1):
            if pattern.match(str(product_id)) is not None:
                yield product_id


def sum_invalid_ids(
    ranges: Iterable[Range], allow_more_than_twice: bool = False
) -> int:
    """Sum all invalid product IDs from a set of ranges."""
    return sum(
        itertools.chain(
            *(id_range.get_invalid_ids(allow_more_than_twice) for id_range in ranges)
        )
    )


def main() -> None:
    ranges = itertools.tee(
        (Range.from_string(string) for string in input().split(",")), 2
    )
    print(sum_invalid_ids(ranges[0]))
    print(sum_invalid_ids(ranges[1], True))


if __name__ == "__main__":
    main()
