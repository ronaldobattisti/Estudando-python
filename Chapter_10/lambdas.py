'''
known by lambda expression are funcions wo name os anonimous function
'''

#a function in python
def sum(x):
    return 3 * x + 1

print(sum(4))
####1
#lambda/input parameter/return
lambda x: 3 * x + 1 #anonimous funct
#How to use?
calc = lambda x: 3 * x + 1

print(calc(4))#just to understand how ir works

####2
#we can have lamb with multiple inputs
complete_name = lambda name, surname: name.strip().title() + ' ' + surname.strip().title()
print(complete_name(' ronaldo ','BATTISTI  '))

####3
#LAMBDA WO INPUT
love = lambda :'How not to love python'
une = lambda x: 3 * x + 1
print(love())
print(une(6))#more arguments than parametes = TypeError

####4
authors = ['Isaac Asimov', 'Ronaldo Battisti', 'Marcelo Paiva', 'Clarice Lispector',
           'Douglas Adams', 'H. G. Walls', 'Arthur C. Clarke']
print(authors)
authors.sort(key=lambda surname: surname.split(' ')[-1].lower())
print(authors)

####5
def quadratic_function(a, b, c):
    return lambda x : a * x ** 2 + b * x + c

print(quadratic_function(2, 3, -5)(2))#value of lambda in a diffrent parentheses
