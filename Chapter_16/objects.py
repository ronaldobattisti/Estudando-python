"""
POO - objects

Objects -> are class instances

After mapping a real life object to it's computationar represention, we can create as many objects are needed.
We can think in objects/instances of a class as variables of undefined type
"""


class Lamp:

    def __init__(self, color, voltage, luminosity):
        self._color = color
        self._coltage = voltage
        self._luminosity = luminosity
        self._on = False

    def check_lamp(self):
        return self._on

    def on_off(self):
        if self._on:
            self._on = False
        else:
            self._on = True


class CurrentAccount:

    counter = 499

    def __init__(self, limit, balance, client):
        self._number = CurrentAccount.counter + 1
        self._limit = limit
        self._balance = balance
        self._client = client
        CurrentAccount.counter = self._number

    def show_client(self):
        print(f"The client is {self._client._name}")

    '''def say(self):
        print(f"the client ")'''


class Client:

    def __init__(self, name, cpf):
        self._name = name
        self._cpf = cpf


class User:

    def __init__(self, name, surname, email, password):
        self._name = name
        self._surname = surname
        self._email = email
        self._password = password


lamp1 = Lamp('white', 110, 60)  # it' a instance/object

lamp1.on_off()

print(f'The lamp is on? {lamp1.check_lamp()}')

"""acc1 = CurrentAccount(5000, 20000)"""

user1 = User('Ronaldo', 'Battisti', 'rb@gmail.com', '123456')

client = Client('Ronaldo Battisti', '123.456.789-98')

cc = CurrentAccount(5000, 10000, client)

cc.show_client()
