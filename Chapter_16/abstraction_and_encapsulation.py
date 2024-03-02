"""
POO - Abstraction and ancapsulation

The great objective of POO is encapsulate our code inside a logic and hierarchical group using classes

Encapsulate
           Class
|----------------------------|
|known attributes and methods|
|----------------------------|

#rememberig private methods and attributes in python

Exemple: acessing private ellements out of "People" class

instance._People__name

instance._People__speak() #wrong acess but python doesn't block

#Abstraction in POO is the act of expose just relevant data of a class hidding private attributes an methods from user

"""

"""These way the security is very weak
class Account:

    count = 400

    def __init__(self, name, balance, limit):
        self.number = Account.count + 1
        self.name = name
        self.balance = balance
        self.limit = limit
        Account.count = self.number

    def statement(self):
        print(
            f"statement of {self.balance} of {self.name} with limit {self.limit}")

    def deposit(self, value):
        self.balance = self.balance + value

    def withdraw(self, value):
        self.balance = self.balance - value

acc1 = Account('Ronaldo Battisti', 2000, 10000)

print(acc1.number)
print(acc1.name)
print(acc1.balance)
print(acc1.limit)

acc1.balance = 9999999999999
print(acc1.__dict__)

acc1.statement()

"""


class Account:

    count = 400

    def __init__(self, name, balance, limit):
        self._number = Account.count + 1
        self._name = name
        self._balance = balance
        self._limit = limit
        Account.count = self._number

    def statement(self):
        print(
            f"statement of {self._balance} of {self._name} with limit {self._limit}")

    def deposit(self, value):
        self._balance = self._balance + value

    def withdraw(self, value):
        self._balance = self._balance - value

    def transfer(self, value, destiny_account):
        # 1->Remove value from origin account
        self._balance -= value
        # 2->Add value to origin account
        destiny_account._balance += value


acc1 = Account('Ronaldo Battisti', 200, 1000)
acc1.statement()
acc2 = Account('Daniela Donida', 5000, 20000)
acc2.statement()

value = 100

print(acc1.__dict__)
print(acc2.__dict__)

acc2.transfer(100, acc1)

print(acc1.__dict__)
print(acc2.__dict__)

""" Working fine
print(acc1.__dict__)

acc1.withdraw(150)

print(acc1.__dict__)
"""
