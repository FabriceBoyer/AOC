def readMerged(str) -> int:
    return int(str.split(":")[1].replace(" ", ""))


with open("input.txt") as f:
    total_time = readMerged(f.readline())
    record_distance = readMerged(f.readline())

# brute force
ways_to_win = 0
for press_time in range(total_time):
    remaining_time = total_time - press_time
    distance = press_time * remaining_time
    if distance > record_distance:
        ways_to_win += 1

print(ways_to_win)
