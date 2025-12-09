"""Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

EMPTY_SPACE = "."


def parse_positions(string: str) -> set[int]:
    """Extract the positions of non-empty items from a diagram row."""
    return {
        position
        for position, character in enumerate(string)
        if character != EMPTY_SPACE
    }


def main() -> None: ...


if __name__ == "__main__":
    main()
