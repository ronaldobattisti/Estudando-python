'''
Dictionary comprehension

to create a dict:
dict = {'a' : 1, 'b' : 2, 'c' : 3}

#sintaxe
{key:value for value in iterable}
'''

#ex1
dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
sqr = {key : value ** 2 for key, value in dict.items()}
print(sqr)

#ex2
numbers = [1, 2, 3, 4, 5]#could be a tuple or a set too
sqr = {value : value **2 for value in numbers}
print(sqr)

#ex3 - mixing str w list
keys = 'abcde'
values = [1, 2, 3, 4, 5]
mix = {keys[i]:values[i] for i in range(0, len(keys))}
print(mix)

#ex4 - cond logic
res = {num:('even' if num % 2 == 0 else 'odd') for num in numbers}
print(res)