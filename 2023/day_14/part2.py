from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import numpy as np

# @dataclass
# class Platform:


with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]


line_count = len(lines)
col_count = len(lines[0])
platform = np.zeros((line_count, col_count), dtype=int)

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            platform[y, x] = 1
        elif char == "O":
            platform[y, x] = 2
        elif char == ".":
            platform[y, x] = 0
        else:
            raise ValueError(f"Unknown char {char}")


def tilt_north(platform):
    stopper_offset = [0 for _ in range(len(lines[0]))]
    for y, line in enumerate(lines):
        for x, elem in enumerate(line):



def rotate(platform):
    platform.rot90()

def cycle(platform):
    pass


weight = 0
print(weight)
