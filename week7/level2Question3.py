from dataScraping import *


def calcAvg(items):
    total = 0
    for item in items:
        total += item
    return round(float(total) / len(items), 3)


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
dataDict = {}
for row in data:
    if row[0] in dataDict.keys():
        dataDict[row[0]].append(row[2:])
    else:
        dataDict[row[0]] = [row[2:]]
# computedDict is composed of:
# year : [year's average data]
computedDict = {}
# Iterate through the years
for key, value in dataDict.items():
    avgYearData = []
    # Iterate through the different types of values (rainfall, temp etc.)
    for i in range(len(value[0])):
        toAvg = []
        # Iterate through each month's value and add it to a list to be averaged
        for monthData in value:
            toAvg.append(monthData[i])
        avg = calcAvg(toAvg)
        avgYearData.append(avg)
    computedDict[key] = avgYearData


# Get the data back in the right format
data = []
for key, value in computedDict.items():
    row = [key]
    for entry in value:
        row.append(entry)
    data.append(row)
writeCSV("processedData.csv", data)
