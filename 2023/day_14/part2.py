from __future__ import annotations
import numpy as np

with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])
platform = np.zeros((line_count, col_count), dtype="U1")
stopper_offset = np.zeros(col_count, dtype=int)
cycle_history: list[np.ndarray] = []


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


# -1 not found
def inList(searched_elem, elem_list) -> int:
    for i, elem in enumerate(elem_list):
        if np.array_equal(elem, searched_elem):
            return i
    return -1


def cycle(count: int):
    global platform
    for counter in range(count):
        # Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east.
        for _ in range(4):
            tilt_north()
            platform = np.rot90(
                platform, k=-1
            )  # rotate and tilt north to compute all directions
        i: int = inList(platform, cycle_history)
        if i >= 0:
            # detect repeated cycle pattern and apply modulo in range
            print(
                f"pattern found after {len(cycle_history)} cycles between cycle {counter} and {i}"
            )
            platform = cycle_history[i + (count - i - 1) % (counter - i)]
            return
        cycle_history.append(platform.copy())


def compute_weight() -> int:
    weight = 0
    for y, line in enumerate(platform):
        for char in line:
            if char == "O":
                weight += line_count - y
    return weight


def print_platform():
    for line in platform:
        print("".join(line))


parse()
cycle(int(1e9))
print_platform()
weight = compute_weight()
print(weight)
