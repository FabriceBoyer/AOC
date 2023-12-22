from __future__ import annotations
import numpy as np

with open("input2.txt", encoding="utf-8") as f:
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
step_limit = 100  # 26501365
for step in range(step_limit):
    new_positions: set[tuple[int, int]] = set()
    for pos in positions:
        y = pos[0]
        x = pos[1]
        new_pos_list: list[tuple[int, int]] = []
        new_pos_list.append(((y - 1), x))  # north
        new_pos_list.append((y, (x - 1)))  # west
        new_pos_list.append((y, (x + 1)))  # east
        new_pos_list.append(((y + 1), x))  # south
        for new_pos in new_pos_list:
            if garden[new_pos[0] % line_count, new_pos[1] % col_count] == 0:
                new_positions.add(new_pos)
    positions = new_positions

print(len(positions))
