from os import system, name

# Functions to make it pretty
def unknownInput():
    print("Are you sure you spelled that right?")
    enterContinue()
    
def enterContinue():
    print("Press enter to go again.")
    input()

def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")

# Return a float from user input.
# Can be labelled
def floatInput(text):
    text = str(text)
    return float(input(text + "> "))

# Program is wrapped in a while loop to facilitate repeated interaction and to avoid having to launch again and again.
while True:

    # Clear the console and welcome the user. Take their choices, this would be better with an enumerator or numbered selection.
    clear()
    print("Welcome to the imperial converter!")
    print("Enter the system you're converting from:")
    choice = input("> ").lower()
    if choice == "quit":
        break
    print("Please enter the metric you wish to convert. Supported are distance, weight and volume.")
    metricChoice = input("> ").lower()
    if metricChoice == "quit":
        break


    if choice == "imperial":
        imperial = []
        while True:
            if metricChoice == "distance":
                #Get the amounts and store them in a list for easy iteration
                print("Enter your imperial dimensions:")
                imperial.append(floatInput("Yards"))
                imperial.append(floatInput("Feet"))
                imperial.append(floatInput("Inches"))
                # Set any blank inputs to 0.
                for i in range(0, len(imperial)):
                    if imperial[i] == "":
                        imperial[i] = 0
                # Perform the conversion.
                metres = (imperial[0] * 0.9144) + (imperial[1] * 0.3048) + (imperial[2] * 0.0254)
                # Show the result to the user.
                print("This distance is equal to " + str(round(metres, 2)) + " metres.")
                enterContinue()
                break
            elif metricChoice == "weight":
                # Get the amounts and store them in a list for easy iteration.
                print("Enter your imperial weights:")
                imperial.append(floatInput("Stones"))
                imperial.append(floatInput("Pounds"))
                # Set any blank inputs to 0.
                for i in range(0, len(imperial)):
                    if imperial[i] == "":
                        imperial[i] = 0
                # Perform the conversion.
                kilos = (imperial[0] * 6.35029) + (imperial[1] * 0.453592)
                # Show the result to the user.
                print("This weight is equal to " + str(round(kilos, 2)) + " kilograms.")
                break
            elif metricChoice == "volume":
                # Get the amounts and store them in a list for easy iteration.
                print("Enter your imperial volumes:")
                imperial.append(floatInput("Gallons"))
                imperial.append(floatInput("Quarts"))
                imperial.append(floatInput("Pints"))
                imperial.append(floatInput("Cups"))
                # Set any blank inputs to 0.
                for i in range(0, len(imperial)):
                    if imperial[i] == "":
                        imperial[i] = 0
                # Perform the conversion.
                litres = (imperial[0] * 4.54609) + (imperial[1] * 1.13652) + (imperial[2] * 0.5) + (imperial[3] * 0.284131)
                # Show the result to the user.
                print("This volume is equal to " + str(round(litres, 2)) + " litres.")
                enterContinue()
                break
            else:
                unknownInput()


    elif choice == "metric":
        metric = []
        while True:
            if metricChoice == "distance":
                #Get the amounts and store them in a list for easy iteration
                print("Enter your metric system dimensions:")
                metric.append(floatInput("Metres"))
                # Set any blank inputs to 0.
                for i in range(0, len(metric)):
                    if metric[i] == "":
                        metric[i] = 0
                yards = metric[0] * 1.09361
                print("This distance is equal to " + str(round(yards, 2)) + " yards.")
                enterContinue()
                break
            if metricChoice == "weight":
                #Get the amounts and store them in a list for easy iteration
                print("Enter your metric system dimensions:")
                metric.append(floatInput("Kilograms"))
                # Set any blank inputs to 0.
                for i in range(0, len(metric)):
                    if metric[i] == "":
                        metric[i] = 0
                stones = metric[0] * 0.157473
                print("This weight is equal to " + str(round(stones, 2)) + " stone.")
                enterContinue()
                break
            if metricChoice == "volume":
                #Get the amounts and store them in a list for easy iteration
                print("Enter your metric system dimensions:")
                metric.append(floatInput("Litres"))
                # Set any blank inputs to 0.
                for i in range(0, len(metric)):
                    if metric[i] == "":
                        metric[i] = 0
                gallons = metric[0] * 0.219969
                print("This volume is equal to " + str(round(gallons, 2)) + " gallons.")
                enterContinue()
                break

    # If they didn't enter some variation of the specified commands, just ask them again.
    else:
        unknownInput()
        continue
