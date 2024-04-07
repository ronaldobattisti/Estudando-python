class Account:
    counter = 1

    def __init__(self: object, name: str, balance: float, number: int = None) -> None:
        if number is not None:
            self.__number = number
        else:
            self.__number: int = Account.counter
            Account.counter += 1

        self.__name: str = name
        self.__balance: float = balance

    @property
    def number(self: object) -> int:
        return self.__number

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def balance(self: object) -> float:
        return self.__balance

    @number.setter
    def number(self: object, new_number: int) -> None:
        self.__number = new_number

    @balance.setter
    def balance(self: object, new_value: float) -> None:
        self.__balance = new_value

    def __str__(self: object) -> str:
        return f"Account number: {self.number} | Holder: {self.name} | Balance: {self.balance}"
