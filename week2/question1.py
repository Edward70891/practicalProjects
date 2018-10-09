print("Enter your first number:")
num1 = input(">")
print("Enter your second number:")
num2 = input(">")
print("Enter your third and final number:")
num3 = input(">")

if num3 > num2 and num3 > num1:
    print("Your third number, " + str(num3) + ", was the highest!")
elif num2 > num3 and num2 > num1:
    print("Your second number, " + str(num2) + ", was the highest!")
elif num1 > num3 and num1 > num2:
    print("Your third nunber, " + str(num3) + ", was the highest!")
elif num1 == num2 and num2 == num3:
    print("All three numbers are the same!")
elif num1 == num2:
    print("Your first and second numbers were both equal to " + str(num1) + ", which is the highest number!")
elif num1 == num3:
    print("Your first and third numbers were both equal to " + str(num1) + ", which is the highest number!")
elif num2 == num3:
    print("Your second and third numbers were both equal to " + str(num2) + ", which is the highest number!")
else:
    print("You've somehow managed to break the program!")
