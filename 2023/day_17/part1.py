from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import numpy as np
import sys
import bisect


@dataclass
class Node:
    y: int
    x: int
    direction: int  # 0=north, 1=east, 2=south, 3=west
    straight_counter: int  # max 3
    total_heatloss: int
    path: list[tuple[int, int, int, int]]


min_heat: int = sys.maxsize  # for the nodes having reached target
min_node: Optional[Node] = None
best_heatloss_dict: dict[tuple[int, int, int, int], int] = {}


def move_node(old: Node, new_dir: int) -> None:
    global min_heat, min_node, nodes
    new = Node(
        old.y, old.x, new_dir, old.straight_counter, old.total_heatloss, old.path.copy()
    )

    # straight_counter
    if new_dir == old.direction:
        new.straight_counter += 1
    else:
        new.straight_counter = 1

    # move y,x
    if new_dir == 0:  # north
        new.y -= 1
    elif new_dir == 1:  # east
        new.x += 1
    elif new_dir == 2:  # south
        new.y += 1
    elif new_dir == 3:  # west
        new.x -= 1

    # bound check
    if new.y < 0 or new.y > line_count - 1 or new.x < 0 or new.x > col_count - 1:
        return

    # re-exploration check
    new_coord = (new.y, new.x, new.direction, new.straight_counter)
    # if new_coord in new.path:
    #     return
    new.path.append(new_coord)

    # heat check
    heatloss = int(city[new.y, new.x])
    new.total_heatloss += heatloss

    best_for_coord = best_heatloss_dict.get(new_coord, -1)
    if best_for_coord == -1 or best_for_coord > new.total_heatloss:
        best_heatloss_dict[new_coord] = new.total_heatloss
    else:
        return  # better path exist somewhere else

    if new.total_heatloss >= min_heat:
        return

    # target reached check
    if new.y == line_count - 1 and new.x == col_count - 1:
        if new.total_heatloss < min_heat:
            min_heat = new.total_heatloss
            min_node = new
            print(f"target reached with better total_heatloss of {min_heat}")
        return

    bisect.insort_left(nodes, new, key=lambda x: -x.total_heatloss)  # reverse


def print_node(node_: Optional[Node]):
    if node_ is None:
        return

    view = np.zeros((line_count, col_count), dtype="U1")
    for y in range(line_count):
        for x in range(col_count):
            view[y, x] = str(city[y, x])

    for n in node_.path:
        char: str = ""
        dir = n[2]
        if dir == 0:
            char = "^"
        elif dir == 1:
            char = ">"
        elif dir == 2:
            char = "v"
        elif dir == 3:
            char = "<"
        view[n[0], n[1]] = char

    for y in range(line_count):
        msg: str = ""
        for x in range(col_count):
            msg += view[y, x]

        print(msg)


with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])

city = np.zeros((line_count, col_count), dtype="int")

# parse
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        city[y, x] = int(char)

# init with top-left to right
nodes: list[Node] = [Node(0, 0, 1, 1, 0, [(0, 0, 1, 1)])]

start: datetime = datetime.now()
while len(nodes) > 0:
    node = nodes.pop()
    if node.straight_counter < 3:
        move_node(node, node.direction)  # straight

    move_node(node, (node.direction - 1) % 4)  # left
    move_node(node, (node.direction + 1) % 4)  # right

print(f"time spent: {datetime.now() - start}")
print_node(min_node)
print(min_heat)
