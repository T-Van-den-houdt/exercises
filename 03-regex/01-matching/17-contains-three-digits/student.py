
# Write your code here
import re

def contains_three_digits(string):
    return re.fullmatch("(.*\d){3}", string)