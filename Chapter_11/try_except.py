'''
block try except

We use to threat errors thatould occure in the code, avoiding unexoected error messages

the simpliest way is:

try:
    problematic execution
except:
    what to do in case of problem
'''

#ex1: generic error

try:
    geek() #try to execute these function
    len(5)
except:
    print('Problem') #in case of error, print this
# threating error as generic is not the best way, we shoud threat the specific error

#ex2: threating a specific error
try:
    geek() #try to execute these function
except NameError:
    print('You\'re using a inexisting function') #in case of error, print this    

#ex 3
try:
    len(5) #try to execute these function
except TypeError:
    print('You\'re using a inexisting function') #in case of error, print this    

#ex 4
try:
    len(5)
except TypeError as err:
    print(f'the application throws the following error: {err}')

#ex5 - getting more than 1 exception
try:
    len(5)
except NameError as erra:
    print(f'the error was {erra}')
except TypeError as errb:
    print(f'the error was {errb}')
'''except TypeError as errb:
    print(f'the error was {errb}')'''

#ex5 - getting more than 1 exception
try:
    print('Geek'[9])
except NameError as erra:
    print(f'the error was {erra}')
except TypeError as errb:
    print(f'the error was {errb}')
except:
    print('Diffrent error')

#ex6 - 

def get_value(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'name': 'value'}
print(get_value(dic, 'name'))

dic = {'name': 'value'}#key error
print(get_value(dic, 'game'))