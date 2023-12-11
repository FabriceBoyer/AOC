from __future__ import annotations
from dataclasses import dataclass
import sys

with open("input.txt", encoding="utf-8") as f:
    data = f.readlines()


@dataclass
class Galaxy:
    x: int
    y: int


y = 0
galaxies: list[Galaxy] = []
for line in data:
    empty_line = True
    for x, char in enumerate(line):
        if char == "#":
            empty_line = False
            galaxies.append(Galaxy(x, y))
    y += 2 if empty_line else 1  # expansion

sum = 0
count = len(galaxies)
for i1, g1 in enumerate(galaxies[:-1]):
    shortest_dist = sys.maxsize
    i2 = i1 + 1
    for g2 in galaxies[i2:]:
        dist = abs(g2.x - g1.x) + abs(g2.y - g1.y)
        shortest_dist = min(dist, shortest_dist)
    sum += shortest_dist
print(sum)
