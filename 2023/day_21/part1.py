from __future__ import annotations
import numpy as np

with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])
garden = np.zeros((line_count, col_count), dtype="int")
positions: set[tuple[int, int]] = set()  # set filter duplicates

# parse
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        garden[y, x] = 1 if char == "#" else 0
        if char == "S":
            positions.add((y, x))

# compute
step_limit = 64
for step in range(step_limit):
    new_positions: set[tuple[int, int]] = set()
    for pos in positions:
        y = pos[0]
        x = pos[1]
        if y > 0 and garden[y - 1, x] == 0:
            new_positions.add((y - 1, x))
        if x > 0 and garden[y, x - 1] == 0:
            new_positions.add((y, x - 1))
        if y < line_count - 1 and garden[y + 1, x] == 0:
            new_positions.add((y + 1, x))
        if x < col_count - 1 and garden[y, x + 1] == 0:
            new_positions.add((y, x + 1))
    positions = new_positions

print(len(positions))
