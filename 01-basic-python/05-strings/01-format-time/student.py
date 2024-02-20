# Write your code here
def format_time(hours, minutes, seconds):
    if hours <= 9:
        i = "0"
    else:
        i = ""
    if minutes <= 9:
        j = "0"
    else: 
        j = ""
    if seconds <= 9:
        k = "0"
    else:
        k = ""
    return (f"{i}{hours}:{j}{minutes}:{k}{seconds}")