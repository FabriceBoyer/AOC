# day 2 / part 1
with open("input.txt", "r", encoding="utf-8") as file:
    intervals = file.read().split(",")
    sum: int = 0
    for interval in intervals:
        start, end = map(int, interval.split("-"))
        # print(f"{end-start}")

        for num_id in range(start, end + 1, 1):
            id_str: str = str(num_id)
            if len(id_str) % 2 != 0:
                continue
            cut: int = len(id_str) // 2
            first_half: str = id_str[:cut]
            second_half: str = id_str[cut:]
            if first_half == second_half:  # invalid
                print(f"invalid id: {num_id}")
                sum += num_id

    print(f"Sum of invalid: {sum}")
