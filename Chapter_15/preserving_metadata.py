"""
preserving metadata with wraps

Metadata -> are files intrinsic data

Wraps -> are functions that involve elements with many purpouses
"""

# Problem

def see_log(function):
    def login(*args, **kwargs):
        """I'm the function login insithe other function"""
        print(f"You're calling {function.__name__}")
        print(f"Here's documentation: {function.__doc__}")
        return function(*args, **kwargs)
    

@see_log
def sum1(a, b):
    """Sum two numbers"""
    return a + b


a = sum1(10, 30)
print(a)