"""
POO - Properties

In POO languages as JAva, when we declare private atrtibutes, we use to create publoc methods to manupulate the, known as getters and setters
"""

# before improove
"""
class Account:
    count = 0

    def __init__(self, owner, balance, limit):
        self._number = Account.count + 1
        self._owner = owner
        self._balance = balance
        self._limit = limit
        Account.count += 1

    def statement(self):
        return f"statement = {self._balance} from {self._owner}"

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self.balance -= value

    def transfer(self, value, target):
        self._balance -= value
        target._balance += value

    def get_number(self):
        return self._number

    def get_owner(self):
        return self._owner

    def get_balance(self):
        return self._balance

    def get_limit(self):
        return self._limit

    def set_limit(self, limit):
        self._limit = limit


account1 = Account('Ronaldo', 3000, 5000)
account2 = Account('Daniela', 2000, 4000)

print(account1.statement())
print(account2.statement())

print(account2.__dict__)
account2.set_limit(99999999)
print(account2.__dict__)
"""


class Account:
    count = 0

    def __init__(self, owner, balance, limit):
        self._number = Account.count + 1
        self._owner = owner
        self._balance = balance
        self._limit = limit
        Account.count += 1

    @property
    def number(self):
        return self._number

    @property
    def number(self):
        return self._number

    @property
    def balance(self):
        return self._balance

    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, limit):
        self._limit = limit

    def statement(self):
        return f"statement = {self._balance} from {self._owner}"

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self.balance -= value

    def transfer(self, value, target):
        self._balance -= value
        target._balance += value

    @property
    def total_valie(self):
        return self._limit + self._balance


account1 = Account('Ronaldo', 3000, 5000)
account2 = Account('Daniela', 2000, 4000)

print(account1.statement())
print(account2.statement())

sum = account1.balance + account2.balance

print(sum)

print(account2.limit)
account2.limit = 99999999
print(account2.limit)

print(account1.total_valie)
print(account2.total_valie)
