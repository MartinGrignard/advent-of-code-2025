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
    def __init__(self: Self, depth: int, position: int, children: list[Self] | None = None) -> None:
        self.depth, self.position = depth, position
        self.children = children or []
    
    def __repr__(self: Self) -> str:
        return f"Tree(depth={self.depth}, pos={self.position})"


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
    root = Tree(0, beam_position)
    current_level = {beam_position: root}
    for string in strings:
        depth += 1
        splitter_positions = parse_positions(string)
        beam_positions = set(current_level.keys())
        splitted_beam_positions = beam_positions & splitter_positions
        non_splitted_beam_positions = beam_positions - splitted_beam_positions
        next_level = {}
        for position in non_splitted_beam_positions:
            next_level[position] = Tree(depth, position)
            current_level[position].children.append(next_level[position])
        for current_position, next_position in itertools.chain(*[((position, position - 1), (position, position + 1)) for position in splitted_beam_positions]):
            if next_position not in next_level:
                next_level[next_position] = Tree(depth, next_position)
            current_level[current_position].children.append(next_level[next_position])
        current_level = next_level
    return root


def dfs(tree: Tree, callback: Callable[[Tree], bool]) -> None:
    """Traverse a tree."""
    nodes_to_traverse = [tree]
    while nodes_to_traverse:
        node = nodes_to_traverse.pop()
        if not callback(node):
            continue
        for child in node.children:
            nodes_to_traverse.append(child)


def count_beam_splits(tree: Tree) -> int:
    """Count the number of beam splits."""
    count = 0
    visited_nodes: set[tuple[int, int]] = set()

    def callback(node: Tree) -> bool:
        nonlocal count
        if (node.depth, node.position) in visited_nodes:
            return False
        if len(node.children) > 1:
            count += 1
        visited_nodes.add((node.depth, node.position))
        return True
    
    dfs(tree, callback)
    return count


def count_timelines(tree: Tree) -> int:
    """Count the possible timelines."""
    count = 1

    def callback(node: Tree) -> bool:
        nonlocal count
        if not node.children:
            return False
        count += len(node.children) - 1
        return True
    
    dfs(tree, callback)
    return count


def main() -> None:
    tree = parse_tree(sys.stdin)
    print(count_beam_splits(tree))
    print(count_timelines(tree))


if __name__ == "__main__":
    main()
