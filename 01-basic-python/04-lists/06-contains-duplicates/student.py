# Write your code here
def contains_duplicates(xs):
    new_list = []
    for i in xs:
        if i not in new_list:
            new_list.append(i)
        else:
            return True
    return False