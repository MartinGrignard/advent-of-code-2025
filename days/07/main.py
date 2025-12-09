"""Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

import sys
from typing import TextIO, TypeAlias


Positions: TypeAlias = set[int]
Diagram: TypeAlias = tuple[int, list[Positions]]


EMPTY_SPACE = "."


def parse_positions(string: str) -> Positions:
    """Extract the positions of non-empty items from a diagram row."""
    return {
        position
        for position, character in enumerate(string)
        if character != EMPTY_SPACE
    }


def parse_diagram(strings: TextIO) -> tuple[int, list[Positions]]:
    """Parse a full diagram."""
    beam_position = parse_positions(next(strings).strip()).pop()
    splitter_positions = [parse_positions(string.strip()) for string in strings]
    return beam_position, splitter_positions


def split_beams_and_count_splits(
    beam_positions: Positions, splitter_positions: Positions
) -> tuple[Positions, int]:
    """Let the beams pass through a set of splitters."""
    to_be_splitted_beam_positions = beam_positions & splitter_positions
    non_splitted_beam_positions = beam_positions - to_be_splitted_beam_positions
    splitted_beam_positions = set()
    for position in to_be_splitted_beam_positions:
        splitted_beam_positions.update({position - 1, position + 1})
    return non_splitted_beam_positions | splitted_beam_positions, len(
        to_be_splitted_beam_positions
    )


def count_splits(diagram: Diagram) -> int:
    """Count the total number of splits."""
    count = 0
    beam_positions = {diagram[0]}
    splitter_positions = diagram[1]
    for row in splitter_positions:
        beam_positions, splits = split_beams_and_count_splits(beam_positions, row)
        count += splits
    return count


def main() -> None:
    diagram = parse_diagram(sys.stdin)
    print(count_splits(diagram))


if __name__ == "__main__":
    main()
