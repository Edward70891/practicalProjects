numbers = [int(input("First Number >")), int(input("Second Number >")), int(input("Third Number >"))]

maxes = max(numbers)
if isinstance(maxes, list):
    for highest in maxes:
        print("Number " + str(numbers.index(highest) + 1) + " was joint highest at " + str(highest))
else:
    print("Number " + str(numbers.index(maxes) + 1) + " was highest at " + str(maxes))
