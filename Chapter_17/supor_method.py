"""
POO - super() method

refers to a super class

"""


class Animal:

    def __init__(self, name, species):
        self._name = name
        self._species = species

    def sound(self, sound):
        print(f"{self._name} goes {sound}")


class Cat(Animal):

    def __init__(self, name, species, race):
        # Animal.__init__(self, name, species)
        super().__init__(name, species)  # its the iddeal
        self._race = race


felix = Cat('Felix', 'Feline', 'Angorá')

felix.sound('Meow')
