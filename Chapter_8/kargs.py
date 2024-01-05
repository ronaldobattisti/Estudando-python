'''
**kaergs
diffrent from *args, needs to be a nominated parameter, to be inserted in a dictionary

def fav_colors(n1, s1, *kwargs):
    print(kwargs)

fav_colors(1, 'Hello', Marcos='verde', Julia='amarelo', Fernando='azul', Vanessa='branco')

#orger;
-> Obligatory parameters;
-> *args;
-> Default parametera(Optional);
-> **kwargs;
'''


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f'Favorite color of {person.title()} is {color}')


fav_colors(Marcos='verde', Julia='amarelo', Fernando='azul', Vanessa='branco')

# *args and **kwargs are not obligatory


def special_greeting(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'You get a pythonic greeting'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek"
    return 'Not sure whoyou are'


print(special_greeting())
print(special_greeting(geek='Python'))
print(special_greeting(geek='Hi'))
print(special_greeting(geek='Special'))


def my_funct(age, name, *args, single=False, **kwargs):  # correct declaration order
    print(f'{name} with {age} anos')
    print(args)
    if single:
        print('Single')
    else:
        print('Married')
    print(kwargs)


my_funct(8, 'Julia')
my_funct(18, 'Felicity', 4, 5, 3, single=True)
my_funct(34, 'Felipe', me='Não', you='go')
my_funct(19, 'Carla', 9, 4, 3, java=False, python='True')

# Why these order matters
'''#correct parameter order
def show_info(a, b, *args, instructor='Geek', **kwargs):
    return [a, b, args, instructor, kwargs]

print(show_info(1, 2, 3, surname='University', position='Instructor'))'''

'''# wrong parameter order -> difrent values
def show_info(a, b, instructor='Geek', *args, **kwargs):
    return [a, b, args, instructor, kwargs]


print(show_info(1, 2, 3, surname='University', position='Instructor'))'''

# unpacking dictionary


def show_name(**kwargs):
    return f"{kwargs['name']} {kwargs['surname']}"


name = {'name': 'Felicity', 'surname': 'Jones'}

print(show_name(**name))  # ** = unpacking


def sum_multiple_numbers(n1, n2, n3):
    return n1+n2+n3


print(sum_multiple_numbers(1, 2, 3))
list1 = [1, 2, 3]
print(sum_multiple_numbers(*list1))  # tuple and set too
# keys should be te same as the function, if not type error
dic1 = dict(n1=1, n2=2, n3=3)
print(sum_multiple_numbers(**dic1))
