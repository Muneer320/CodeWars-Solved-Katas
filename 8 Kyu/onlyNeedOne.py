def check1(a, v):
    for x in a:
        if x == v:
            return True
    return False

def check2(seq, elem):
    return elem in seq

check3 = lambda a, v: v in a

from operator import contains as check4

print(check1(['23','4',34,'234'], 34))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(check2(['23','4',34,'234'], 34))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(check3(['23','4',34,'234'], 34))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(check4(['23','4',34,'234'], 34))