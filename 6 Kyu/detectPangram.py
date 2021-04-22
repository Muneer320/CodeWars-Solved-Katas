import string

def is_pangram1(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in s.lower(): 
            return False
  
    return True

def is_pangram2(s):
    return set(string.ascii_lowercase) <= set(s.lower())

if is_pangram1('Abcdefghi.j"kl"mnopqrstuvwxyz'):
    print('Yes, it is a pangram')
else:
    print('No, it is not a pangram')

print("\n\n\t\t\t**********Alternate Way**********\n\n")

if is_pangram2('Abcdefghi.j"kl"mnopqrstuvwxyz'):
    print('Yes, it is a pangram')
else:
    print('No, it is not a pangram')