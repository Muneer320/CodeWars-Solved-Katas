def is_triangle1(a, b, c): #My code
    
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if c + b <= a:
        return False

    else:
        return True

def is_triangle2(a, b, c): #Shortest code
    return (a<b+c) and (b<a+c) and (c<a+b)

print(is_triangle1(2,5,4))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(is_triangle2(2,5,4))