import string

# Part One
data = open("dayTwoInput.txt", "r")
maxRed = 12
maxGreen = 13
maxBlue = 14 
idSum = 0
for line in data:
    validRed = True
    validBlue = True
    validGreen = True
    gameID = line.split(':')[0].split(' ')[1]
    gameData = line.split(':')[1].split(";")
    for round in gameData:
        colors = round.split(',')
        for color in colors:
            match color.split(" ")[2].split("\n")[0]:
                case "green":
                    if int(color.split(" ")[1]) > maxGreen:
                        validGreen = False
                case "blue":
                    if int(color.split(" ")[1]) > maxBlue:
                        validBlue = False
                case "red":
                    if int(color.split(" ")[1]) > maxRed:
                        validRed = False
    if validRed & validBlue & validGreen:
        idSum += int(gameID)
print(f"Part one sum of IDs is: {idSum}")

# Part Two
data = open("dayTwoInput.txt", "r")
totalSum = 0
for line in data:
    minRed = -1
    minBlue = -1
    minGreen = -1
    gameData = line.split(':')[1].split(";")
    for round in gameData:
        colors = round.split(',')
        for color in colors:
            match color.split(" ")[2].split("\n")[0]:
                case "green":
                    if int(color.split(" ")[1]) > minGreen:
                        minGreen = int(color.split(" ")[1])
                case "blue":
                    if int(color.split(" ")[1]) > minBlue:
                        minBlue = int(color.split(" ")[1])
                case "red":
                    if int(color.split(" ")[1]) > minRed:
                        minRed = int(color.split(" ")[1])
    totalSum+= (minRed * minGreen * minBlue)
print(f"Part two sum of powers is: {totalSum}")
