"""Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

from typing import TextIO, TypeAlias


Positions: TypeAlias = set[int]


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


def split_beams(beam_positions: Positions, splitter_positions: Positions) -> Positions:
    """Let the beams pass through a set of splitters."""
    to_be_splitted_beam_positions = beam_positions & splitter_positions
    non_splitted_beam_positions = beam_positions - to_be_splitted_beam_positions
    splitted_beam_positions = set()
    for position in to_be_splitted_beam_positions:
        splitted_beam_positions.update({position - 1, position + 1})
    return non_splitted_beam_positions | splitted_beam_positions


def main() -> None: ...


if __name__ == "__main__":
    main()
