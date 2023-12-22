#tuples are very simmilar with lists
#there are 2 mains differences
#1-Tuples are represented by ()
#2-Tuples are immutable - after creates, it does not change
#all operations in it make another tuple

print(type(()))

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

tuple2 = 4, 5, 6, 7
print(tuple2)
print(type(tuple2))

#Tuples with one element
tuple3 = (4) #Not a tuple
tuple3 = (4,) #or |tuple3 = 4,| It's a tuple

#range
tuple4 = tuple(range(10))#range(init,end,step)
print(tuple4)
print(type(tuple4))

#unpacking
tuple5 = ('Geek university', 'Python programming')
school, course = tuple5
print(school)
print(course)

print(sum(tuple1))
print(max(tuple1))
print(min(tuple1))
print(len(tuple1))

print(tuple1 + tuple2)

tuple1 = tuple1 = tuple2 #tuples are immutable but acessible to change values

tuple6 = (1, 2, 3, 6)

print(3 in tuple6)

#iterating in a tuple
for n in tuple6:
    print(n)

for ind, value in enumerate(tuple6):
    print(f"{ind}, {value}")

#counting elements in a tuple
tuple7 = ('a', 'b', 'c', 'd', 'c', 'b',)
print(tuple7.count('a'))
print(tuple7.count('b'))

tuple8 = tuple('Ronaldo Battisti')
print(tuple8.count('t'))

#use when there's no need to modify values
#ex monts

months = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(months)

#acess to elements
print(months[5])

i = 0

while i < len(months):
    print(months[i])
    i += 1

#verufy index
print(months.index('Junho'))

#slicing
#tuple[beg:end:step]
print(months[5:9])
print(months[1:10:2])

#copiyng tuple
tuple9 = tuple1#Don't exist shallow copy problem/trouble