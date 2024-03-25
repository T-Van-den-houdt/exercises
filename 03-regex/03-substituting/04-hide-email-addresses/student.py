# Write your code here
import re

def hide_email_addresses(string):
    def replace(match):
        email = match.group(1)
        email = len(email) * '*'
        return email

    return re.sub(r'([a-zA-Z0-9.]+@[a-zA-Z0-9.]+)', replace, string)