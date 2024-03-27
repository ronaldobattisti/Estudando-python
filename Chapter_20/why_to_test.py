"""
why to test the code:
    - reduce bugs
    - guarentee that new features don't change the old ones
    - guarentee that old fixed bugs still fixed
    - guarantee that refactoring don't bring ey bugs

TDD - test driven development
-> first write the test, then the code
    - Write the test
    - develop the code to pass the test
    - improove the code
    - if pass the test, it's complete

-> these stages of TDD are mantra like following, and are known as:
    - Red;
    - Green;
    - Refactor;
"""


class Cat:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def meow(self):
        print(f"{self.name} is meowing")


felix = Cat('Felix')

felix.meow()

print(felix.name)
