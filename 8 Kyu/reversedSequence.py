def reversed1(n):
    result = []

    for x in range(1, n + 1):
        result.insert(0, x)
    
    return result

def reversed2(n):
    return list(range(n, 0, -1))


print(reversed1(4))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(reversed2(4))