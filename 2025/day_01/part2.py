with open("test.txt") as file:
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
    delta = raw_pos - prev_pos
    pos %= 100
    print(f"dial is incremented of {line} and now points at {pos}")
    count_incr: int = 0
    if abs(delta - prev_pos) >= 100:
        count_incr = abs(delta - prev_pos) // 100

    if count_incr > 0:
        print(f"it points at 0 - {count_incr} times")
    count += count_incr

    prev_pos = pos
print(f"Total of zero counts: {count}")
