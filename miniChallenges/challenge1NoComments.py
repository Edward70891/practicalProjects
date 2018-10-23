import math


primesDict = {2: True}


def advanced(num):
    prime = True
    for i in range(2, math.floor(num**(0.5)) + 1):
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
        print("Largest prime factor found at " + str(num) + ", terminating...")
        return [num]
    for i in range(2, math.floor(num**(0.5)) + 1):
        if num % i == 0 and clever(i):
            print("Found the lowest prime factor at " + str(i))
            print("Calling prime factors with " + str(int(num/i)))
            prior = primeFactors(int(num/i))
            print("primeFactors terminated with " + str(prior.append(i)))
            return prior.append(i)


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
