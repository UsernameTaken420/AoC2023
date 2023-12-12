import re

# Part One
data = open("dayOneInput.txt", "r")
partOneSum = 0
for line in data:
    firstNum = 0
    lastNum = 0
    for char in line:
        if char.isnumeric():
            if firstNum==0:
                firstNum = char
            lastNum = char
    numberGen = str(firstNum) + str(lastNum)
    partOneSum+=int(numberGen)
print(f"The final sum for part one is: {partOneSum}")

# Part Two
data = open("dayOneInput.txt", "r")
textNumbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
partTwoSum = 0
for line in data:
    tempLine = line
    digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', tempLine)
    for number in digits:
        if number in textNumbers:
            digits[digits.index(number)] = str(textNumbers[number])
    firstNum = 0
    lastNum = 0
    for char in digits:
        if char.isnumeric():
            if firstNum == 0:
                firstNum = char
            lastNum = char
    numberGen = str(firstNum) + str(lastNum)
    partTwoSum+=int(numberGen)
print(f"The final sum for part two is: {partTwoSum}")