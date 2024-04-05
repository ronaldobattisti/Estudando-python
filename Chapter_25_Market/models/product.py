from utils.helper import format_float_str_currency


class Product:
    counter: int = 1

    def __init__(self: object, name: str, price: float) -> None:
        self.__cod: int = Product.counter
        self.__name: str = name
        self.__price = price
        Product.counter += 1

    @property
    def cod(self: object) -> int:
        return self.__cod

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def price(self: object) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Code: {self.cod} | Name: {self.name} | Price: {self.price}'
