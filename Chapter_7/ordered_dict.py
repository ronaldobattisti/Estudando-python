'''

'''

from collections import OrderedDict

dic = {'a': 5, 'b': 2, 'e': 3, 'd': 4, 'c': 1}
print(dic)
# value isn't ordenable

for key, value in dic.items():
    print(f'key {key}: value {value}')

print('############')
dic2 = OrderedDict({'a': 5, 'b': 2, 'e': 3, 'd': 4, 'c': 1})
for key, value in dic2.items():
    print(f'key {key}: value {value}')

# understending difference between dict and ordereddict

d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}

print(d1 == d2)  # True

d3 = OrderedDict({'a': 1, 'b': 2})
d4 = OrderedDict({'b': 2, 'a': 1})

print(d3 == d4)  # False because order matters
