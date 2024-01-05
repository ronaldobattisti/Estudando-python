'''
set comprehension

same as list
'''
#ex1
numbers = {num for num in range(1,7)}
print(numbers)

#ex2
numbers = {num ** 2 for num in range(1, 7)}
print(numbers)
numbers = {num : num ** 2 for num in range(1, 7)}
print(numbers)

#ex3
letters = {letter for letter in 'Ronaldo Battisti'}
print(letters)