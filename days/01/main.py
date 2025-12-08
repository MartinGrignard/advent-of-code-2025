"""Day 1: Secret Entrance

https://adventofcode.com/2025/day/1
"""


def parse_clicks(string: str) -> int:
    """Parse a string describing a rotation."""
    return (-1 + 2 * int(string[0] == "R")) * int(string[1:])


def main() -> None: ...


if __name__ == "__main__":
    main()
