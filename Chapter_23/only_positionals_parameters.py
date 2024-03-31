def greet_1(name):
    return f'Hello, {name}'


print(greet_1('Ronaldo Battisti'))
print(greet_1(name='Ronaldo Battisti'))


def greet_2(name, /):
    return f'Hello, {name}'


print(greet_2('Ronaldo Battisti'))
# print(greet_2(name='Ronaldo Battisti')) -> don't let keywords arguments

# everything before the '/' is positional only


def greet_3(name, /, msg='Hello'):
    return f'{msg}, {name}'


print(greet_3('Ronaldo'))
print(greet_3('Ronaldo', msg='Olá'))


def greet_4(name, /, msg1="Hello", *, msg2):  # everything after the '*' is amndatory
    return f'{msg1} {name} {msg2}'
