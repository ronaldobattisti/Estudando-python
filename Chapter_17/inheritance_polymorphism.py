"""
POO - Inheritance

- Reuse codes and extend our classes

With inheritance, by a existing classe we extend another classe that inherits attributes and methods

Ex:
Client:
    name
    surname
    cpf
    income

employee
    name
    surname
    cpf
    registration

Is that any suficiently generic expression to encapsulate?

When a class inherits from other class, it nherits all attributes and methods

when a class inherits another

Ovrttiding occurs wher override a method present in superclass os subclass
"""

# class Super


class Person:
    def __init__(self, name, surname, cpf):
        self._name = name
        self._surname = surname
        self._cpf = cpf

    def complete_name(self):
        return f"{self._name} {self._surname}"


# Before
"""
class Client():

    def __init__(self, name, surname, cpf, income):
        self._name = name
        self._surname = surname
        self._cpf = cpf
        self._income = income

    def complete_name(self):
        return f"{self._name} {self._surname}"


class Employee:

    def __init__(self, name, surname, cpf, registration):
        self._name = name
        self._surname = surname
        self._cpf = cpf
        self._registration = registration

    def complete_name(self):
        return f"{self._name} {self._surname}"
"""
# After

# sub class


class Client(Person):
    """Client inherits from person"""

    def __init__(self, name, surname, cpf, income):
        super().__init__(name, surname, cpf)
        self._income = income
# sub class


class Employee(Person):
    """Employee inherits from person"""

    def __init__(self, name, surname, cpf, registration):
        super().__init__(name, surname, cpf)
        self._registration = registration

    # Overriding exemple
    def complete_name(self):
        print(super().complete_name())
        return f"Employee registration: {self._registration} is called {self._name}"

# Overriding


client1 = Client('Ronaldo', 'Battisti', '000.123.156-98', 5000)
employee1 = Employee('Daniela', 'Pastel', '123.456.789-98', 1234)

print(client1.complete_name())
print(employee1.complete_name())
