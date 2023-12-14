with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

weight = 0
stopper_offset = [0 for _ in range(len(lines[0]))]
line_count = len(lines)
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            stopper_offset[x] = y + 1
        elif char == "O":
            weight += (line_count - stopper_offset[x])
            stopper_offset[x] += 1
        elif char == ".":
            pass
        else:
            raise ValueError(f"Unknown char {char}")
print(weight)
