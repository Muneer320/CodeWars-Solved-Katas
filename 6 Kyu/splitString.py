def solution(s):
    result = []

    while len(s) > 1:
        result.append(s[0:2])
        s = s[2:]
    if len(s) == 1:
        result.append(s + '_')
    
    return result

a = input('Give your Input: ')
print(solution(a))