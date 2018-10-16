class vector:
    # Print a vector with an optional highlight on an element
    def printVector(self, highlightCoord = [-1, -1]):
        # Iterate through the rows of the vector, printing a space at the beginning of each
        for y in range(len(self.value[0])):
            print(" ", end = "")
            # Iterate through the elements in the row, printing each (with brackets around the highlighted one)
            for x in range(len(self.value)):
                if x == highlightCoord[0] and y == highlightCoord[1]:
                    print("[" + str(self.value[x][y]) + "]\t", end="")
                else:
                    print(str(self.value[x][y]) + " \t", end="")
            print()
        print()

    # Create a vector based on user input
    def __init__(self):
        # Obtain the needed dimensions of the vector
        print("How wide do you want your vector to be?")
        width = int(input("Width> "))
        print("How tall do you want your vector to be?")
        height = int(input("Height> "))
        self.value = list()
        # Generate an empty vector of the appropriate size
        for x in range(width):
            self.value.append(list())
            for y in range(height):
                self.value[x].append(0)
        # Fill the vector
        for y in range(len(self.value)):
            for x in range(len(self.value[x])):
                self.printVector([x,y])
                self.value[x][y] = int(input(">"))

    # Return the scalar product of a number and a vector
    def scalarProduct(self, scalar):
        for x in range(len(self.value)):
            for y in range(len(self.value[x])):
                self.value[x][y] *= scalar

    # Return the sum of two vectors
    def vectorAddition(self, vector2):
        if len(self.value) != len(vector2.value) or len(self.value[0]) != len(vector2.value[0]):
            raise ValueError("Differing array dimensions")
        for x in range(len(self.value)):
            for y in range(len(self.value[x])):
                self.value[x][y] += vector2.value[x][y]

print("Do you want to add[1] or scalar multiply[2]?")
choice = input(">")

