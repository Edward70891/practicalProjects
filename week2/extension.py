def menu(options):
    if not all(isinstance(x, str) for x in options):
        raise ValueError("Non-string options were passed to menu()")
    for i in range(len(options)):
        print(str(i + 1) + ") " + str(options[i]))
    while(True):
        print()
        print("Please select an option by putting it's number in:")
        selection = int(input(">")) - 1
        if selection > len(options):
            print("That's an invalid selection!")
        else:
            return selection

# The main program
again = True
total = 0
while (again):
    products = [["DVD", "Blu-ray", "New Game", "Game"], [2.5, 3.5, 4, 2.5]]
    selection = menu(products[0])
    price = products[1][selection]
    total += price
    print("That costs " + str(price) + " pounds, making your total " + str(total) + " pounds")
    print("Would you like to go again [y/n]?")
    goAgain = str(input(">"))
    if goAgain.lower() == "n":
        again = False

print("Okay, your total cost is " + total + " pounds!")
