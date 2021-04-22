def generate_hashtag1(s): #My code
    
    a = s.lower().split()
    result = '#'

    for word in a:
            word = word[0].capitalize() + word[1:]
            result = result + word
    
    if len(a) == 0:
        return False
    
    elif len(result) > 140:
        return False

    else:
        return result 

def generate_hashtag2(s): #Shortest Code
    return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False

print(generate_hashtag1("I loVe to code!"))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(generate_hashtag2("I loVe to code!"))