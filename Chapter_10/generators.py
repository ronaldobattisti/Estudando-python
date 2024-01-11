'''
Generators

WE've studied:
- List Comprehension
- Dict comprehension
- set comprehensio

Didn't see tuple comprehension... they're called generators

We did:
names = ['Carlos', 'Carla', 'Cassiano']
print(any(name[0] == 'C' for name in names))#Return True
'''

names = ['Carlos', 'Carla', 'Cassiano']

print(any(name[0] == 'C' for name in names))#It's not a list comprehension
print(name[0] == 'C' for name in names)#It's not a list comprehension

print(any([name[0] == 'C' for name in names]))#It is a list comprehension
print([name[0] == 'C' for name in names])#It is a list comprehension

#doing this as list comprehension
res = [name[0] == 'C' for name in names]
print(type(res))
print(res)

#doing as list comprehension
res = (name[0] == 'C' for name in names)
print(type(res))#Generator - best performance
print(res)#exclude from memory after use

from sys import getsizeof as gso

print(gso('Geek'))#show how meny bites of memory the string is using
print(gso(''))

#generatig a number list with list comprehension
list_comprehension = gso([x * 10 for x in range(1000)])
#generatig a number list with set comprehension
set_comprehension = gso({x * 10 for x in range(1000)}) 
#generatig a number list with dictionarie comprehension
dict_comprehension = gso({x: x * 10 for x in range(1000)})
#generatig a number list with generator
gen_comprehension = gso(x * 10 for x in range(1000))


print(list_comprehension)
print(set_comprehension)
print(dict_comprehension)
print(gen_comprehension)

#Can I iterate in a generator?
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))
for num in gen:
    print(num)