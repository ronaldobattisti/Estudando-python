import math
from random import random

def fill(vec1):
    while len(vec1) < 10:
        i = math.ceil(random()*10)
        if not(i in vec1):
            vec1.append(i)
    return vec1

list1 = [1, 5, 9, 4, 10]
print(fill(list1))