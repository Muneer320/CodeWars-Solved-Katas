def lovefunc1( flower1, flower2 ): #My Code
    
    
    if flower1 % 2 == 0:
        if flower2 % 2 != 0:
            return True
    
    elif flower1 % 2 != 0:
        if flower2 % 2 == 0:
            return True

    return False

def lovefunc2( flower1, flower2 ): #Shortest code
    return flower1 % 2 != flower2 % 2


print(lovefunc1(8 ,7))
print(lovefunc1(7 ,10))
print(lovefunc1(7 ,7))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(lovefunc2(8 ,7))
print(lovefunc2(7 ,10))
print(lovefunc2(7 ,7))