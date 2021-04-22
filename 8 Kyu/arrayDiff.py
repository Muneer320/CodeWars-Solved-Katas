list1 = [1, 2, 2, 3, 4, 2, 6, 7]
list2 = [2]

def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff(list1, list2))