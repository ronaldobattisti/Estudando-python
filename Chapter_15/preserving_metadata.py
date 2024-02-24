"""
preserving metadata with wraps

Metadata -> are files intrinsic data

Wraps -> are functs that involve elements with many purpouses
"""

#solution

from functools import wraps

# Problem

def see_log(funct):
    @wraps(funct)
    def login(*args, **kwargs):
        """I'm the funct login insithe other funct"""
        print(f'Youre calling {funct.__name__}')
        print(f'Heres documentation: {funct.__doc__}')
        return funct(*args, **kwargs)
    return login

@see_log
def sum1(a, b):
    """Sum two numbers"""
    return a + b


a = sum1(10, 30)
print(a)

print(sum1.__name__)
print(sum1.__doc__)#if not using wraps, instead showing sum1 documentation, it shows login documentation

