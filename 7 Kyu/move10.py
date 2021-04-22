def move_ten(text, n=10):
    return ''.join(chr((ord(c) - ord('a') + n) 
        % 26 + ord('a')) for c in text)


print(move_ten('testcase'))
print(move_ten('test'))