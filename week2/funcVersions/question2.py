print("How many hours did you work?")
hours = float(input(">"))
print("How much do you get paid (per hour)?")
salary = float(input(">"))
print("You're owed " + str(hours * salary) + " pounds in ordinary wages.")

if hours > 40:
    print("You've worked overtime!")
    overtime = hours - 40
    print("You're owed " + str(overtime * salary * 0.5) + " pounds in additional overtime pay!")
