def scrapeData(fileName):
    data = []
    with open(fileName, "r") as toRead:
        for line in toRead.readlines():
            if line[:2] != "##":
                data.append([getValue(x.replace("\n", "")) for x in line.split(",")])
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
