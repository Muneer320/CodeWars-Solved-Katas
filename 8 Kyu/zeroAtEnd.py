def move_zeros1(array): #My Code

    for key in array:
        if key == 0:
            array.remove(key)
            array.append(key)

    return array

def move_zeros2(array): #Shortest Code
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

print(move_zeros1([1,3,4,7,0,0,0,0,53]))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(move_zeros2([1,3,4,7,0,0,0,0,53]))