"""
Manipulating date and time

"""
import datetime

# print(dir(datetime))
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.datetime.now())

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))

start = datetime.datetime.now()

print(start)

start = start.replace(hour=16, minute=0, second=0, microsecond=0)

print(start)

event = datetime.datetime(2025, 1, 1, 0)

print(type(event))

print(event)
"""
aniversary = input("Wirite your bith date:(dd/mm/yyyy) ")
aniversary = aniversary.split('/')
aniversary = datetime.datetime(
    int(aniversary[2]), int(aniversary[1]), int(aniversary[0]))
print(aniversary)
print(type(aniversary))
"""
# individual acess to date and hour
print(event.year)
print(event.month)
print(event.day)
