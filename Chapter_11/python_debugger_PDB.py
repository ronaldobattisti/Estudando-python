'''
PDB debugging - Python Debugger

Using 'print' to debug a code isn't good

There ir better way to do this using debugger like pdb
'''
#native debugger - indicated
def divide(a, b):
    try:
        return int(a) / int(b)#add to watch
    except ValueError as verr:
        print('Incorrect value')
    except ZeroDivisionError as zerr:
        print('Impossible division by 0')

print(divide(4, 7))

#to use python debugger, we shold import pdb lybrarie*

#ex1
#pdb basics commands
#l to list where we are in the code
#n new line
#p print variable
#c continue execution - end debug
import pdb

name = 'Ronaldo'
surname = 'Battisti'
pdb.set_trace()
complete_name = name + ' ' + surname
course = 'Pytohn'
final = complete_name + ' do the ' + course + ' course'
print(final)

#ex2

name = 'Ronaldo'
surname = 'Battisti'
import pdb; pdb.set_trace()#when we want to use 2 commands in the same line, use ;
complete_name = name + ' ' + surname
course = 'Pytohn'
final = complete_name + ' do the ' + course + ' course'
print(final)

#why to use these format?
#the debug is used during the develop
#We use to do all lib imports in the beginning
#So its easier and cleaner do the import in the middle to clear after find the error

#ex 3
#from python 3.7 it's nor necessary to import pdb, because turned built-in, it's called breakingpoint
name = 'Ronaldo'
surname = 'Battisti'
breakpoint()
complete_name = name + ' ' + surname
course = 'Pytohn'
final = complete_name + ' do the ' + course + ' course'
print(final)

#caution with conflict between variable names and pdb commands
def sum(l, n, p, c):
    breakpoint()#breakpoint commands conflict - we need to input "p c"(print variable c)
    return l + n + p + c

print(sum(1, 3, 5, 7))