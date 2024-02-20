# Write your code here
def make_path(parts):
    string = ""
    for part in parts:
        string += part + "/"
    return string[:-1]