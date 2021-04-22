def is_vow1(inp): #My code
    
    for key in inp:

        if key == 97:
            index = inp.index(key)
            inp.remove(key)
            inp.insert(index, 'a')
        elif key == 101:
            index = inp.index(key)
            inp.remove(key)
            inp.insert(index, 'e')
        elif key == 105:
            index = inp.index(key)
            inp.remove(key)
            inp.insert(index, 'i')
        elif key == 111:
            index = inp.index(key)
            inp.remove(key)
            inp.insert(index, 'o')
        elif key == 117:
            index = inp.index(key)
            inp.remove(key)
            inp.insert(index, 'u')
        
    return inp

def is_vow2(inp): #Shortest Code
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]

print(is_vow1([118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113, 114, 113, 120, 106]))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(is_vow2([118, 117, 120, 121, 117, 98, 122, 97, 120, 106, 104, 116, 113, 114, 113, 120, 106]))