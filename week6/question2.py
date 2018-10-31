def generateBasePattern(size, str1, str2):
    if size < 3:
        raise ValueError("Size too small!")
    output = []
    for i in range(size):
        line = ""
        for o in range(size):
            if o == i or o == size - i - 1:
                line += str1
            else:
                line += str2
        output.append(line)
    return output


def printBasePattern(size, str1, str2):
    output = generateBasePattern(size, str1, str2)
    for line in output:
        print(line)
