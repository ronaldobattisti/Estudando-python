"""Testing a obbject method that didn't work befora"""


class User:

    def __init__(self, name, surname):
        self._name = name
        self._surname = surname


class Product:

    def __init__(self, cod, user):
        self._cod = cod
        self._user = user

    def show_user(self):
        return self._user._name


user = User('Ronaldo', 'Battisti')

prod = Product('ps4', user)

print(prod.show_user())
