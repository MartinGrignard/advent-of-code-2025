"""Day 3: Lobby

https://adventofcode.com/2025/day/3
"""

import itertools
import sys
from typing import Generator, Iterable


def parse_joltages(string: str) -> Generator[int, None, None]:
    """Convert a string into its integer joltages."""
    return (int(joltage) for joltage in string.strip())


def update_sequence(new_value: int, current_sequence: list[int]) -> list[int]:
    """Return the highest sequence possible with a new value."""
    if len(current_sequence) == 2:
        if new_value >= current_sequence[0]:
            return [new_value, max(current_sequence)]
    if new_value >= current_sequence[0]:
        return [new_value] + update_sequence(current_sequence[0], current_sequence[1:])
    return current_sequence


def sequence_to_joltage(sequence: Iterable[int]) -> int:
    return int("".join(str(digit) for digit in sequence))


def get_bank_joltage(joltages: Iterable[int], size: int) -> int:
    """Get the joltage of a bank."""
    joltages = list(joltages)
    highest = joltages[-size:]
    for joltage in reversed(joltages[:-size]):
        highest = update_sequence(joltage, highest)
    return sequence_to_joltage(highest)


def sum_banks_joltages(banks: Iterable[Iterable[int]], size: int) -> int:
    """Sum the joltage of a series of banks."""
    return sum(get_bank_joltage(bank, size) for bank in banks)


def main() -> None:
    banks = itertools.tee((list(parse_joltages(string)) for string in sys.stdin), 2)
    print(sum_banks_joltages(banks[0], 2))
    print(sum_banks_joltages(banks[1], 12))


if __name__ == "__main__":
    main()
