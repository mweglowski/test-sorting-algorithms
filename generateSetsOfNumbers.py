import random

def generateSetsOfNumbers(numOfSets, setLength):
    file = open('setsData.txt', 'w')

    sets = []
    for i in range(numOfSets):
        numSet = []
        for j in range(setLength):
            numSet.append(str(random.randint(0, 100)))
        sets.append(numSet)

    setsString = ""
    for item in sets:
        item = " ".join(item)
        setsString += item + '\n'
    # setsString = setsString[:-1]

    file.write(setsString)
    file.close()


