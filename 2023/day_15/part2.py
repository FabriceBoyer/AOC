from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Lens:
    label: str
    focal: int


@dataclass
class Box:
    lenses: list[Lens]


with open("input.txt", encoding="utf-8") as f:
    line = f.readline().strip()


def get_box_id(label_: str) -> int:
    val: int = 0
    for char in label_:
        val += ord(char)
        val *= 17
        val %= 256
    return val


boxes: list[Box] = [Box([]) for _ in range(256)]  # fixed size

seqs = line.split(",")
for seq in seqs:
    if seq[-1] == "-":  # remove
        label: str = seq[:-1]
        box_id: int = get_box_id(label)
        box: Box = boxes[box_id]
        for lens in box.lenses:
            if lens.label == label:
                box.lenses.remove(lens)
                break

    else:  # add
        split = seq.split("=")
        label: str = split[0]
        focal: int = int(split[1])
        box_id: int = get_box_id(label)
        box: Box = boxes[box_id]
        replaced: bool = False
        for i_lens, lens in enumerate(box.lenses):
            if lens.label == label:
                box.lenses[i_lens] = Lens(label, focal)
                replaced = True
                break
        if not replaced:
            box.lenses.append(Lens(label, focal))

power: int = 0
for box_id, box in enumerate(boxes):
    for slot, lens in enumerate(box.lenses):
        print(f"box {box_id} / lense {slot} ({lens.label} {lens.focal})")
        power += (box_id + 1) * (slot + 1) * lens.focal

print(power)
