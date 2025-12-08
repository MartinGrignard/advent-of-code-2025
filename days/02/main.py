"""Day 2: Gift Shop

https://adventofcode.com/2025/day/2
"""

from dataclasses import dataclass
from typing import Self


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


def main() -> None: ...


if __name__ == "__main__":
    main()
