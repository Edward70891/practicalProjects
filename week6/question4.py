decypherbook = {'0000': 8, '0001': 1, '0010': 0, '0011': 9, '0100': 5, '0101': 3, '0110': 7, '0111': 2, '1110': 4, '1111': 6}

cypherbook = {8: '0000', 1: '0001', 0: '0010', 9: '0011', 5: '0100', 3: '0101', 7: '0110', 2: '0111', 4: '1110', 6: '1111'}


def encode(cypher, number):
    output = ""
    for digit in str(number):
        try:
            output += (cypher[int(digit)])
        except KeyError:
            print("Non - digit input!")
    return output


def decode(cypher, encrypted):
    if len(encrypted) % 4 != 0:
        raise ValueError("The length of the encrypted binary string must be a multiple of 4!")
    output = ""
    for i in range(3, len(encrypted), 4):
        decryptedDigit = cypher[encrypted[i - 3:i + 1]]
        output += str(decryptedDigit)
    return output


def dictSwap(dictionary):
    swapped = dict((v, k) for k, v in dictionary.iteritems())
    return swapped


def advancedEncode(cypher, number):
    output = ""
    for digit in str(number):
        try:
            output += (cypher[int(digit)])
        except KeyError:
            print("Non - digit input!")
    return output


def advancedDecode(cypher, encrypted):
    cypher = dictSwap(cypher)
    if len(encrypted) % 4 != 0:
        raise ValueError("The length of the encrypted binary string must be a multiple of 4!")
    output = ""
    for i in range(3, len(encrypted), 4):
        decryptedDigit = cypher[encrypted[i - 3:i + 1]]
        output += str(decryptedDigit)
    return output


print(encode(cypherbook, "12"))
print(decode(decypherbook, "00000110"))
