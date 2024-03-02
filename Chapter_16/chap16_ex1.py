class Person:

    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def print_data(self):
        print(f"{self._name} have {self._age} years and {self._height} tall")


p1 = Person("Ronaldo Battisti", 28, 1.83)

p1.print_data()
