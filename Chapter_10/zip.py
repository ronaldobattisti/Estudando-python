'''
zip() -> create a iterable caller zip objet that adds eny ellement from iterable as pairs
'''

list1 = [1, 2, 3]
list2 = [4, 5, 6]
zip1 = zip(list1, list2)

print(zip1)#Useless
print(type(zip1))#type zip, we need to convert to list
print(list(zip1))

print(dict(zip([1, 2, 3], [4, 5, 6])))#returns {1: 4, 2: 5, 3: 6}

zip1 = zip(list1, list2, 'ab')#return [(1, 4, 'a'), (2, 5, 'b')]
print(list(zip1))

list3 = [7, 8, 9, 10, 11]

#creater a iterable with the sze of the shortest list
zip3 = zip(list1, list2, list3)
print(list(zip3))

#wu can use different iterable

tuple1 = 1, 2, 3, 4, 5
list1 = [6, 7, 8, 9, 10]
dic1 = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tuple1, list1, dic1.values())
print(list(zt))

#tuples list
data = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*data)))#* = unpacking

#more complex exempler
test1 = [80, 91, 78]
test2 = [98, 89, 53]
names = ['ronaldo', 'daniela', 'cassio']

final = {data[0]:max(data[1], data[2]) for data in zip(names, test1, test2)}

print(final)

#we can use map
final = zip(names, map(lambda note: max(note), zip(test1, test2)))
print(dict(final))