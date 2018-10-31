def generateBasePattern(size):
    if size < 3:
        raise ValueError("Size too small!")
    output = []
    for i in range(size):
        line = ""
        for o in range(size):
            if o == i or o == size - i - 1:
                line += "x"
            else:
                line += "."
        output.append(line)
    return output


def printBasePattern(size):
    output = generateBasePattern(size)
    for line in output:
        print(line)
