"""Day 7: Laboratories

https://adventofcode.com/2025/day/7
"""

import itertools
import sys
from typing import Callable, Self, TextIO, TypeAlias


Positions: TypeAlias = set[int]
Diagram: TypeAlias = tuple[int, list[Positions]]


EMPTY_SPACE = "."


class Tree:
    def __init__(self: Self, children: list[Self] | None = None) -> None:
        self.children = children or []


def parse_positions(string: str) -> Positions:
    """Extract the positions of non-empty items from a diagram row."""
    return {
        position
        for position, character in enumerate(string)
        if character != EMPTY_SPACE
    }


def parse_tree(strings: TextIO) -> Tree:
    beam_position = parse_positions(next(strings).strip()).pop()
    depth = 0
    root = Tree()
    current_level = {beam_position: root}
    for string in strings:
        depth += 1
        splitter_positions = parse_positions(string)
        beam_positions = set(current_level.keys())
        splitted_beam_positions = beam_positions & splitter_positions
        non_splitted_beam_positions = beam_positions - splitted_beam_positions
        next_level = {}
        for position in non_splitted_beam_positions:
            next_level[position] = current_level[position]
        for current_position, next_position in itertools.chain(
            *[
                ((position, position - 1), (position, position + 1))
                for position in splitted_beam_positions
            ]
        ):
            if next_position not in next_level:
                next_level[next_position] = Tree()
            current_level[current_position].children.append(next_level[next_position])
        current_level = next_level
    return root


def dfs(tree: Tree, callback: Callable[[Tree], bool]) -> None:
    """Traverse a tree."""
    if not callback(tree):
        return
    for node in tree.children:
        dfs(node, callback)


def count_beam_splits(tree: Tree) -> int:
    """Count the number of beam splits."""
    count = 0
    visited_nodes: set[Tree] = set()

    def callback(node: Tree) -> bool:
        nonlocal count
        if node in visited_nodes:
            return False
        if len(node.children) > 1:
            count += 1
        visited_nodes.add(node)
        return True

    dfs(tree, callback)
    return count


def count_timelines(tree: Tree) -> int:
    """Count the possible timelines."""
    visited_nodes: dict[Tree, int] = {}

    def inner(node: Tree) -> int:
        if not node.children:
            return 0
        if node in visited_nodes:
            return visited_nodes[node]
        timelines_count = len(node.children) - 1
        for child in node.children:
            timelines_count += inner(child)
        visited_nodes[node] = timelines_count
        return timelines_count
    
    return 1 + inner(tree)


def main() -> None:
    tree = parse_tree(sys.stdin)
    print(count_beam_splits(tree))
    print(count_timelines(tree))


if __name__ == "__main__":
    main()
