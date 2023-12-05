import os

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

sum = 0
for line in lines:
    char1Set = False
    for char in line:
        if char.isnumeric():
            if not char1Set:
                char1 = char
                char1Set = True
                char2 = char1
            else:
                char2 = char
    calibValue = int(char1 + char2)
    print(f"Calib value of '{line}' is '{calibValue}'")
    sum += calibValue

print(f"Sum:  {sum}")
