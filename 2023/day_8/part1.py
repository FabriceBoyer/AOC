from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    start: str
    left: str
    right: str


with open("input.txt") as f:
    instructions = f.readline().strip()
    f.readline()
    nodes_str = [line.strip() for line in f.readlines()]

nodes: dict[str, Node] = {}
pattern_size: int = len(instructions)

for node_str in nodes_str:
    part_split = node_str.split("=")
    name = part_split[0].strip()
    lr_split = part_split[1].strip()[1:-1].split(",")
    nodes[name] = Node(name, lr_split[0].strip(), lr_split[1].strip())

current: Node = nodes["AAA"]
cursor: int = 0
steps: int = 0
while current.start != "ZZZ":
    instruction = instructions[cursor]
    if instruction == "L":
        current = nodes[current.left]
    elif instruction == "R":
        current = nodes[current.right]
    else:
        raise Exception("Shouldn't happen")
    cursor += 1
    cursor %= pattern_size
    steps += 1

print(steps)
