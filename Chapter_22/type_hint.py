def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet('Ronaldo'))


def header(text: str, alignment: bool = True) -> str:
    if alignment:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f"{text.title()}".center(50, '*')


print(header('Ronaldo Battisti', alignment=True))

print(header('Ronaldo Battisti', alignment=True))

# Exemple annotations
name: str = 'Ronaldo Battisti'

mass: float = 76.5

active: bool

active = True

print(__annotations__)

########################################################


class Person:

    def __init__(self, name: str, age: int, mass: float):
        self._name = name
        self._age = age
        self._mass = mass

    def walk(self) -> str:
        return f"{self._name} is walking"


p = Person(name='Ronaldo Battisti', age=27, mass=76.5)

print(p.__dict__)
# print(p.__annotations__) #Instance don't have annotations
print(p.__init__.__annotations__)
