def christmasTree(n):
    for i in range(n):
        for j in range(n-i):
            print('', end=' ')
        for k in range(2*i+1):
            print('*',end='')
        print()

def christmas_tree(height: int) -> str:
    return '\n'.join(('*' * i).center(2 * height - 1) for i in range(1, height * 2, 2))


christmasTree(10)

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(christmas_tree(10))