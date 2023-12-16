from __future__ import annotations
import numpy as np

with open("input2.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])
platform = np.zeros((line_count, col_count), dtype="U1")
stopper_offset = np.zeros(col_count, dtype=int)


def parse():
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            platform[y, x] = char


def tilt_north():
    stopper_offset.fill(0)  # reset
    for y, line in enumerate(platform):
        for x, char in enumerate(line):
            if char == "#":
                stopper_offset[x] = y + 1
            elif char == "O":
                platform[y, x] = "."
                platform[stopper_offset[x], x] = "O"
                stopper_offset[x] += 1


# detect repeated cycle pattern and apply modulo
def cycle(count: int):
    global platform
    for i in range(count):
        # Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east.
        for _ in range(4):
            tilt_north()
            platform = np.rot90(platform, k=-1)


def compute_weight() -> int:
    weight = 0
    for y, line in enumerate(platform):
        for char in line:
            if char == "O":
                weight += y
    return weight


def print_platform():
    for line in platform:
        print("".join(line))


parse()
cycle(3)
print_platform()
weight = compute_weight()
print(weight)
