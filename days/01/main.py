"""Day 1: Secret Entrance

https://adventofcode.com/2025/day/1
"""

from dataclasses import dataclass
import itertools
import sys
from typing import Callable, Iterable, Self


@dataclass
class Rotation:
    """A rotation of the dial."""
    clicks: int
    clicks_per_turn: int
    start: int

    @property
    def clicks_in_last_turn(self: Self) -> int:
        """The number of clicks remaining after full turns."""
        if self.clicks == 0:
            return 0
        return (self.clicks // abs(self.clicks)) * (abs(self.clicks) % self.clicks_per_turn)
    
    @property
    def full_turns_count(self: Self) -> int:
        """The number of full turns."""
        return abs(self.clicks) // self.clicks_per_turn

    @property
    def end(self: Self) -> int:
        """The end position of the rotation."""
        return (
            self.clicks_per_turn + self.start + self.clicks_in_last_turn
        ) % self.clicks_per_turn
    
    def passes_by_in_last_turn(self: Self, position: int) -> bool:
        """Check whether the rotation passes by a position during the last turn."""
        if self.end == position:
            return False
        distance = position - self.start
        if distance < 0 and self.clicks_in_last_turn > 0:
            distance = (position + self.clicks_per_turn) - self.start
        elif distance > 0 and self.clicks_in_last_turn < 0:
            distance = (position - self.clicks_per_turn) - self.start
        return abs(distance) < abs(self.clicks_in_last_turn)


class Dial:
    """A circular dial."""

    def __init__(self: Self, size: int, position: int) -> None:
        self._size = size
        self._position = position

    @property
    def size(self: Self) -> int:
        return self._size

    @property
    def position(self: Self) -> int:
        return self._position

    def rotate(self: Self, clicks: int) -> Rotation:
        """Rotate the dial."""
        rotation = Rotation(clicks, self.size, self.position)
        self._position = rotation.end
        return rotation


def parse_clicks(string: str) -> int:
    """Parse a string describing a rotation."""
    return (-1 + 2 * int(string[0] == "R")) * int(string[1:])


def follow_instructions(
    dial: Dial, instructions: Iterable[int], callback: Callable[[Rotation], None]
) -> None:
    """Apply a series of rotations to the dial."""
    for clicks in instructions:
        rotation = dial.rotate(clicks)
        callback(rotation)


def count_ends_on(position: int, dial: Dial, instructions: Iterable[int]) -> int:
    """Count the number of times the dial ends on a given position."""
    count = 0

    def callback(rotation: Rotation) -> None:
        nonlocal count
        count += rotation.end == position

    follow_instructions(dial, instructions, callback)
    return count


def count_passes_by(position: int, dial: Dial, instructions: Iterable[int]) -> int:
    """Count the number of times the dial passes by a given position."""
    count = 0

    def callback(rotation: Rotation) -> None:
        nonlocal count
        count += rotation.full_turns_count
        count += rotation.passes_by_in_last_turn(position)
    
    follow_instructions(dial, instructions, callback)
    return count


def main() -> None:
    instructions = itertools.tee((parse_clicks(string) for string in sys.stdin), 2)
    print(count_ends_on(0, Dial(100, 50), instructions[0]))
    print(count_passes_by(0, Dial(100, 50), instructions[1]))


if __name__ == "__main__":
    main()
