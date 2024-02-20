"""
Higher Order Functions - HOF

What does that means?

- When a lenguage let we use HOF, it indicates that we can have functions that return
 other functions as result ou throw a function as argument to another function, or ever 
 create a variable of the function kind
"""

#exemple - defining functions
def som(a, b):
    return a + b

def dim(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

def calculate(num1, num2, function):
    return function(num1, num2)

#testing

print(calculate(4, 3, som))

print(calculate(4, 3, dim))

print(calculate(4, 3, mul))

print(calculate(4, 3, div))

#Nested functions
"""
In python we also can have a function inside a function
"""

#returning functions from other functions
from random import choice

def make_me_laught():
    def laught():
        return choice(('hahahaha', 'kkkkkkkkkkk', 'jajajajaja'))
    return laught

laughting = make_me_laught()

print(laughting)

#inner functions or nested functions can acess the scope os external function
