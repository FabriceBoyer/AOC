sum = 0
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])
grid = [["" for c in range(col_count)] for l in range(line_count)]
parts = [[(-1, -1) for c in range(col_count)] for l in range(line_count)]  # uid, value
for line_idx, line in enumerate(lines):
    for char_idx, char in enumerate(line):
        grid[line_idx][char_idx] = char

part_number = ""
uid = 0
for line in range(line_count):
    for col in range(col_count):
        if grid[line][col].isdigit():
            part_number += grid[line][col]
            if col == col_count - 1:
                uid += 1
                for i in range(len(part_number)):
                    parts[line][col - i] = (uid, int(part_number))
                part_number = ""  # reset
        else:
            if part_number != "":
                uid += 1
                for i in range(len(part_number)):
                    parts[line][col - i - 1] = (uid, int(part_number))
                part_number = ""  # reset

with open("output.txt", "w") as f:
    for line in range(line_count):
        msg = ""
        for col in range(col_count):
            msg += str(parts[line][col]) + "\t"
        f.write(msg + "\n")

for line in range(line_count):
    for col in range(col_count):
        char = grid[line][col]
        if char == "*":  # is star
            adj_parts = set()  # avoid duplicates
            for l in [-1, 0, 1]:
                for c in [-1, 0, 1]:
                    if l == 0 and c == 0:
                        continue
                    if (
                        line + l < 0
                        or line + l >= line_count
                        or col + c < 0
                        or col + c >= col_count
                    ):
                        continue
                    if parts[line + l][col + c] != (-1, -1):
                        adj_parts.add(parts[line + l][col + c])
            if len(adj_parts) == 2:
                print(f"Gear at {line + 1}, {col + 1} adjacent to {adj_parts}")
                ratio = 1
                for part in adj_parts:
                    ratio *= part[1]
                sum += ratio

print(sum)
