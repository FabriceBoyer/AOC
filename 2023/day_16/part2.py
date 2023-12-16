from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
import numpy as np

with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])
platform = np.zeros((line_count, col_count), dtype="U1")


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


def go_north(beam_: Beam):
    append_beam(Beam(beam_.y - 1, beam_.x, Direction.North))


def go_south(beam_: Beam):
    append_beam(Beam(beam_.y + 1, beam_.x, Direction.South))


def go_east(beam_: Beam):
    append_beam(Beam(beam_.y, beam_.x + 1, Direction.East))


def go_west(beam_: Beam):
    append_beam(Beam(beam_.y, beam_.x - 1, Direction.West))


def get_energy_for_initial_beam(init_beam: Beam):
    energized = np.zeros((line_count, col_count), dtype="bool")
    current_beams_list.clear()  # reset
    past_beams_list.clear()  # reset

    append_beam(init_beam)
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
    return total_energy


max_energy: int = 0
for y in range(line_count):
    energy = get_energy_for_initial_beam(Beam(y, 0, Direction.East))
    max_energy = max(max_energy, energy)

    energy = get_energy_for_initial_beam(Beam(y, col_count - 1, Direction.West))
    max_energy = max(max_energy, energy)

    print(f"y={y}/{line_count}")

for x in range(col_count):
    energy = get_energy_for_initial_beam(Beam(0, x, Direction.South))
    max_energy = max(max_energy, energy)

    energy = get_energy_for_initial_beam(Beam(line_count - 1, x, Direction.North))
    max_energy = max(max_energy, energy)

    print(f"x={x}/{col_count}")

print(max_energy)
