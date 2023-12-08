from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    name: str
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

currents: list[Node] = list(
    filter(lambda node: node.name.endswith("A"), list(nodes.values()))
)


def check_all_ends_with_z() -> bool:
    for node in currents:
        if not node.name.endswith("Z"):
            return False
    return True


cursor: int = 0
steps: int = 0
current_count = len(currents)
while not check_all_ends_with_z():
    instruction = instructions[cursor]
    for i in range(current_count):
        node = currents[i]
        if instruction == "L":
            currents[i] = nodes[node.left]
        elif instruction == "R":
            currents[i] = nodes[node.right]
        else:
            raise Exception("Shouldn't happen")
    cursor += 1
    cursor %= pattern_size
    steps += 1
    if steps % 1e6 == 0:
        print(steps)

print(steps)
