def snail1(array): #My code
    results = []
    while len(array) > 0:
        # go right
        results += array[0]
        del array[0]

        if len(array) > 0:
            # go down
            for i in array:
                results += [i[-1]]
                del i[-1]

            # go left
            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            # go top
            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results


def snail2(array): #Short Code
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out


print(snail1([[1,2,3],
             [2,5,9],
             [8,5,5]]))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(snail2([[1,2,3],
             [2,5,9],
             [8,5,5]]))