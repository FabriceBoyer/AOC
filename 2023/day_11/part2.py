from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class Galaxy:
    orig_x: int
    x: int
    y: int


with open("input.txt", encoding="utf-8") as f:
    data = [line.strip() for line in f.readlines()]

factor: int = int(1e6)

# parse
y: int = 0
galaxies: list[Galaxy] = []
col_galaxy_count = np.zeros(len(data[0]))
for line in data:
    empty_line: bool = True
    for x, char in enumerate(line.strip()):
        if char == "#":
            col_galaxy_count[x] += 1
            empty_line = False
            galaxies.append(Galaxy(x, x, y))
    y += factor if empty_line else 1  # y expansion

# x expansion
for i, r in enumerate(col_galaxy_count):
    if r == 0:
        for g in galaxies:
            if g.orig_x > i:
                g.x += factor - 1

sum: int = 0
for i1, g1 in enumerate(galaxies):
    for g2 in galaxies[i1 + 1 :]:
        dist = abs(g2.x - g1.x) + abs(g2.y - g1.y)
        sum += dist
print(sum)
