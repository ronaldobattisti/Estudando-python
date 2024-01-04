"""
The *args is a parameter of a function, can be called anything, but need the *
The *args used in a function insert the values in a tuple - immutable

"""


def sum_all_numbers(n1, n2, n3):
    return n1+n2+n3


print(sum_all_numbers(4, 6, 9))

# print(sum_all_numbers(4, 6)) -> typeError
# print(sum_all_numbers(4, 6, 9, 5)) -> typeError

# Undersanding *args


def sum_all_numbers(*args):
    return sum(args)


print(sum_all_numbers())
print(sum_all_numbers(1))
print(sum_all_numbers(1, 2))
print(sum_all_numbers(1, 2, 3))
print(sum_all_numbers(1, 2, 3, 4))

number = [1, 2, 3, 4, 5, 6, 7]
# Unpacking the list to be used in the functiton numb by numb
print(sum_all_numbers(*number))


def verify_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Welcome geek'
    return 'I don\'t know you'


print(verify_info())
print(verify_info(1, True, 'University', 'Geek'))
print(verify_info(1, 'University', 3.145))
