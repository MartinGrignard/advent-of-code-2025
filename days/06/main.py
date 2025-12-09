"""Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""

import operator
import re
import sys
from typing import Generator, Literal, TextIO, TypeAlias


Assessment: TypeAlias = tuple[str, ...]
Problem: TypeAlias = tuple[Literal["+", "*"], tuple[int, ...]]


REPLACE_SPACES_PATTERN = re.compile(r"\s+")


def split_assessments(strings: TextIO) -> Generator[Assessment, None, None]:
    """Extract each assessment."""
    assessment: list[str] = []
    for column in zip(*strings):
        if all(character == " " for character in column):
            yield tuple("".join(row) for row in zip(*assessment))
            assessment = []
            continue
        assessment.append(column)
    yield tuple("".join(row).replace("\n", "") for row in zip(*assessment))


def parse_problems(strings: TextIO) -> list[Problem]:
    """Parse problems from a text."""
    rows = [
        re.sub(REPLACE_SPACES_PATTERN, " ", string).strip().split(" ")
        for string in strings
    ]
    values = zip(*[[int(number) for number in row] for row in rows[:-1]])
    return list(zip(rows[-1], values))


def execute_problem(problem: Problem) -> int:
    """Execute a problem."""
    operation = {
        "+": operator.add,
        "*": operator.mul,
    }[problem[0]]
    values = problem[1]
    result = values[0]
    for value in values[1:]:
        result = operation(result, value)
    return result


def main() -> None:
    problems = parse_problems(sys.stdin)
    print(sum(execute_problem(problem) for problem in problems))


if __name__ == "__main__":
    main()
