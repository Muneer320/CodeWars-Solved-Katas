def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for x in range(0, len(spl)):
        while (x < len(spl)):    
            if (len(spl[x]) > longest): 
                longest = len(spl[x])
            break
    return longest

print('Started!')
print(find_longest('It is the longest string ever in the history of earth ;)'))