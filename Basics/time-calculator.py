'''time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))'''

def add_time(second1, minute1, hour1, day1, second2, minute2, hour2, day2):
    seconds = second1 + second2
    minutes = minutes1 + minutes2
    hours = hour1 + hour2
    days = day1 + day2
    if seconds = 60:
        minutes = minutes + 1
    if seconds > 60:
        minutes = minutes + 1
        seconds = seconds - 60
    if minutes = 60:
        hours = hours + 1
    if minutes > 60:
        hours = hours + 1
        minutes = minutes - 60
    if hours = 24:
        days = days + 1
    if hours > 24:
        days = days + 1
        hours = hours + 24
