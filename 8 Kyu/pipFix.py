def pipe_fix1(nums):
    result = []

    for x in range(nums[0], nums[len(nums) - 1] + 1):
        result.append(x)
    
    return result

def pipe_fix2(nums):
    return list(range(nums[0], nums[-1] + 1))

print(pipe_fix1([1, 3, 6, 8, 11]))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(pipe_fix2([1, 3, 6, 8, 11]))