sampleImage = [
    [0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0],
    [1,1,1,0,1,1,1,0],
    [1,0,1,0,0,1,1,0],
    [1,1,1,0,0,0,0,0],
    [1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1],
    [0,0,0,0,0,0,1,1]
    ]


def cellSize(image, x, y, neighbourhood = 8):
    alreadyExamined = []
    return cellSizeRec(image, x, y, neighbourhood, alreadyExamined)


def cellSizeRec(image, x, y, neighbourhood, exclude):
    if x >= len(image) or y >= len(image[0]) or image[x][y] == 0:
        return 0
    total = 1
    exclude.append([x, y])
    toCheck = []
    if neighbourhood == 4:
        toCheck = [[x, y + 1], [x + 1, y], [x, y - 1], [x - 1, y]]
    elif neighbourhood == 8:
        X = [x - 1, x, x + 1]
        Y = [y - 1, y, y + 1]
        toCheck = [[i,o] for i in X for o in Y]
    for coord in toCheck:
        if coord not in exclude:
            total += cellSizeRec(image, coord[0], coord[1], neighbourhood, exclude)
            print(total)
    return total


print(cellSize(sampleImage, 1, 0, 8))
