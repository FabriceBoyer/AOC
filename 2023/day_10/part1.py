from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import numpy as np

with open("input.txt", encoding="utf-8") as f:
    data = f.read().splitlines()


@dataclass
class Position:
    x: int
    y: int
    kind: str
    distance: int
    connected: list[Position]


# parse
col_count = len(data[0])
line_count = len(data)
grid = np.empty((line_count, col_count), dtype=object)
start: Optional[Position] = None
for y, line in enumerate(data):
    for x, char in enumerate(line):
        grid[x, y] = Position(x, y, char, 0, [])
        if char == "S":
            start = grid[x, y]


def connect_north(_pos: Position):
    if _pos.y > 0:
        _pos.connected.append(grid[_pos.x, _pos.y - 1])


def connect_south(_pos: Position):
    if _pos.y < line_count - 1:
        _pos.connected.append(grid[_pos.x, _pos.y + 1])


def connect_east(_pos: Position):
    if _pos.x < col_count - 1:
        _pos.connected.append(grid[_pos.x + 1, _pos.y])


def connect_west(_pos: Position):
    if _pos.x > 0:
        _pos.connected.append(grid[_pos.x - 1, _pos.y])


# compute connections
for y in range(line_count):
    for x in range(col_count):
        pos = grid[x, y]
        # | is a vertical pipe connecting north and south.
        if pos.kind == "|":
            connect_north(pos)
            connect_south(pos)
        # - is a horizontal pipe connecting east and west.
        if pos.kind == "-":
            connect_east(pos)
            connect_west(pos)
        # L is a 90-degree bend connecting north and east.
        if pos.kind == "L":
            connect_north(pos)
            connect_east(pos)
        # J is a 90-degree bend connecting north and west.
        if pos.kind == "J":
            connect_north(pos)
            connect_west(pos)
        # 7 is a 90-degree bend connecting south and west.
        if pos.kind == "7":
            connect_south(pos)
            connect_west(pos)
        # F is a 90-degree bend connecting south and east.
        if pos.kind == "F":
            connect_south(pos)
            connect_east(pos)
        # . is ground; there is no pipe in this tile.
        # S is the starting position of the animal;
        # there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

if start:  # for type hint
    # compute start
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            pos = grid[start.x + x, start.y + y]
            if start in pos.connected:
                start.connected.append(pos)

    if not len(start.connected) == 2:
        raise ValueError("Shouldn't happen")

    # compute distances
    previous: list[Position] = [start]
    to_process: list[Position] = start.connected
    distance = 1
    while len(to_process) > 0:
        nexts = []
        for i, pos in enumerate(to_process):
            pos.distance = distance
            n = next(
                (p for p in pos.connected if p not in previous),
                None,
            )
            if n is not None and n.distance == 0:
                nexts.append(n)
        distance += 1
        previous = to_process
        to_process = nexts
    print(distance - 1)
