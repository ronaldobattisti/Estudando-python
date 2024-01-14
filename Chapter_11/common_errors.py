'''
#1 - SyntaxError - occures when python find a sytax error
# yow wrote somthing python doesn't know as part of the lenguage

#ex syntas error
#Call wrong a funct
def function:
    print('Ronaldo')

#using a reserved word
None = 1

#return


#2 - NameError -> occure when a variable or funct wasn't defined
ex name error
geek()

a = 18

if a < 10:
    msg = 'a is lower than 10'

print(msg)

#3 - TypeError -> functio applyed in a wrong type

ex type_error
print(len(5)) - len just wirk with iterables

print('Geek' + []) can not concatene a string with a list

#4 - IndexError -> occure when we try to acess a ellement in a iterable with a invalid index
list1 = [1, 2, 3]

print(list1[5]) does not exists

#5 - ValueError -> When a funct or operacion built-in gets a correct type of ellement but innapropriated value
print(int('42.8'))

#6 - KeyError -> when we try to acess a dict with a non existing key
dict1 = {}
print(dict['geek'])

#7 - AttributeError - when a variable don't have a atribute or function
tuple1 = (10, 2, 31, 4)
tuple1.sort() - don't exists

#8 - IdentationError -> out of pep8



'''