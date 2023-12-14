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


# vertical reflection check
def get_vsymetry_index(_pattern: list[str], rejected: int) -> int:  # -1 means not found
    col_count = len(_pattern[0])
    for r_index in range(1, col_count):  # reflection index
        if r_index == rejected:
            continue
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


def get_reflection_line(
    _pattern: list[str], reject: tuple[str, int]
) -> tuple[str, int]:
    reject_id = reject[1] if reject[0] == "vertical" else -1
    v_reflect = get_vsymetry_index(_pattern, reject_id)
    if v_reflect != -1:
        res = ("vertical", v_reflect)
    else:
        reject_id = reject[1] if reject[0] == "horizontal" else -1
        h_reflect = get_vsymetry_index(get_transpose(_pattern), reject_id)
        if h_reflect != -1:
            res = ("horizontal", 100 * h_reflect)
        else:
            res = ("none", -1)
    return res


# analyse
summary = 0
for i_pattern, pattern in enumerate(patterns):
    orig_line = get_reflection_line(pattern, ("none", -1))
    if orig_line[0] == "none":
        raise ValueError("no reflection found")
    smudge_found = False
    for y, line in enumerate(pattern):
        for x, char in enumerate(line):
            new = "#" if char == "." else "."
            newline = line[:x] + new + line[x + 1 :]
            pattern[y] = newline  # smudge
            smudged_line = get_reflection_line(pattern, orig_line)
            pattern[y] = line  # restore
            if smudged_line[0] != "none" and smudged_line != orig_line:
                print(
                    f"for pattern {i_pattern}, a smudge added at ({x}, {y}) changed refection from {orig_line} to {smudged_line}"
                )
                summary += smudged_line[1]
                smudge_found = True
                break
        if smudge_found:
            break
    if not smudge_found:
        print(f"no smudge found for pattern {i_pattern}")

print(summary)
