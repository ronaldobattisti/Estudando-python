"""
POO - magic methods

Are all method that use __ dunder

__init__

__repr__ - object representation

__str__ - same as __repr_ but have execution preference

__len__ - habilits use of len

__del__ - action when delete something

__add__ - change the sum action
"""


class Book:

    def __init__(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    def __repr__(self):  # Class representation
        return self._title

    def __str__(self):  # same as __repr_ but have execution preference
        return self._title

    def __len__(self):
        return self._pages

    def __del__(self):
        print("A book object was deleted")

    def __add__(self, other):
        return f"{self} - {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = ''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return "Can't multiply"


book1 = Book('Livro1', 'Ronaldo', 400)
book2 = Book('Livro2', 'Daniela', 420)

print(book1)
print(book2)

print(len(book1))

print(book1 + book2)

print(book1 * 2)
