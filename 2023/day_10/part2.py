from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


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
for y, line in enumerate(data):
    for x, char in enumerate(line):
        grid[x, y] = Position(x, y, char, 0, [])


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
start: Optional[Position] = None
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
        if pos.kind == "S":
            start = grid[x, y]

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

    # compute polygon
    previous: Position = start
    current: Position = start
    coords: list[tuple[int, int]] = []

    while current != start or len(coords) == 0:
        coords.append((current.x, current.y))
        new_one = next(
            (p for p in current.connected if p != previous),
        )
        previous = current
        current = new_one

    # compute enclosed
    polygon: Polygon = Polygon(coords)
    enclosed: int = 0
    for y in range(line_count):
        for x in range(col_count):
            pos = grid[x, y]
            pt = Point(pos.x, pos.y)
            if polygon.contains_properly(pt):
                enclosed += 1
    print(enclosed)
