class Person:

    def __init__(self, name, adress, phone):
        self._name = name
        self._adress = adress
        self._phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def adress(self):
        return self._adress

    @adress.setter
    def adress(self, value):
        self._adress = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def print(self):
        print(f"{self._name} lives at {self._adress} with phone number {self._phone}")


p1 = Person('Ronaldo Battisti', 'Mars', '9999')
p2 = Person('', '', '')
p2.name = 'Daniela Donida'
p2.adress = 'Rosa'
p2.phone = '999999'

p1.print()
p2.print()
