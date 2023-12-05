import os

textNumberArray = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def getTextNumberEndValue(str) -> int:
    i = 0
    for textNumber in textNumberArray:
        i += 1
        if str.endswith(textNumber):
            return i
    return -1


with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

sum = 0
for line in lines:
    char1Set = False
    partialTextNumber = ""
    for char in line:
        if char.isnumeric():  # num
            partialTextNumber = ""  # reset
            if not char1Set:
                char1 = char
                char1Set = True
                char2 = char1
            else:
                char2 = char
        else:  # alpha
            partialTextNumber += char
            number = getTextNumberEndValue(partialTextNumber)
            if number > 0:
                partialTextNumber = char
                if not char1Set:
                    char1 = str(number)
                    char1Set = True
                    char2 = char1
                else:
                    char2 = str(number)

    calibValue = int(char1 + char2)
    print(f"Calib value of '{line}' is '{calibValue}'")
    sum += calibValue

print(f"Sum:  {sum}")
