"""
Knowing Pickle

Pickle function is:

Python object -> Binarization

Binarization -> Python object

Serialization/deserealization

OBS: Picke module isn't safe against malwares, so it's not recommended to work with pickle data from others
"""

import pickle


class Animal:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def eat(self):
        print(f"{self._name} is eating...")


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print(f"{self.name} is going meow...")


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def auau(self):
        print(f"{self.name} is going auau...")


felix = Cat('Felix')
pluto = Dog('Pluto')

with open('Chapter_18/test_pickle.pickle', 'wb') as file:
    pickle.dump((felix, pluto), file)

# read pickle files
with open('Chapter_18/test_pickle.pickle', 'rb') as file:
    cat, dog = pickle.load(file)

    print(f"The cat's name is {cat.name}")
    cat.meow()
    print(f"Cat's type is {type(cat)}")

    print(f"The dog's name is {dog.name}")
    dog.auau()
    print(f"Dog's type is {type(dog)}")
