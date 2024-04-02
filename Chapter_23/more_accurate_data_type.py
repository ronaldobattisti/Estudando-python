from typing import final  # this final is a decorator
from typing import Final
from typing import Union
from typing import Literal


def double(value: int) -> int:
    return value * 2


print(double(2))
print(double('Ronaldo'))

"""
- Literal type
- Union
- Final
- Typed dictionaries
- Protocols
"""


def get_status(user: str) -> Literal['connected', 'disconnected']:
    pass


""" With out literal type
def calculate_v1(operation: str, num1: int, num2: int) -> None:
    if operation == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operation == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Invalid operation {operation!r}')
"""

# With literal type


def calculate_v1(operation: Literal['+', '-'], num1: int, num2: int) -> None:
    if operation == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operation == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Invalid operation {operation!r}')


calculate_v1('+', 6, 4)
# calculate_v1('*', 3, 5)
print('--------------------------------------------------')


# This function can return either a string or an integer
def sum(num1: int, num2: int) -> Union[str, int]:
    pass


NAME: Final = 'Geek'


@final
class Person:
    pass


class Student:
    pass

    @final
    def study(self):
        print("I'm studying...")


class Intern(Student):  # can't inherate person, ecause it's final
    pass

    def study(self):  # can't extend study() because it's final
        print("Studying and interning")
