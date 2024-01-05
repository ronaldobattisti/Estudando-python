'''
List comprehension

we can add ligic conditional structures
'''

#1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [number for number in numbers if number % 2 == 0]
print(even)

# if answer iz 0, false, if not false, than is true
even = [number for number in numbers if not number % 2]
print(even)

res = [number * 2 if number % 2 == 0 else number / 2 for number in numbers]
print(res)