def get_count(input_str):
    input_str = input_str.lower()
    vowels = 'aeiou'
    num_vowels = 0
    for x in input_str:
        if x in vowels:
            num_vowels += 1
    
    return num_vowels


def get_count2(s):
    return sum(c in 'aeiou' for c in s)

print(get_count('nsqwertyuijhgfdsfghjhfdsasfghnbvcoiuyreoiuytrew'))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(get_count2('nsqwertyuijhgfdsfghjhfdsasfghnbvcoiuyreoiuytrew'))