'''
Reversed

It's not reverse() funct

reversed function with eny iterable, not only list
'''

list1 = [1, 2, 3, 4, 5]
res = reversed(list1)

print(res)
print(type(res))
#Reversedfunct returns a iterable called list_reverseiterator, that we can conver to a known iterable like:
list(res)

for letter in reversed('Geek University'):
    print(letter, end='')#these command is to not jump a line between prints

print('\n')

print(''.join(reversed('Geek University')))#another way wo for

#using reversed() to invert a loop

for i in reversed(range(0, 10)):
    print(i)

for i in range(9, -1, -1):
    print(i)