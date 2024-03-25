
# Write your code here
import re

def only_letters(string):
    string = string.lower()
    return re.fullmatch('[a-z]*', string)