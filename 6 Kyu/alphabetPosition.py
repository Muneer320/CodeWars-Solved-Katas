import string
def alphabet_position1(text):
    alphabets = {v: k for k, v in enumerate(string.ascii_lowercase, start=1)}
    return " ".join(str(alphabets.get(char)) for char in text.lower() if char in alphabets.keys())

def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

a = input('Give your Input: ')
print(alphabet_position1(a))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(alphabet_position2(a))