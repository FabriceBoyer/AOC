from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from shapely.geometry.polygon import Polygon

with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

current_x: int = 0
current_y: int = 0
coords: list[tuple[int, int]] = [(current_x, current_y)]

for line in lines:
    split = line.split(" ")
    direction: str = split[0]
    length: int = int(split[1])

    if direction == "R":
        current_x += length
    elif direction == "D":
        current_y += length
    elif direction == "L":
        current_x -= length
    elif direction == "U":
        current_y -= length
    else:
        raise ValueError("Value not recognized")

    coords.append((current_x, current_y))

polygon: Polygon = Polygon(coords)
print(f"Area: {polygon.area}")
print(f"Perimeter: {polygon.length}")
print(polygon.length/2.0 + polygon.area + 1)