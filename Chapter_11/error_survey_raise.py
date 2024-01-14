'''
raise - throw exceptions

it's not a function, it's a reserver word like def

used to create our own exception

raise KindOfError('Error msg)
'''

#raise ValueError('Incorrect Value')

'''#real exemple
def color(text, color):
    if type(text) is not str:
        raise TypeError('Text should be a string')
    if type(color) is not str:
        raise TypeError('Color should be a string')
    print(f'{text} well be printed in {color}')
    
color('Geek', 'Blue')
color('Geek', 4)'''

def color(text, color):
    colors = ('green', 'yellow', 'red')
    if type(text) is not str:
        raise TypeError('Text should be a string')
    if type(color) is not str:
        raise TypeError('Color should be a string')
    if color not in colors:
        raise ValueError(f'The collor needs to be one of {colors}')
    print(f'{text} well be printed in {color}')
    
color('Geek', 'green')
color('Geek', 'purple')