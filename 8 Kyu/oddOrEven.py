def oddOrEven1(n):
    sum = 0
    for x in n:
        sum += x
    if sum % 2 == 1:
        return 'odd'
    else:
        return 'even'

def oddOrEven2(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

print(oddOrEven1([2,5,7,8]))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(oddOrEven2([2,5,7,8]))