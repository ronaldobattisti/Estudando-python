"""
POO - attributes

Attributes represent the object characteristics
With attributes we can represent computationally the object states

In python, we divide attributes in 3 groups
    - instance attributes;
    -Class attribute
    -Dinamic attribute

In python it was conventioned that ALL CLASS ATTRIBUTE is public, if we want to threat a attribute as private(used just inside the class), 
use __ in the begining of the name -> NmeMangling(class._ClassName.__protectedattribute)
"""

# Instance attribute: are attributes declared inside the builder method
# Builder method is a method responsable for the object building


class Lampada:

    # this init is a method. If this function is outside the class, it will be just a function
    def __init__(self, voltage, color):
        self.voltage = voltage  # this self means that whan you instance a object with a class,
        self.color = color  # the instanced object will have it owns characteristics
        self.on = False  # the word "self" is a convention and it's not nedded to be "self"


class CurrentAccount:

    def __init__(self, number, limit, balance):
        self.number = number
        self.limit = limit
        self.balance = balance


"""
class Product:

    def __init__(self, name, desc, value):
        self.name = name
        self.desc = desc
        self.value = value
"""


class user:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Teste:

    def __init__(airplane, name):
        airplane.name = name


class Acess:

    def __init__(self, email, password):
        self.email = email
        self.__password = password

    def show_email(self):
        print(self.email)

    def show_password(self):
        print(self.__password)
# it is just a convention, python will let us acess these attributes
# ex


user = Acess('ronaldo@gmail.com', '123465')

print(user.email)
# print(user.__password)         #Attribute error
print(user._Acess__password)  # We have acess, but we shouldn't do it


################ Instance attributes####################
# What instance attribute means: It means that when we create a class instance, all instances will have these attributes
user1 = Acess('user1@gmail.com', '123456')
user2 = Acess('user2@gmail.com', '654321')

user1.show_email()
user1.show_password()
user2.show_email()
user2.show_password()

################ Class atributes################
"""
p1 = Product('ps 4', 'Videogame', 2300.0)
p2 = Product('xbox S', 'Videogame', 4500.0)
"""

# Clas attributes are directy declared in the class(out of the builder)

# refactoring th procuct class:


class Product:

    # Class attribute:
    tax = 1.05  # 0.05%
    cont = 0

    def __init__(self, name, desc, value):
        self.id = Product.cont + 1
        self.name = name
        self.desc = desc
        self.value = value * Product.tax
        Product.cont = self.id


p1 = Product('ps 4', 'Videogame', 2300.0)
p2 = Product('xbox S', 'Videogame', 4500.0)
"""
print(p1.tax)  # possible but incorrect
print(p2.tax)
print(p1.value)
print(p2.value)
print(p1.id)
print(p2.id)

# we dont need do acess a instance to acess a class attribute
print(Product.tax)  # correct way to acess
"""
################# Dinamic attributes#######################
# a instance attribute that can be created in execution time
# the dinamic attribute is exclusive for the instance that creates it

p1 = Product('ps 4', 'Videogame', 2300.0)
p2 = Product('xbox S', 'Videogame', 4500.0)

# Creating a dinamic attribute in execution time
p2.weight = '5kg'  # not common

print(p2.weight)

print(p1.__dict__)
print(p2.__dict__)

del p2.weight

print(p1.__dict__)
print(p2.__dict__)
