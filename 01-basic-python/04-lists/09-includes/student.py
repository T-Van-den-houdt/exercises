# Write your code here
def includes(xs, ys):
    count = 0
    for i in ys:
        if i in xs:
            count += 1
    if count == len(ys):
        return True
    return False