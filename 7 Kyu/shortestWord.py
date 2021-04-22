def find_short1(s): # My COde
    words = s.split()
    length = []

    for word in words:
        a = len(word)
        length.append(a)
    
    return min(length)
        
def find_short2(s): #Shortest Code
    return min(len(x) for x in s.split())


print(find_short1('Hi I am Muneer alam how are you hope you are good ;)'))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(find_short2('Hi I am Muneer alam how are you hope you are good ;)'))