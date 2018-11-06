def scrapeData(fileName):
    data = []
    with open(fileName, "r") as toRead:
        for line in toRead.readlines():
            if line.split()[0][0] not in "#":
                data.append([getValue(x.replace("\n", "").replace(" ", "")) for x in line.split(",")])
    return data


def getValue(string):
    try:
        string = int(string)
    except ValueError:
        try:
            string = float(string)
        except ValueError:
            pass
    return string
