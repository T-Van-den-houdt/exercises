# Write your code here
def rotate(xs, n):
    j = 0
    for i in range(n, len(xs)):
        xs.insert(j, xs[i])
        xs.pop(i + 1)
        j += 1
    return xs