def toTime1(s):
    hour = 0
    minute = 0
    
    if s > 60:
        minute = int(s / 60)
    if minute > 59:
        hour = int(minute / 60)
        minute -= hour * 60


    return f'{hour} hour(s) and {minute} minute(s)'

def toTime2(seconds):
    return f'{seconds//3600} hour(s) and {seconds%3600//60} minute(s)'


print(toTime1(323550))

print("\n\n\t\t\t**********Alternate Way**********\n\n")

print(toTime2(323550))