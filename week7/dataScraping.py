def scrapeData(fileName):
    """
    scrapeData(string) -> [list, list, ...]
    Reads a CSV-style file and returns a crude, raw list of
    the list of values on each line.
    """
    data = []
    with open(fileName, "r") as toRead:
        for line in toRead.readlines():
            line.replace("\n", "").replace(" ", "")
            if line.split()[0][0] not in "#":
                data.append([getValue(x) for x in line.split(",")])
    return data


def writeCSV(filename, data):
    """
    writeData(filename <- string, data <- [list, list, ...]) -> None
    Takes a list of nested lists and (over)writes it to the
    given file path.
    """
    with open(filename, "w") as outputFile:
        for row in data:
            writeRow = ""
            for i in range(len(row)):
                writeRow += str(row[i])
                if i != len(row) - 1:
                    writeRow += ","
            outputFile.write(writeRow + "\n")


def getValue(string):
    try:
        string = int(string)
    except ValueError:
        try:
            string = float(string)
        except ValueError:
            pass
    return string
