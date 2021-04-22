def get_middle1(s): #My way
    length = len(s)
    
    if length % 2 == 0:
        return s[int(length / 2) - 1 : int((length / 2) + 1)]
    else:
        return s[int((length - 1) / 2)]

def get_middle2(s): #Shorter way
   return s[int((len(s)-1)/2) : int(len(s)/2+1)]


value = input('Give the input here: ')
print(get_middle1(value))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(get_middle2(value))