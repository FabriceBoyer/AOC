import numpy

histories = []
with open("input.txt") as f:
    for line in f.readlines():
        history = list(map(lambda x: int(x.strip()), line.strip().split(" ")))
        histories.append(history)

sum: int = 0
for history in histories:
    first_values = []
    while not all(v == 0 for v in history):
        first_values.append(history[0])
        history = numpy.diff(history)
    first_values.reverse()
    prediction = 0
    for value in first_values:
        prediction = value - prediction
    sum += prediction
print(sum)
