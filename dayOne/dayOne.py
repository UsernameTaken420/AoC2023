import os
import string


data = open("dayOneInput.txt", "r")
# Part One
totalsum = 0
for line in data:
    firstNum = 0
    lastNum = 0
    for char in line:
        if char.isnumeric():
            if firstNum==0:
                firstNum = char
            lastNum = char
    numberGen = firstNum + lastNum
    totalsum+=int(numberGen)
print(totalsum)