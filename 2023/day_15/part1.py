with open("input.txt", encoding="utf-8") as f:
    line = f.readline().strip()

sum: int = 0
seqs = line.split(",")
for seq in seqs:
    val: int = 0
    for char in seq:
        val += ord(char)
        val *= 17
        val %= 256
    sum += val

print(sum)
