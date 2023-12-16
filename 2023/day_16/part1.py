from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import numpy as np

with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])
platform = np.zeros((line_count, col_count), dtype="U1")
energized = np.zeros((line_count, col_count), dtype="bool")

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        platform[y, x] = char


# enum of cardinal directions
class Direction(Enum):
    North = 0
    South = 1
    East = 2
    West = 3


@dataclass
class Beam:
    y: int
    x: int
    direction: Direction


current_beams_list: list[Beam] = []
past_beams_list: list[Beam] = []


def append_beam(beam_: Beam):
    for b in past_beams_list:
        if b.x == beam_.x and b.y == beam_.y and b.direction == beam_.direction:
            return
    current_beams_list.append(beam_)
    past_beams_list.append(beam_)


append_beam(Beam(0, 0, Direction.East))  # initial beam


def go_north(beam_: Beam):
    append_beam(Beam(beam_.y - 1, beam_.x, Direction.North))


def go_south(beam_: Beam):
    append_beam(Beam(beam_.y + 1, beam_.x, Direction.South))


def go_east(beam_: Beam):
    append_beam(Beam(beam_.y, beam_.x + 1, Direction.East))


def go_west(beam_: Beam):
    append_beam(Beam(beam_.y, beam_.x - 1, Direction.West))


while len(current_beams_list) > 0:
    beam: Beam = current_beams_list.pop()

    # bound check
    if beam.x < 0 or beam.x > col_count - 1:
        continue
    if beam.y < 0 or beam.y > line_count - 1:
        continue

    pos = platform[beam.y, beam.x]
    energized[beam.y, beam.x] = True

    if beam.direction == Direction.East:
        if pos == "." or pos == "-":
            go_east(beam)
        elif pos == "\\":
            go_south(beam)
        elif pos == "/":
            go_north(beam)
        elif pos == "|":
            go_north(beam)
            go_south(beam)

    elif beam.direction == Direction.North:
        if pos == "." or pos == "|":
            go_north(beam)
        elif pos == "\\":
            go_west(beam)
        elif pos == "/":
            go_east(beam)
        elif pos == "-":
            go_west(beam)
            go_east(beam)

    elif beam.direction == Direction.South:
        if pos == "." or pos == "|":
            go_south(beam)
        elif pos == "\\":
            go_east(beam)
        elif pos == "/":
            go_west(beam)
        elif pos == "-":
            go_east(beam)
            go_west(beam)

    elif beam.direction == Direction.West:
        if pos == "." or pos == "-":
            go_west(beam)
        elif pos == "\\":
            go_north(beam)
        elif pos == "/":
            go_south(beam)
        elif pos == "|":
            go_north(beam)
            go_south(beam)

total_energy: int = 0
for e in np.nditer(energized):
    total_energy += 1 if e else 0
print(total_energy)
