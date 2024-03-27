"""
Doctests - are tests in the docstring in python

To execute a doctest:   -> python -m doctest -v Chapter_20/doctests.py 
                        -> python -m doctest -v module_name.py

-----------------------------------
Output:
Trying:
    sum(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.sum
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
------------------------------------

"""


def sum(a, b):
    """sum values a and b

    >>> sum(1, 2)
    3

    >>> sum(1, 2)
    3
    """
    return a + b


print(sum(3, 4))


def duplicate(value):
    """duplicate the values in a list

    >>> duplicate([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicate ([])
    []

    >>> duplicate(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> duplicate ([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """

    return [2 * ellement for ellement in value]


def say_hi():
    """Say Hi

    >>> say_hi()
    'hi' # should be '', not ""
    """
    return 'hi'
