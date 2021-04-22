def total_item(lst):
    result = {}

    dictItem = 0
    listItem = 0
    tupleItem = 0
    strItem = 0
    intItem = 0
    floatItem = 0
    boolItem = 0

    for item in lst:
        if type(item) is dict:
            dictItem += 1
            
        elif type(item) is list:
            listItem += 1

        elif type(item) is tuple:
            tupleItem += 1

        elif type(item) is str:
            strItem += 1

        elif type(item) is int:
            intItem += 1

        elif type(item) is float:
            floatItem += 1

        elif type(item) is bool:
            boolItem += 1


    if dictItem != 0:
        result.update(Dictionary = dictItem)
    if listItem != 0:
        result.update(List = listItem)
    if tupleItem != 0:
        result.update(Tupple = tupleItem)
    if strItem != 0:
        result.update(String = strItem)
    if intItem != 0:
        result.update(Integer = intItem)
    if floatItem != 0:
        result.update(Float = floatItem)
    if boolItem != 0:
        result.update(Boolean = boolItem)


    return result


print(total_item([1, 1.64, 'Hello', ['1', 9], ('1', 0.23), {1:'5', 'y': 7}, True]))
print(total_item([1, 1.64, 'Hello', ['1', 9], ('1', 0.23), True]))
print(total_item([1, 1.64, 'Hello', ['1', 9], True]))
print(total_item([1, 'Hello', ['1', 9], ('vd', '3')]))
print(total_item([]))