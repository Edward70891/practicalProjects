def is_power(a, b):
    if a == 0 or b == 0 or (b == 1 and b != a):
        return False
    elif a == b or a == 1:
        return True
    elif a % b == 0:
        return is_power(int(a/b), b)
    else:
        return False


def rec_sum(numbers):
    if type(numbers) is not list:
        raise TypeError("numbers is not a list!")
    elif len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return int(numbers[0])
    else:
        return int(numbers[0] + rec_sum(numbers[1:]))


def sum_all(numbers):
    if len(numbers) == 0:
        return 0
    elif type(numbers[0]) is list:
        return sum_all(numbers[0]) + sum_all(numbers[1:])
    elif len(numbers) == 1:
        return int(numbers[0])
    else:
        return int(numbers[0] + sum_all(numbers[1:]))


def flatten(mlist):
    current = mlist[0]
    remainder = mlist[1:]
    if type(remainder) is not list:
        remainder = [remainder]
    if type(current) is list:
        return flatten(current).extend(flatten(remainder))
    elif len(mlist) == 1:
        return list(current)
    else:
        return list(current).extend(flatten(remainder))

