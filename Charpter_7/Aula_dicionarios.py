# in some lenguages, dictionares == maps
# they are connections between key and value
'''
In lists an tuples you can see the inde
[0, 1, 2]
[2, 5, 4]

dictionares are represented by {}
'''

print(type({}))
# form 1
paises = {'br': 'Brazil', 'eua': 'United States os America', 'py': 'Paraguay'}

print(paises)
print(type(paises))

# Form 2
paises = dict(br='Brazil', eua='United States od America', py='Paraguay')
print(paises)
print(type(paises))

# accesing etlements
# 1: by key - as list/tuple
print(paises['br'])
# print(paises['ru']) - key error

# 2 byy get
print(paises.get('br'))
print(paises.get('ru'))
# the data 'none' in python is type without type, or void type
# None is always specified with first letter in upper case
# we cas use none when wu want to create a variable an initializate without type before give a fanal value
# its preferible the use of get because of the facility using the data ex:
russia = paises.get('ru')
if russia:  # O tipo none é sempre considerado falso
    print('Encontrei rússia')
else:
    print('não encontrei rússia')

# valor padrão caso não encontre o objeto
russia = paises.get('ru', 'Não ancontrado')
print(f'Encontrei o país {russia}')

print('br' in paises)  # busca pelo valor, não pela chave
print('ru' in paises)

if 'ru' in paises:  # ...
    i = 0

# we can use ny kind of data
# in this case wu are using tules as dictionaries keys because they are immutable
localitys = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.1236, 74.4815): 'Escritório em Noca York',
    (35.6549, 78.6541): 'Escritório em São Paulo',
}

print(localitys)
print(type(localitys))

# Add elements to dictionaries
reciep = {'jan': 100, 'fev': 120, 'mar': 300}

print(reciep)
print(type(reciep))
# common
reciep['abr'] = 350

print(reciep)

new_data = {'mai': 500}

reciep.update(new_data)  # reciep.updete({'mai: 500})

print(reciep)

# att data in dictionary
# 1
reciep['mai'] = 550

# 2
reciep.update({'mai': 600})

# removig data
# 1 - most commom
ret = reciep.pop('mar')
print(ret)  # whe we remove, it return the removed value
print(reciep)
# 2
# if key doent exists, return key error - don't return removed value
del reciep['fev']
print(reciep)

'''
when to use dictionary
imagine you have a e-commerce
cart:
    Product 1:
        name:
        quant:
        price:
    Product 2:
        name:
        quant:
        price:    
'''

# can we use list? yes
cart = []

prod1 = ['Bike', 1, 1000.0]
prod2 = ['TV', 1, 2000.0]

cart = (prod1, prod2)

print(cart)  # we should know what id the index of each prod

# Could wu use a tuple? Yes...

# dictionary? YRS
cart = []

product1 = {'name': 'Bike', 'quant': 1, 'price': 1000.0}
product2 = {'name': 'TV', 'quant': 1, 'price': 2000.0}
cart.append(product1)
cart.append(product2)
print(cart)  # these way easely we add and remove product with clear information

# Metods

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
# clear dict
d.clear()
print(d)

# copy
# 1-deep copy
d = dict(a=1, b=2, c=3)
a = d.copy()
print(a)
d['d'] = 4  # deep copy
print(d)
print(a)

# 2-shallow copy
e = d
d['e'] = 5
print(d)
print(e)

# non usual creation method
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

# unknow is the value for all other keys
user = {}.fromkeys(['name', 'points', 'email', 'profile'], 'unknow')
print(user)

veja = {}.fromkeys('test', 'value')
print(veja)  # for each letter creates a index(dont repeat the letter)

veja = {}.fromkeys(range(1, 11), 'value')
print(veja)

# how to iterate
reciep = {'jan': 100, 'fev': 120, 'mar': 300}
for key in reciep:
    print(key)

for key in reciep:
    print(reciep[key])

print(reciep.keys())

# recommended
for key in reciep.keys():
    print(reciep[key])

print(reciep.values())
for val in reciep.values():
    print(val)

# unpacking
for keys, value in reciep.items():
    print(f'Reciep: {keys}, value: {value}')

print(sum(reciep.values()))
print(max(reciep.values()))
print(min(reciep.values()))
print(len(reciep.values()))
