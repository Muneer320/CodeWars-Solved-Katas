def sum_mix1(arr):
    result = 0
    for value in range(0, len(arr)):
        result = result + int(arr[value])
    return result

def sum_mix2(arr):
    return sum(map(int, arr))


print(sum_mix1([2,46,9,46,8,'5','47''8',4]))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(sum_mix2([2,46,9,46,8,'5','47''8',4]))