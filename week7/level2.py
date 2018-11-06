from dataScraping import *


def minPrecip(fileName):
    data = {k:v for k,v in (scrapeData(fileName))}
    miniValue = min(data.values())
    years = [k for k,v in data.items() if v == miniValue]
    return years


def maxPrecip(fileName):
    data = {k:v for k,v in (scrapeData(fileName))}
    maxiValue = max(data.values())
    years = [k for k,v in data.items() if v == maxiValue]
    return years


def avgPrecip(fileName):
    data = scrapeData(fileName)
    total = 0
    for point in data:
        total += point[1]
    return total / len(data)


def collatePrecipFiles(fileNames, outputFile):
    data = [scrapeData(table) for table in fileNames]
    totalData = []
    for table in data:
        totalData.extend(table)
    collatedData = {}
    for row in totalData:
        if row[0] in collatedData.keys():
            collatedData[row[0]].append(row[1])
        else:
            collatedData[row[0]] = [row[1]]
    print(collatedData)


collatePrecipFiles(["precipitations-Europe.txt", "precipitations-NAmerica.txt", "precipitations-world.txt"], "blag")
