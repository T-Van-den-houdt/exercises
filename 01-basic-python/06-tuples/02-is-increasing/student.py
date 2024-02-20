# Write your code here
def is_increasing(ns):
    ms = ns[1:]
    for i in list(zip(ms, ns)):
        if i[1] > i[0]:
            return False
    return True