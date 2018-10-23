import math


primesDict = {2: True}


# Runs through all numbers between 2 and the square root
# (rounded down if necessary) of the number and checks if they divide it
def advanced(num):
    for i in range(2, math.floor(num**(0.5)) + 1):
        if num % i == 0:
            return False
    return True


# Calls the above, but checks if the number is in the primes dictionary
# beforehand. If it is a prime but not in the dictionary, it is added to the
# dictionary.
def clever(num):
    prime = num in primesDict.keys()
    if not prime:
        prime = advanced(num)
    if prime:
        primesDict[num] = True
    return prime


# Returns a list of all the prime factors of a number; duplicates included.
# Note: recursive.
def primeFactors(num: int) -> list:
    num = int(num)
    if clever(num):
        return [num]
    for i in range(2, math.floor(num**(0.5)) + 1):
        if num % i == 0 and clever(i):
            prior = primeFactors(int(num/i))
            prior.append(i)
            return prior


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
