def encode1(s):
    code = {'a': 1,'e':2,'i':3,'o':4,'u':5}
    for letter in s:
        if letter in code:
            s = s.replace(letter, str(code[letter]))
    return s

def decode1(s):
    code = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u',}
    for letter in s:
        if letter in code:
            s = s.replace(letter, str(code[letter]))
    return s


def encode2(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def decode2(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)


print(encode1('Hello how are you!'))
print(decode1('H2ll4 h4w 1r2 y45!'))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(encode2('Hello how are you!'))
print(decode2('H2ll4 h4w 1r2 y45!'))