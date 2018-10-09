print("What was the speed limit?")
limit = int(input(">"))
print("How fast were you going?")
speed = int(input(">"))

if speed > limit:
    print("You were speeding!")
    if speed > 90:
        print("You were also over 90 so you owe extra!")
        fine = 300 + 5 * (speed - limit)
    else:
        fine = 100 + 5 * (speed - limit)
    print("You owe " + str(fine) + " pounds fine!")
else:
    print("Congratulations, you're a safe driver.")
