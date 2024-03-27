"""

"""

import functools
import timeit
from textblob import TextBlob
import datetime

# with now wu can spacufy a timezone
now = datetime.datetime.now()
print(now)
print(type(now))
print(repr(now))

today = datetime.datetime.today()
print(today)
print(type(today))
print(repr(today))

print('----------------------------------')

# changes occuring middlenight

maintence = datetime.datetime.combine(
    (datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(maintence)
print(type(maintence))
print(repr(maintence))

# today is thursday, this method returned 3 because 0-monday/1-tuesday/2-wednesday/3-thursday/...
print(maintence.weekday())

print('----------------------------------')

'''
anniversary = input('Write your burth date(dd/mm/yyyy): ')
an = anniversary.split('/')
an = datetime.datetime(year=int(an[2]), month=int(an[1]), day=int(an[0]))

if an.weekday() == 0:
    print("You were born in a monday")
elif an.weekday() == 1:
    print("You were born in a tuesday")
elif an.weekday() == 2:
    print("You were born in a wednesday")
elif an.weekday() == 3:
    print("You were born in a thursday")
elif an.weekday() == 4:
    print("You were born in a friday")
elif an.weekday() == 5:
    print("You were born in a saturday")
elif an.weekday() == 6:
    print("You were born in a sunday")
'''

print('----------------------------------')

# formating date hour with strftime()

today = datetime.datetime.today()
print(today)
f_today = today.strftime('%d/%m/%Y')
print(f_today)
f_today = today.strftime('%d/%m/%y')
print(f_today)
f_today = today.strftime('%d/%B/%y')
print(f_today)
f_today = today.strftime('%d/%b/%y')
print(f_today)
f_today = today.strftime('%d de %B de %y')
print(f_today)
# docs.python.org/3/library/datetime.html


def format_date(date):
    if date.month == 1:
        return (f"{date.day} de janeiro de {date.year}")
    elif date.month == 2:
        return (f"{date.day} de fevereiro de {date.year}")
    elif date.month == 3:
        return (f"{date.day} de março de {date.year}")
    elif date.month == 4:
        return (f"{date.day} de abril de {date.year}")
    elif date.month == 5:
        return (f"{date.day} de maio de {date.year}")
    elif date.month == 6:
        return (f"{date.day} de junho de {date.year}")
    elif date.month == 7:
        return (f"{date.day} de julho de {date.year}")
    elif date.month == 8:
        return (f"{date.day} de agosto de {date.year}")
    elif date.month == 9:
        return (f"{date.day} de setembro de {date.year}")
    elif date.month == 10:
        return (f"{date.day} de outubro de {date.year}")
    elif date.month == 11:
        return (f"{date.day} de novembro de {date.year}")
    elif date.month == 12:
        return (f"{date.day} de dezembro de {date.year}")


print(format_date(today))

"""
def format_blob_date(date):
    blob_month = TextBlob(date.strftime('%B'))
    print(blob_month)
    return f"{date.day} de {blob_month.translate(to='pt-br')} de {date.year}"

print(format_blob_date(today))
"""

print('----------------------------------')

born = datetime.datetime.strptime('02/12/1996', '%d/%m/%Y')
print(born)

"""born = input('Write your birth date(dd/mm/yyyy):')
birth = datetime.datetime.strptime(born, '%d/%m/%Y')

print(birth)
"""
print('----------------------------------')

# to work just with hour

lunch = datetime.time(12, 30, 0)

print(lunch)

print('----------------------------------')


# execution time with timeit

# loop for
time = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(time)
# list comprehension
time = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(time)
# map
time = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(time)

print('----------------------------------')


def test(n):
    sum = 0
    for num in range(n * 200):
        sum = sum + num ** num + 4
    return sum


print(test(5))

# similar to timeit, but uses a function as inout
print(timeit.timeit(functools.partial(test, 2), number=10000))
