'''
default parameters - optional parameters

'''
#parameter optional#
print('Geek University')
print()

#obrigatory parameter#
def sqr(n1):
    return(n1 **2)
n1 = 1
print(sqr(n1))

#optional parameter#
def exp(num, pow=2):
    return num ** pow
print(exp(2, 3))
print(exp(3, 2))

print(exp(2))#by default, power 2

#default parameter should be declarated in the end
#ref exp(pow=2, num): -> error

#more complex exemple#
def show_info(name='Ronaldo', instructor=False):
    if name == 'Ronaldo' and instructor:
        print('Hello instructor')
    elif name == 'Ronaldo':
        print('I thaugt you was the instructor')
    print(f'Hello, {name}')

show_info()
show_info(instructor=True)
show_info(True)
show_info('Ronaldo')
show_info(name='Altemir')

#funct as parameter#
def sum(n1, n2):
    return n1+n2

def mat(n1, n2, fun=sum):
    return fun(n1, n2)

def subt(n1, n2):
    return n1-n2
 
print(mat(2, 3))
print(mat(2, 3, subt))

#scope#
#local and globar variable#
total = 0

def increment():
    global total #Informs that want to use the global variable value

    total += 1
    return total

print(increment())
print(increment())
print(increment())

#funct inside funct#
def out():
    count = 0

    def ins():
        nonlocal count
        count += count
        return count
    return ins()
