class Motorcycle:

    def __init__(self, brand, model, color, gear, higher_gear, lower_gear):
        self._brand = brand
        self._model = model
        self._color = color
        self._gear = gear
        self._higher_gear = higher_gear
        self._lower_gear = lower_gear

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def color(self):
        return self._color

    @property
    def gear(self):
        return self._gear

    @brand.setter
    def brand(self, value):
        self._brand = value

    @model.setter
    def model(self, value):
        self._model = value

    @color.setter
    def color(self, value):
        self._color = ValueError

    @gear.setter
    def gear(self, value):
        self._gear = value

    def prints(self):
        print(
            f"Brand = {self._brand}|Model = {self._model}|Color = {self._color}|Gear = {self._gear}")

    def gear_up(self):
        if self._gear < self._higher_gear:
            self._gear += 1
        else:
            print(
                f"This gear can't be reacher, higher gear is {self._higher_gear}")

    def gear_down(self):
        if self._gear > self._lower_gear:
            self._gear -= 1
        else:
            print(
                f"This gear can't be reacher, lower gear is {self._lower_gear}")


m1 = Motorcycle("Honda", "Fazer", "Black", 0, 5, 0)
m1.prints()
m1.brand = "Yamaha"
m1.prints()
m1.gear_down()
m1.gear = 5
m1.gear_up()
