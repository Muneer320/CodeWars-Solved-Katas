def even_binary(s):
    s = s.split()
    e = sorted(filter(lambda b: b[-1]=='0', s), reverse=True)
    return ' '.join(map(lambda b: e.pop() if b[-1]=='0' else b, s))

print(even_binary('123 432 754 345 556 100'))