"""
decorators with differenst signatures(different inpur parameters)

# to solve the 2 input function problem, we use a default parameter Decorator Patter

# a function signature is represented by it's return, name and input parameters
"""

def scream(function):
    def increase(name):
        return function(name).upper()
    return(increase)

@scream
def salutation(name):
    return f"Hello, I'm {name}"

@scream
def order(main, side):
    return f"I want {main} with {side}"

#testing

print(salutation("Ronaldo"))
print('------------------------')
'''print(order('tofu', 'letuga'))'''#type error

#######################################################
#########Refactorating with decorator pattern##########
#######################################################

def scream(function):
    def increase(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return increase

@scream
def salutation(name):
    return f"Hello, I'm {name}"

@scream
def order(main, side):
    return f"I want {main} with {side}"

print(salutation("Ronaldo"))
print('------------------------')
print(order('tofu', 'letuga'))

print(order(side='lettuce', main="meat"))

print('---------------------------------------------')

#Decorator with arguments

def verify_first_argument(value):
    def internal(function):
        def other(*args, **kwargs):
            if args and args[0] != value:
                return f"1st argument should be {value}"
            return function(*args, **kwargs)
        return other
    return internal

@verify_first_argument('pizza')
def favorite_food(*args):
    print(args)

@verify_first_argument(10)
def sum_ten(num1, num2):
    return num1 + num2

print(sum_ten(10, 12))

print(sum_ten(1, 21))#just let be if 1st argument is 10

print(favorite_food('pizza', 'barbes'))

print(favorite_food('sandwich', 'barbes'))#same as before