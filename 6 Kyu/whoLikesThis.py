def likes(name):
    result = ""

    if len(name) == 0:
        result = "no one likes this"
    elif len(name) == 1:
        result = f"{name[0]} likes this"
    elif len(name) == 2:
        result = f"{name[0]} and {name[1]} like this"
    elif len(name) == 3:
        result = f"{name[0]}, {name[1]} and {name[2]} like this"
    else:
        result = f"{name[0]}, {name[1]} and {len(name) - 2} others like this"
    
    return result


print(likes(['Muneer']))
print(likes(['Muneer', 'Alex']))
print(likes(['Muneer', 'Alex', 'Alam']))
print(likes(['Muneer', 'Alex', 'Alam', 'Unknown']))
print(likes(['Muneer', 'Alex', 'Alam', 'Unknown', 'Steve']))