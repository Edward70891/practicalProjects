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


def printMultipleBasePattern(height, width, size):
    if width < 0 or height < 0:
        raise ValueError("Height and Width must be greater than or equal to 0!")
    pattern = generateBasePattern(size, "O", "-")
    for y in range(height):
        for line in range(size):
            print(pattern[line] * width)
