'''
reduce

It in no more a integred function(not a built in function) - need lib

99% of the time a loop for is more legible


#####Imagine a data collection:

data = [a1, a2, a3, ..., an]

def funct(x, y):
return x * y

Just like map() and filter(), reduce() recieves two parameters -> a function and a iterable

reduce(funct, data)

STP1: res1 = f(a1, a2) # apply the funct in the two firt ellements in the collection and save the result
STP2: res2 = f(res1, a3) # apply the funct with the result of STP1 plus 3rd ellement and save res2

STP3: res3 = f(res2, a4)

#each step it apply the funct sending as argument the result of the previous application. Reduce returns a final result

###alternatively:

'''

from functools import reduce

#how it works:

#lets use reduce tu multiply all numbers of a list

data = [2, 3, 4, 5, 7, 11, 13 ,17, 19, 23, 29]
#to use reduce, we need a funct that recieves 2 parametes
mult = lambda x, y: x * y
res = reduce(mult, data)
print(res)


