import math


primesDict = {2: True}


# Completely useless
def basic(num):
    if num < 2 or num > 49:
        raise OverflowError
    divisors = (2, 3, 5, 7)
    prime = True
    for current in divisors:
        if num % divisors == 0:
            prime = False
    return prime


# Runs through all numbers between 2 and the square root
# (rounded down if necessary) of the number and checks if they divide it
def advanced(num):
    prime = True
    for i in range(2, math.floor(num**(0.5)) + 1):
        if num % i == 0:
            prime = False
    return prime


# Calls the above, but checks if the number is in the primes dictionary
# beforehand. If it is a prime but not in the dictionary, it is added to the
# dictionary.
def clever(num):
    if num in primesDict.keys():
        prime = True
    else:
        prime = advanced(num)
    if prime:
        primesDict[num] = True
    return prime


# Returns a list of all the prime factors of a number; duplicates included.
# Note: recursive.
def primeFactors(num: int) -> list:
    # Ensure the number is an integer, this has the double effect of triggering.
    # an exception if the parse fails.
    num = int(num)
    # Checks if the number is a prime using clever(), and if it is
    # returns it in a list by itself.
    # Note: the base case.
    if clever(num):
        print("Largest prime factor found at " + str(num) + ", terminating...")
        return [num]
    # Runs through all the numbers between 2 and the target's square root
    # (inclusive), and selects the first one which is both a factor of the
    # target and prime, using clever() again.
    # Note: the recursive case.
    for i in range(2, math.floor(num**(0.5)) + 1):
        if num % i == 0 and clever(i):
            print("Found the lowest prime factor at " + str(i))
            print("Calling prime factors with " + str(int(num/i)))
            # Calls the whole function again on the number divided by our
            # prime factor. For example, in the case of 100 we will find
            # the prime factor of 2 and call the function again with 50.
            prior = primeFactors(int(num/i))
            print("primeFactors terminated with " + str(prior.append(i)))
            # Return the total list returned by lower recursions appended with
            # the prime factor this iteration found.
            return prior.append(i)


# The actual function, calls primeFactors and sorts it's return into
# a dictionary to eliminate duplicates without any hassle (using the
# keys of the dictionary as the numbers) then multiplys them together
# to get the product. The unique list is returned along with the
# product.
def olympian(num):
    product = 1
    factors = primeFactors(num)
    uniqueFactors = {}
    for i in factors:
        uniqueFactors[i] = True
    for i in uniqueFactors.keys():
        product *= i
    return (product, list(uniqueFactors.keys()))


data = olympian(100)
print("The product was " + str(data[0]) + ".")
print("This was from the unique factors: " + print(str(data[1])))
