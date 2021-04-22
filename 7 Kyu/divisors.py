def divisors1(integer): #My code
    integer = (int(integer))
    l = []
    
    for i in range(2,integer):
        if integer % i == 0:
            l.append(i)
    
    if l:
        return l
    else:
        return f"{integer} is prime"

def divisors2(n): #Shortest Code
    n = int(n)
    return [i for i in range(2, n) if not n % i] or '%d is prime' % n

print(divisors1('23'))
print(divisors1('13'))
print(divisors1('50'))
print(divisors1('1024'))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(divisors2('23'))
print(divisors2('13'))
print(divisors2('50'))
print(divisors2('1024'))