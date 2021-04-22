from collections import Counter

def mix(s1, s2):
    c1, c2 = [Counter({s: n for s, n in Counter(c).items() if n > 1 and s.islower()}) for c in (s1, s2)]
    return '/'.join(c + ':' + -n * s for n, c, s in
                    sorted((-n, '=12'[(c1[s] == n) - (c2[s] == n)], s) for s, n in (c1 | c2).items()))



s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
print(mix(s1, s2))