import math


def count_multiples_of_100_excluding_a(a, b):
    if a < b:
        return max(0, math.floor(b / 100) - math.floor(a / 100))
    elif a > b:
        return max(0, math.floor((a - 1) / 100) - math.floor((b - 1) / 100))
    else:
        return 0


with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

count: int = 0
pos: int = 50
prev_pos: int = pos
for line in lines:
    dir: int = 1
    if line[0] == "L":
        dir = -1
    increment = int(line[1:])

    pos += dir * increment
    raw_pos = pos
    pos %= 100
    print(f"dial is incremented of {line} and now points at {pos}")

    count_incr: int = count_multiples_of_100_excluding_a(prev_pos, raw_pos)
    if count_incr > 0:
        print(f"it points at 0 - {count_incr} times")
    count += count_incr

    prev_pos = pos
print(f"Total of zero counts: {count}")
