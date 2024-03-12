class Square:

    def __init__(self, side):
        self._side = side
        self._area = self.area()
        self._perimeter = self.perimeter()

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = value

    def area(self):
        return self._side ** 2

    def perimeter(self):
        return self._side * 4

    def __repr__(self):
        return f"Side = {self.side} | perimeter = {self._perimeter} | area = {self._area}"


sq1 = Square(2)
sq2 = Square(0)
sq2.side = 3
print(sq1)
print(sq2)

print(sq1.__dict__)
print(sq2.__dict__)
