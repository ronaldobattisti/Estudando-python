"""
Difference between iterator and iterable

Iterator is a programming ellement that can be iterable
A object that returns a data being one element each time always ehan next() is used

Iterable
    Object that returns a iterator when funct iter() is called
"""

name = 'Geek'
numbers = [1, 2, 3, 4, 5, 6]
#Those are iterables - return a iterator

it1 = iter(name)
it2 = iter(numbers)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

for let in name:#under the covers, this function turns name a iterable and use next
    print(let)
