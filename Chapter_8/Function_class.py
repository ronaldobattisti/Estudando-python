'''
Defining functions

DRY - Don't Repeat Yourself

def funct_nam input_parameter():
    funct_block

Where:

-> funct_name       - ALWAYS lower case separated by underline
-> input_parameter  - Optional
-> funct_block      - Processing
'''

def diz_oi():
    print('Oi!')

diz_oi()

def happy_birthday():
    print('Happy birthday to you')

happy_birthday()

sing = happy_birthday #attribute a function to a variable - non commom

sing()

##heads or tails
from random import random
def flip_coin():
    n = random()
    if n > 0.5:
        return 'head'#don't need else because of the return
    return 'tail'

print(flip_coin())
