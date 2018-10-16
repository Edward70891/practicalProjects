import math

# Prompt the user for a string to test.
print("Input your string to be tested:")
test = input(">")

# Filter out all non-alphabetical characters
test = test.lower()
testList = []
for character in test:
    if character.isalpha():
        testList.append(character)
test = "".join(testList)

# Remove the middle character if it's odd because we don't need to consider it
if len(test) % 2 != 0:
    midpoint = math.floor(len(test) / 2)
    test = test[:midpoint] + test[midpoint + 1:]

# Check through the remaining string comparing back to front
for i in range(int(len(test) / 2)):
    valid = True
    if test[i] != test[len(test) - i - 1]:
        valid = False
        break

# Print the result
print(valid)
