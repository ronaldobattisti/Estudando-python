"""
Forcing types of data with decorators

zip

a = (1, 3, 5)
b = (2, 4, 6)
c = zip(a, b)
(1, 2), (3, 4, (5, 6))

"""

def force_type(*types):
    def decor(funct):
        def convert(*args, **kwargs):
            new_args = []
            for(value, tipe) in zip(args, types):
                new_args.append(tipe(value))
            return funct(*new_args, *kwargs)
        return convert
    return decor

@force_type(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg('ronaldo', '3')

@force_type(float, float)
def divide(a, b):
    return a / b

print(divide('1', 5))