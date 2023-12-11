from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import numpy as np

with open("input2.txt", encoding="utf-8") as f:
    data = [line.strip() for line in f.readlines()]


@dataclass
class Galaxy:
    orig_x: int
    x: int
    y: int


y = 0
galaxies: list[Galaxy] = []
row_galaxy_count=np.zeros(len(data[0]))
for line in data:
    empty_line = True
    for x, char in enumerate(line.strip()):
        if char == "#":
            row_galaxy_count[x]+=1
            empty_line = False
            galaxies.append(Galaxy(x, x, y))
    y += 2 if empty_line else 1  # y expansion

# x expansion
for i, r in enumerate(row_galaxy_count):
    if r==0:
        for g in galaxies:
            if g.orig_x > i:
                g.x+=1

sum = 0
for i1, g1 in enumerate(galaxies):
    for g2 in galaxies[i1+1:]:    
        dist = abs(g2.x - g1.x) + abs(g2.y - g1.y)    
        sum += dist    
print(sum)
