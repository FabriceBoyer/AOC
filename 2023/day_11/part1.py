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
    y += 1
    if empty_line:
        y += 1  # expansion

sum = 0
count = len(galaxies)
for index1, g1 in enumerate(galaxies):
    if index1 == count - 2:
        break
    shortest_dist = sys.maxsize
    index2 = index1 + 1
    for g2 in galaxies[index2:]:
        dist = abs(g1.x - g2.x) + abs(g1.y - g2.y)
        shortest_dist = min(dist, shortest_dist)
    sum += shortest_dist
print(sum)
