def size(*args, **kwargs):
    print(len(args))
    print(len(kwargs))
    
value_args = (1, 2, 3, 4,)
value_kwargs = {'name' : 'Ronaldo', 'surname' : 'Battisti'}
size(*value_args, **value_kwargs)