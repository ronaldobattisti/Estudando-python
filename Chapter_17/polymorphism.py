"""
POO -> polymorphism
poly - many
morphys - ways
"""


class Animal():

    def __init__(self, name):
        self._name = name

    def talk(self):
        raise NotImplementedError(
            'The son class should implement this method')  # Throw a exception

    def eat(self):
        print(f"{self._name} is eating!")


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f"{self._name} goes auauau!")


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f"{self._name} goes miaumiau!")


class Mouse(Animal):

    def __init__(self, name):
        super().__init__(name)

    def talk(self):
        print(f"{self._name} goes rsrsrsr")


jujuba = Cat('Jujuba')
jujuba.talk()
jujuba.eat()

pintas = Dog('Pintas')
pintas.talk()
pintas.eat()

mickey = Mouse('Mickey')
mickey.eat()
mickey.talk()
