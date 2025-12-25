with open("input.txt", "r", encoding="utf-8") as file:
    banks = [line.rstrip() for line in file]

total: int = 0
for bank in banks:
    highest: int = 0
    for i1, bat1 in enumerate(bank):
        for bat2 in bank[(i1 + 1) :]:
            val = int(bat1 + bat2)
            if val > highest:
                highest = val
    print(f"{bank}: {highest}")
    total += highest

print(f"Sum is : {total}")
