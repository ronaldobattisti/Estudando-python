class Person:

    def __init__(self, cod=0, name="Blank", age=0):
        self._cod = cod
        self._name = name
        self._age = age

    @property
    def cod(self):
        return self._cod

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @cod.setter
    def cod(self, value):
        self._cod = value

    @name.setter
    def name(self, value):
        self._name = value

    @age.setter
    def age(self, value):
        self._age = value

    def show(self, *bol):
        """If parameter == 0 don't print the age, else if the parameter == 1, print the age"""
        if bol:
            print(f"{self._name} has the code {self._cod} and {self._age} years old")
        else:
            print(f"{self._name} has the code {self._cod}")


p1 = Person()
p1.name = "Ronaldo Battisti"
p1.cod = 123
p1.age = 27

p1.show()
p1.show(1)
p1.show(4)

p2 = Person(124, "Daniela Donida", 30)
p2.show()
