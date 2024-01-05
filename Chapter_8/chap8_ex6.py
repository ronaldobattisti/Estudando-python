def convert_sec(sec, hour, min):
    return sec + min*60 + hour*3600

hour = 1
minute = 1
second = 1

print(convert_sec(hour, minute, second))