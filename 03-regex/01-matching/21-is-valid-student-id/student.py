# Write your code here
import re

def is_valid_student_id(string):
    return re.fullmatch("^(r|s|R|S)\d{7}", string)