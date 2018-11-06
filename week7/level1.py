def saveListToFile(sentences, filename):
    outputFile = open(filename, "w")
    for string in sentences:
        outputFile.write(string)
    outputFile.close()


def saveToLog(entry, logfile):
    output = open(logfile, "a")
    outputFile.write(entry)
    outputFile.close()


def upperCasePrint(fileName):
    with open(fileName, "r") as toRead:
        for line in toRead:
            print(line.upper())


def toUpperCase(inputFile, outputFile):
    with open(inputFile, "r") as toRead:
        with open(outputFile, "w") as toWrite:
            for line in toRead:
                outputFile.write(line.upper())


def sumString(string):
    digits = string.split()
    total = 0
    for number in digits:
        try:
            total += int(number)
        except TypeError:
            print("Non-integer value in file at " + number + "!")
            return
    return total


def sumFile(fileName):
    total = 0
    with open(fileName, "r") as toRead:
        for line in toRead:
            total += sumString(line)
    return total
