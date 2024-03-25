import re

def parse_time(string):
    match = re.fullmatch(r'(\d{2}):([0-5]\d):([0-5]\d)(\.\d{3})?', string)

    if match:
        h, m, s, ms = match.groups('.000')
        h, m, s, ms = int(h), int(m), int(s), int(ms[1:])
        return (h, m, s, ms)
    return None
