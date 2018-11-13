from dataScraping import scrapeData, writeCSV


# Scrape the data from the text file into a large table
dataRaw = scrapeData("aberporth_meteorological_data.txt")


# dataDict is composed of:
# year : [[month 1's data], [month 2's data]]
# notice that the actual month number is dropped in [2:]
dataDict = {}
for row in dataRaw:
    key = row[0]
    value = [row[2:]]
    newValue = []
    # Iterate through the value types (rainfall, temperature etc.)
    for o in range(len(value[0])):
        # Get all the values of the current type for that year, eg. all the temperatures, rainfalls, and store them in a list
        dataValues = [value[i][o] for i in range(len(value))]
        # Calculate the average of that list
        avgValue = round(sum(dataValues) / len(dataValues), 3)
        newValue.append(avgValue)
    dataDict[key] = newValue

# Get the data back in the right format, ie. [year, data1, data2, ...]
data = [[key] + value for key, value in dataDict.items()]
writeCSV("processedData.csv", data)
print("Finished with no errors!")
