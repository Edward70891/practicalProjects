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


def advanced(num):
    prime = True
    for i in range(2, math.floor(num**(0.5))):
        if num % i == 0:
            prime = False
    return prime


def clever(num):
    if num in primesDict.keys():
        prime = True
    else:
        prime = advanced(num)
    if prime:
        primesDict[num] = True
    return prime


def primeFactors(num: int) -> list:
    num = int(num)
    if clever(num):
        return [num]
    for i in range(2, math.floor(num**(0.5))):
        if num % i == 0 and clever(i):
            return primeFactors(num/i).append(i)
    raise ValueError("primeFactors didn't find a prime factor!")


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
print("This was from the data: " + print(str(data[1])))
