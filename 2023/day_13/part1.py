with open("input.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

# parse
patterns = []
current: list[str] = []
for line in lines:
    if line == "":
        patterns.append(current)
        current = []  # reset
    else:
        current.append(line)


def get_symetry_index(_pattern: list[str]) -> int:  # -1 means not found
    # vertical reflection check
    col_count = len(pattern[0])
    for r_index in range(1, col_count):  # reflection index
        vreflect_ok = True
        for line in _pattern:
            size = min(r_index, col_count - r_index)
            left = line[r_index - size : r_index]
            right = line[r_index : r_index + size]
            if left != right[::-1]:  # compare to reverse right
                vreflect_ok = False
                break
        if vreflect_ok:
            return r_index
    return -1


def get_transpose(_pattern: list[str]) -> list[str]:
    return ["".join(line) for line in zip(*_pattern)]


# analyse
summary = 0
for i_pattern, pattern in enumerate(patterns):
    v_reflect = get_symetry_index(pattern)
    if v_reflect != -1:
        print(f"pattern {i_pattern} has vertical reflection at col {v_reflect}")
        summary += v_reflect
    else:
        pattern = get_transpose(pattern)
        h_reflect = get_symetry_index(pattern)
        if h_reflect != -1:
            print(f"pattern {i_pattern} has horizontal reflection at row {h_reflect}")
            summary += 100 * h_reflect
        else:
            raise ValueError(f"no reflection found for pattern {i_pattern}")

print(summary)
