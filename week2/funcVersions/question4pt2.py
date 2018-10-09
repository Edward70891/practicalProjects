print("Please enter the date in the format DD/MM/YYYY:")
date = str(input(">"))

# Parse the date for the values
dateParsed = date.split("/")
day = int(dateParsed[0])
month = int(dateParsed[1])
year = int(dateParsed[2])

# Define some arrays to search for the differently lengthed months
months31 = [1,3,5,7,8,10,12]
months30 = [4,6,9,11]

# Set the appropriate day limit based on the month
if month in months31:
    daysmax = 31
elif month in months30:
    daysmax = 30
elif month == 2:
    if (year / 4) % 1 == 0:
        if year % 100 == 0 and year % 400 != 0:
            daysmax = 28
        else:
            daysmax = 29
    else:
        daysmax = 28

# Actually perform all the checks
if month > 12:
    print("Imaginary month, invalid")
elif day > daysmax:
    print("Too many days in that month, invalid")
else:
    print("Valid")
