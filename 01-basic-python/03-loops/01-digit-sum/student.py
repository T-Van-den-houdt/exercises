# Write your code here
def last_digit(n):
    return int(str(n)[-1])

def remove_last_digit(n):
    if n > 9:
        return int(str(n)[:-1]) 
    else:
        return 0

def digit_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum