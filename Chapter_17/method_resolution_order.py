"""
Poo - MRO

Method Resolution Order is the execution order of the method - who'll be executed first

In python we can check the order 3 ways:
    1 - by class properties __mro__
    2 - by method
    3 - by help

"""


class Animal:

    def __init__(self, name):
        self._name = name

    def greet(self):
        return f"I'm {self._name}"


class Aquatic(Animal):

    def __init__(self, name):
        super().__init__(name)

    def swim(self):
        return f"{self._name} is swiming"

    def greet(self):
        return f"I'm {self._name} from the sea!"


class Land(Animal):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return f"{self._name} is walking"

    def greet(self):
        return f"I'm {self._name} from the land!"


class Penguin(Land, Aquatic):

    def __init__(self, name):
        super().__init__(name)


peng = Penguin("Pingu")
print(peng.greet())

"""
I'm Pingu from the land! - Execute the first greet in the class
"""
