with open("input.txt", "r", encoding="utf-8") as file:
    intervals = file.read().split(",")
    sum: int = 0
    for interval in intervals:
        start, end = map(int, interval.split("-"))
        # print(f"{end-start}")

        for num_id in range(start, end + 1, 1):
            id_str: str = str(num_id)
            invalid_id: bool = False
            for size in range(1, len(id_str) // 2 + 1):
                if len(id_str) % size != 0:
                    continue
                ref: str = id_str[:size]
                repeated: str = ref * (len(id_str) // size)
                if id_str == repeated:
                    invalid_id = True
                    print(f"invalid id: {num_id}")
                    sum += num_id
                    break

    print(f"Sum of invalid: {sum}")
