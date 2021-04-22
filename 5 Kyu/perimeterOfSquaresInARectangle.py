def perimeter(n):
    n = int(n)
    a, b = 1, 2
    while n:
        a, b, n = b, a + b, n - 1

    return 4 * (b - 1)

print(perimeter('5'))