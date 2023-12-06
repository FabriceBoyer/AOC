def cleanup(str_list):
    return list(
        map(lambda x: int(x.strip()), filter(lambda x: x != "", str_list.split(" ")))
    )


with open("input.txt") as f:
    times_str = f.readline().split(":")[1]
    times = cleanup(times_str)
    distances = cleanup(f.readline().split(":")[1])


result = 1
for i in range(len(times)):  # races
    total_time = times[i]
    record_distance = distances[i]
    ways_to_win = 0
    for press_time in range(total_time):
        remaining_time = total_time - press_time
        distance = press_time * remaining_time
        if distance > record_distance:
            ways_to_win += 1
    result *= ways_to_win
print(result)
