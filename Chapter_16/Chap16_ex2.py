class Schedule:

    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def insert_person(self, name, age, height):
        pass
