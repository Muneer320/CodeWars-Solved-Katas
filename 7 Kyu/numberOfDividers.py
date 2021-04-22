def divisors1(n):
    i = 1
    d = []
    while i <= n :
        if (n % i==0) :
            d.append(i)
        i = i + 1
    return len(d)

def divisors2(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)


print(divisors1(34546))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(divisors2(34546))