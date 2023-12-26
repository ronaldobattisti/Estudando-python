'''
-Refeers to math set theory

-Can't have duplicate value
-Don't have ordenated value
-can't be acessed by index - aren't indexed

Are good when need to store ellements that don't need order and could have duplicated keys values and items
{sets} are referencied with keys {}

sets    maps(dictionaries in python)
value   keys/value
'''

# sets
# 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Have duplicated value
print(s)  # don't print duplicated values***
print(type(s))
# 2 - most commom
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# can conver string, list, tuple to a set

if 9 in s:
    print('Have 9')
else:
    print('Don\'t have 3')

# besides don't have duplicated values, don't have order
list1 = [99, 2, 34, 23, 12, 1, 44, 5]
set1 = {99, 2, 34, 23, 12, 1, 44, 5}
