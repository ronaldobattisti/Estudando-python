"""len() -> return the lenght of a iterable"""
#len() works there way:
#dunder len (dunder = double underline)
print('Geek University'.__len__())

"""abs() -> return the integer number"""
print(abs(-1))

"""sum() -> get a iterable as parameter and return the whole sum"""
#default initial value = 0
print(sum([1, 2, 3, 4, 5]))#return 15
print(sum([1, 2, 3, 4, 5], 5))#eturn 20 because starts with 5
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

"""round() -> return the round number to n digit. If the precision is not setted, return the nearest number"""
print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.219999999, 2))