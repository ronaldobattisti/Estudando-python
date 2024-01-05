'''
List comprehension

- with these featura, we can generate new list with processed data with a iterable

[ data for data in iterable ]
'''

numbers = [1, 2, 3, 4, 5]

res = [num * 10 for num in numbers]
print(res)


def mult(a):
    return a*a


res2 = [mult(num) for num in numbers]
print(res2)

res3 = [num ** 2 for num in [1, 2, 3, 4, 5]]
print(res3)

name1 = 'ronaldo battisti'
print([letra.upper() for letra in name1])


def upper_case(name):
    name = name.replace(name[0], name[0].upper())
    return name


friends = ['ronaldo', 'anderson', 'daniela', 'maria', 'guilherme']
print([upper_case(friend) for friend in friends])

print([number * 3 for number in range(1, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(num) for num in [1, 2, 3, 4]])
