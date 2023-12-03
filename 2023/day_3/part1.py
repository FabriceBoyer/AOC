sum = 0
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

line_count = len(lines)
col_count = len(lines[0])
grid = [["" for c in range(col_count)] for l in range(line_count)]
valid = [[False for c in range(col_count)] for l in range(line_count)]
for line_idx, line in enumerate(lines):
    for char_idx, char in enumerate(line):
        grid[line_idx][char_idx] = char

for line in range(line_count):
    for col in range(col_count):
        char = grid[line][col]
        if char != "." and not char.isdigit():  # isSymbol
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
                    if grid[line + l][col + c].isdigit():
                        valid[line + l][col + c] = True

part_number = ""
at_least_1_digit_valid = False
for line in range(line_count):
    if part_number != "" and at_least_1_digit_valid:
        sum += int(part_number)
    part_number = ""  # reset
    at_least_1_digit_valid = False  # reset
    for col in range(col_count):
        if grid[line][col].isdigit():
            part_number += grid[line][col]
            if valid[line][col]:
                at_least_1_digit_valid = True
        else:
            if part_number != "" and at_least_1_digit_valid:
                sum += int(part_number)
            part_number = ""  # reset
            at_least_1_digit_valid = False  # reset
print(sum)
