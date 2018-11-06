from dataScraping import scrapeData


def writeCSV(filename, data):
    with open(filename, "w") as outputFile:
        for row in data:
            writeRow = ""
            for i in range(len(row)):
                writeRow += str(row[i])
                if i != len(row) - 1:
                    writeRow += ","
            outputFile.write(writeRow + "\n")


# Scrape the data from the text file into a large table
data = scrapeData("aberporth_meteorological_data.txt")


# dataDict is composed of:
# year : [[month 1's data], [month 2's data]]
# note that the actual month number is dropped in [2:]
dataDict = {}
for row in data:
    key = row[0]
    value = [row[2:]]
    newValue = []
    # Iterate through the value types (rainfall, temperature etc.)
    for o in range(len(value[0])):
        # Get all the values of the current type for that year, eg. all the temperatures, rainfalls, and store them in a list
        dataValues = [value[i][o] for i in range(len(value))]
        # Calculate the average of that list and append it to the new list
        newValue.append(sum(dataValues) / len(dataValues))
    dataDict[key] = newValue

print(dataDict)
# Get the data back in the right format, ie. [year, data1, data2, ...]
data = [(list(key) + value) for key, value in dataDict.items()]
writeCSV("processedData.csv", data)
