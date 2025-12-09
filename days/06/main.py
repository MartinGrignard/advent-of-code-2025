"""Day 6: Trash Compactor

https://adventofcode.com/2025/day/6
"""

import itertools
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


def parse_problem_horizontally(assessment: Assessment) -> Problem:
    """Parse problems from a text."""
    return assessment[-1].strip(), tuple(int(number) for number in assessment[:-1])


def parse_problem_vertically(assessment: Assessment) -> Problem:
    """Parse problems from a text."""
    rotated_numbers = ["".join(row) for row in zip(*assessment[:-1])]
    return assessment[-1].strip(), tuple(int(number) for number in rotated_numbers)


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
    assessments = itertools.tee(split_assessments(sys.stdin))
    for parser, assessments in zip(
        [parse_problem_horizontally, parse_problem_vertically],
        itertools.tee(split_assessments(sys.stdin)),
    ):
        print(sum(execute_problem(parser(assessment)) for assessment in assessments))


if __name__ == "__main__":
    main()
