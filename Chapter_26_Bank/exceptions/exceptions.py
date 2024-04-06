class OutOfRangeException(Exception):
    """Custom exception for values out of range"""

    def __init__(self: object, value: int) -> str:
        self.__value = value

    @property
    def value(self: object) -> str:
        return self.__value

    def __str__(self: object):
        return f"Value {self.value} is out of range"
