
class Equipment:

    def __init__(self, voltage, power):
        self._voltage = voltage
        self._power = power

    @property
    def voltage(self):
        return self._voltage

    @property
    def power(self):
        return self._power

    @voltage.setter
    def voltage(self, value):
        self._voltage = value

    @power.setter
    def power(self, value):
        self._power = value

    def show(self):
        return self._voltage, self._power


class Computer(Equipment):

    def __init__(self, brand, model, equipment_instance):
        self._brand = brand
        self._model = model
        super().__init__(equipment_instance.voltage, equipment_instance.power)

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @brand.setter
    def brand(self, value):
        self._brand = value

    @model.setter
    def model(self, value):
        self._model = value

    def show(self):
        return self._brand, self._model, super().show()[0], super().show()[1]


eq1 = Equipment(220, 2200)
eq2 = Computer("Acer", "Nitro", eq1)

print(eq1.__dict__)
print(eq2.__dict__)
print(eq1.show())
print(eq2.show())
