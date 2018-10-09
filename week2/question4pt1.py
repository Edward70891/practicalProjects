print("Enter the year:")
year = int(input(">"))
if (year / 4) % 1 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print("This isn't a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This isn't a leap year.")
