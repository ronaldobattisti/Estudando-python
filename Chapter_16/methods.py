"""
POO - methods

- Methods(functions) -> represent the object behavios, what actions it can do

In python we divide the methods in:
- Instance method:

- Class method:

the method __init__ is a builder method, and its function is to build a object from the class

The dunder ellements in puthon are called magic methods

Class method in python are static method in other lenguage
"""


from passlib.hash import pbkdf2_sha256 as cryp


class Lamp:
    def __init_(self, color, voltage, luminosity):
        self.__color = color
        self.__voltage = voltage
        self.__luminosity = luminosity
        self.__on = False


class CurrentAccount:

    counter = 4999

    def __init__(self, limit, balance):
        self.__number = CurrentAccount.counter + 1
        self.__limit = limit
        self.__balance = balance
        CurrentAccount.counter = self.__number


class Product:

    counter = 0

    def __init__(self, name, description, value):
        self.__id = Product.counter + 1
        self.__name = name
        self.__description = description
        self.__value = value
        Product.counter = self.__id

    def discount(self, percent):  # This is a method bacause it's inside a class
        """Return value with discount"""
        return (self.__value * (100 - percent)) / 100


"""
class User:
    def __init__(self, name, surname, email, password):
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = cryp.hash(password, rounds=200000, salt_size=16)

    def complete_name(self):
        return (f'{self.__name} {self.__surname}')

    def __run__(self, meters):  # not recommended
        # Because could change a native magic function and affect the system
        print(f"{self.__name} is running {meters} meters")

    def check_password(self, password):
        if cryp.verify(password, self.__password):
            return True
        return False
"""

p1 = Product('PS 4', 'Video Game', 2300)

print(p1.discount(20))

# print(Product.discount(20)) It's not possible because we are trying to reach no instanced object
# It's possible because we are sending p1 as self
print(Product.discount(p1, 20))

"""
user1 = User('Angelina', 'Jolie', 'angelinajolie@gmail.com', '123456')
user2 = User('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.complete_name())
print(user2.complete_name())

print(f'Password user 1: {user1._User__password}')  # Uncorrect acess to the attribute
print(f'Password user 2: {user2._User__password}')  # Uncorrect acess to the attribute
"""
"""
name = input("input name: ")
surname = input("inout surname: ")
email = input("Input email: ")
password = input("Input password: ")
conf_password = input("Confirm password: ")

if password == conf_password:
    user = User(name, surname, email, password)
else:
    print('Incorrect password')
    exit(42)

print('user created with sucess')

password = input("Input password")

if user.check_password(password):
    print("Acess allowed")
else:
    print("Acess denied")

print(f'Cript pass: {user._User__password}')
"""

# Class methods


class User:
    counter = 0

    # Class method
    @classmethod  # needed to create a class method
    def count_user(cls):  # Conventioned that cls is from class
        print(f"That/'s {cls.counter} user in the system")

    # Static method
    @staticmethod
    def definition():
        return 'asba456'

    def __init__(self, name, surname, email, password):
        self.__id = User.counter + 1
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__password = cryp.hash(password, rounds=200000, salt_size=16)
        User.counter = self.__id
        print(f"User created: {self.__generate_user()}")

    def complete_name(self):
        return (f'{self.__name} {self.__surname}')

    def __run__(self, meters):  # not recommended
        # Because could change a native magic function and affect the system
        print(f"{self.__name} is running {meters} meters")

    def check_password(self, password):
        if cryp.verify(password, self.__password):
            return True
        return False

    def see(self):
        print('Test')

    def __generate_user(self):
        return self.__email.split('@')[0]


"""
user = User('Ronaldo', 'Battisti', 'ronaldo@gmail.com', '123456')
User.count_user()  # Correct way because use the class name
user.count_user()  # incorrect

# when to use a method class or a instance method
# method class: When we don't need to acess instance(that's no self.something)
# instance class: when we neet to acess a instance


# if we want private methods, the method should start with double underline:
user = User('Ronaldo', 'Battisti', 'roba@gmail.com', '123456')

# print(user.__generate_user()) -> AttributeError
print(user._User___generate_user()) #Bad way to acess
"""

# Static method
print(User.counter)

print(User.definition())

user = User('Ronaldo', 'Battisti', 'rb@gmail.com', '123456')

print(user.counter)

print(user.definition())
