with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

count: int = 0
for line in lines:
    count += 1

print(f"{count}")
