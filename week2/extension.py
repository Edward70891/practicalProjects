def menu(options):
        if not all(isinstance(x, str) for x in options):
            for option in options:
                if not isinstance(option, str) and not isinstance(option, list):
                    raise ValueError("Non-string option passed to menu!")
        for i in range(len(options) - 1):
            optionName = options[i+1]
            if isinstance(options[i+1], list):
                optionName = options[i+1][0]
            print(str(i + 1) + ") " + optionName)
        while(True):
            print()
            print("Please select an option by putting it's number in:")
            selection = int(input(">"))
            if selection >= len(options):
                print("That's an invalid selection!")
            elif isinstance(options[selection], list):
                return [selection].append(menu(options[selection]))
            else:
                return selection

# The main program
again = True
total = 0
while (again):
    products = [["Products", "DVD", "Blu-ray", "New Game", "Game"], [0, 2.5, 3.5, 4, 2.5]]
    selection = menu(products[0])
    price = products[1][selection]
    total += price
    print("That costs " + str(price) + " pounds, making your total " + str(total) + " pounds")
    print("Would you like to go again [y/n]?")
    goAgain = str(input(">"))
    if goAgain.lower() == "n":
        again = False

print("Okay, your total cost is " + str(total) + " pounds!")
