"""
POO - multiple inheritance

multiple iheritance is the possibility of a class inherits from multiple classes - son class inherits all attributes and methods of all classes

It could be done 2 ways:
    -direct multi derivation
    -indirect multi derivation

"""

# 1 - direct


class Base1:
    pass


class Base2:
    pass


class MultiDerivated(Base1, Base2):
    pass

# indirect


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivated(Base3):
    pass

##############################################


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


whale = Aquatic('Wally')
print(whale.swim())
print(whale.greet())

armadillo = Land('Toto')
print(armadillo.greet())
print(armadillo.walk())

peng = Penguin("Pingu")
print(peng.walk())
print(peng.swim())
print(peng.greet())

# finding if a object is instance of other

print(f"Pingu is instance of Penguin? {(isinstance(peng, Penguin))}")
print(f"Pingu is instance of Aquatic? {(isinstance(peng, Aquatic))}")
print(f"Pingu is instance of Land? {(isinstance(peng, Land))}")
print(f"Pingu is instance of Animal? {(isinstance(peng, Animal))}")
print(f"Pingu is instance of Object? {(isinstance(peng, object))}")
