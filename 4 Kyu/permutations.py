import itertools


def permutations1(lst): #My code using pure code

    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i+1:]

        for p in permutations1(remLst):
            l.append(m + p)

    l = list( dict.fromkeys(l) )

    return l

def permutations2(string): #Shortest code using library
    return list("".join(p) for p in set(itertools.permutations(string)))


print(permutations1('aabb'))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(permutations2('aabb'))