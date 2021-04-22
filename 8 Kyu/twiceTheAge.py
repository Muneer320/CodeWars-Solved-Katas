def twice_as_old1(f, s):
    age = str((s * 2) - f)
    if "-" in age:
        return int(age[1:])
    return int(age)

def twice_as_old2(f, s):
    return abs(f - 2*s)

twice_as_old3 = lambda f,s: abs(f - 2*s)
    


print(twice_as_old1(88, 53))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(twice_as_old2(88, 53))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(twice_as_old3(88, 53))