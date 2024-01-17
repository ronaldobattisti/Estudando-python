#integred modules that come with python

#using alias
import random as rdn

#importing all the functions
from random import *
import random
#they are diffrent, because in the first yu can use only random(), while in the second you use random.random()

#alias for function
from random import randint as rin, random as rdm
print(rin(5, 89))
print(rdm)

#importing many modules
from random import randint, shuffle, randrange
#we use to use tupple tu make many imports from the same module
from random import (
    randint,
    shuffle,
    randrange
)
#these way is more organized