'''
random modules and what are moduler

In python, modules are other python files

to use a module we need to install or import

random module -> have a lot of fuct to generate pseudo random numbers

-There are 2 ways to use
'''

#1st way - NOT RECOMMENDED
import random

#importing a module, all funct, attributes, classes and properties in the module will be disponible to use
#If you know what functions you need to use, that's not the best utilization

#dir(random)
i = random.random()
print(i)

#2nd way - importing a specific function from module
from random import random

#############################################################
#uniform() -> generate a pseudo random number between given values

from random import uniform
for i in range(10):
    print(uniform(3, 7))#7 is not included

#for integer numbers: randint()
from random import randint
for i in range(6):
    print(randint(1, 61), end = ', ')

# choice() -> shows a random value between a iterable
from random import choice

plays = ['rock', 'paper', 'scisor']
print(choice(plays))

#shuffle() -> to shuffle datas
from random import shuffle
cards = ['k', 'q', 'j', 'a', '2', '3', '4', '5', '6', '7']
print(cards)
shuffle(cards)
print(cards)