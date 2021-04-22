def larger_pow(x):
    t = 1
    while t < x:
        t <<= 1
    return t

def range_sum(l, r):
    return (l + r) * (r - l + 1) // 2
    
def elder_age1(m,n,l,t):
    if m == 0 or n == 0:
        return 0
    if m > n:
        m, n = n, m
    lm, ln = larger_pow(m), larger_pow(n)
    if l > ln:
        return 0

    if lm == ln:
        return (range_sum(1, ln - l - 1) * (m + n - ln) + elder_age1(ln - n, lm - m, l, t)) % t
    
    if lm < ln:
        lm = ln // 2
        tmp = range_sum(1, ln - l - 1) * m - (ln - n) * range_sum(max(0, lm - l), ln - l - 1)
        if l <= lm:
            tmp += (lm - l) * (lm - m) * (ln - n) + elder_age1(lm - m, ln - n, 0, t)
        else:
            tmp += elder_age1(lm - m, ln - n, l - lm, t)
        return tmp % t


def elder_age2(m,n,l,t,s=0):
    if m > n: m, n = n, m
    if m < 2 or not n & (n - 1): # n is a power of 2
        s, p = max(s-l, 0), max(n+s-l-1, 0)
        return (p - s + 1) * (s + p) // 2 * m % t
    p = 1 << n.bit_length() - 1 # Biggest power of 2 lesser than n
    if m < p: return (elder_age2(m, p, l, t, s) + elder_age2(m, n-p, l, t, s+p)) % t
    return (elder_age2(p, p, l, t, s) + elder_age2(m-p, n-p, l, t, s) +
            elder_age2(p, n-p, l, t, s+p) + elder_age2(m-p, p, l, t, s+p)) % t


print(elder_age1(8 ,5, 1, 100))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(elder_age2(8 ,5, 1, 100))