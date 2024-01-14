'''
try/except/else/finally

tip: when to threata the code
all input should be threated

'''
'''try:
    num = int(input('Input a number:'))
except ValueError as arr1:
    print('Invalid value')
else: #if not error = else and finaly
    print(f'You typed number {num}')
finally: #always executed, if that was a exception or not
    print('Executing finally')'''
#finally is often used to close or deallocate resources
#ex: close a connection with data source, close a file, etc
    
#more complex exemple
#1- not a good way to threat the error - too messy
'''def divide(a, b):
    return a / b

try:
    num1 = int(input('Input 1st number: '))
    num2 = int(input('Input 2nd number: '))
except ValueError as verr:
    print('The number should be numeric')

try:
    print(divide(num1, num2))
except NameError as nerr:
    print('The number should be numeric')'''

#2 - the way it should be - you are responsable for the code

def divide(a, b):
    try:
        return int(a) / int(b)
    except ValueError as verr:
        print('Incorrect value')
    except ZeroDivisionError as zerr:
        print('Impossible division by 0')

num1 = input('Input 1st number: ')
num2 = input('Input 2nd number: ')
print(divide(num1, num2))

#3 - semi-generic way

def divide(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f'Problem!!: {err}')


num1 = input('Input 1st number: ')
num2 = input('Input 2nd number: ')
print(divide(num1, num2))