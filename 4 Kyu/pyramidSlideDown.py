def longest_slide_down1(pyramid):
    pyramid[0][0] = [pyramid[0][0]]
    for i in range(1,len(pyramid)):
        for j in range(len(pyramid[i])):
            if j == 0:
                last_list = pyramid[i-1][j]
            elif j == len(pyramid[i]) - 1:
                last_list = pyramid[i-1][j-1]
            else:
                last_list = pyramid[i-1][j] + pyramid[i-1][j-1]
            new_list = []
            last = max(last_list)
            new_list.append(last + pyramid[i][j])
            pyramid[i][j] = new_list
    final = []
    for i in pyramid:
        for j in i:
            for k in j:
                final.append(k)
    return max(final)

def longest_slide_down2(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1])  for i in range(len(tmp))] 
    return res.pop()


print(longest_slide_down1([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(longest_slide_down2([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))