import numpy

histories = []
with open("input.txt") as f:
    for line in f.readlines():
        history = list(map(lambda x: int(x.strip()), line.strip().split(" ")))
        histories.append(history)

sum: int = 0
for history in histories:
    prediction = 0
    while not all(v == 0 for v in history):
        prediction += history[-1]
        history = numpy.diff(history)
    sum += prediction
print(sum)
