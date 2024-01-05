from collections import namedtuple
tuple1 = (1, 2, 3)
print(type(tuple1))
print(tuple1[1])

'''
Named tuple -> tuples whith name and parameter specified
'''


# define name and parameters

# 1 - declarations
dog1 = namedtuple('dog', 'age race name')

# 2 - declaraiom
dog2 = namedtuple('dog', 'age, race, name')

# 3 - declaration
dog3 = namedtuple('dog', ['age', 'race', 'name'])


# using
ray = dog3(age=2, race='Vira latas', name='Ray')
print(ray)
# acessing data
# 1
print(ray[0])  # print just Ray's age
# 2
print(ray.age)
