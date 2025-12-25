with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

count: int = 0
pos: int = 50
for line in lines:
    dir: int = 1
    if line[0] == "L":
        dir = -1
    increment = int(line[1:])
    pos += dir * increment
    pos %= 100
    print(f"dial is incremented of {increment} and now points at {pos}")
    if pos == 0:
        count += 1
print(f"Total of zero counts: {count}")
