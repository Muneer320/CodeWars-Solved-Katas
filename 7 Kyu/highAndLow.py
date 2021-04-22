def high_and_low(numbers):
    nn = [int(s) for s in numbers.split()]
    return "%i %i" % (max(nn),min(nn))


print(high_and_low('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'))