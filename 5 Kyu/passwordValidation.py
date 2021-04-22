import string

def varify(pswd):
    
    for letter in pswd:
        if letter in string.ascii_uppercase:
            print('upper is available')
            if letter in string.ascii_lowercase:
                print('lower is available')
                if letter in string.digits:
                    print('num is available')
                    return True

print(varify('Muneer320'))