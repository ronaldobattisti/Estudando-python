list1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

list2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

list3 = []

list4 = list(range(11))

list5 = list('Geek University')

num = 18

if num in list4:
    print(f"Could find number {num}")
else:
    print(f"Couldn't find number {num}")

#To order a list
list1.sort()
print(list1)

#To find out number of ocurrences
print(list1.count(1))
print(list5.count('e'))

#To add elements in list
print(list1)
list1.append(42)
print(list1)
list1.append([8, 3, 1])#Insert list as unique element
print(list1)

list1.extend([123, 44, 67])#insert elements one by one
print(list1)

#to add in a certain position
list1.insert(2, 4)
print(list1)

#to join 2 lists - do the same as extend
list6 = list1 + list2
print(list6)

#to reverse the list
list1.reverse()
print(list1)
print(list1[::-1])#mesmo resultado do reverse(slice)

#to copy
list6 = list2.copy()
print(list6)

#to find the size
print(len(list2))

#to remove the last element - pop returns removed element
print(list5)
list5.pop()
print(list5)

#to remove determined item
list5.pop(2)
print(list5)

#to clear a list
list5.clear()
print(list5)

#to repeat elements
new = [1, 2, 3]
new = new * 3
print(new)

#to convert a string into a list
#exemple 1
course = 'Python programming'
course = course.split()
print(course)
#exemple 2
course = 'Python,programming'
course = course.split(',')
print(course)

#convert list into string
list7 = ['Python', 'programming']
course = ' '.join(list7) #in the list 7, put ' ' between each ellement
print(course)

course = '$'.join(list7)
print(course)

#iterating in lists
for element in list1:
    print(element)

'''
car = []
product = []

while product != 'sair':
    product = input("Add a product or tipe 'sair':")
    if product != 'sair':
        car.append(product)

for produtc in car:
    print(product)
'''

colors = ['green', 'white', 'blue', 'black']
print(colors[2])
print(colors[-1])

#to generate a index in for - enumerate - show the index
for ind, color in enumerate(colors):
    print(ind, color)

#to find the index of a cenrtain element
numbers = [5, 6, 7, 8, 9, 10]
print(numbers.index(6))#what's the index of number 6? - if that's more than one element, returns the first index

#searching in a range - what index start a search
print(numbers.index(7, 1))#starts the search in 1 position

#reviewing slice
#list[start:end:step]
#range(start:end:step)
list8 =[1, 2, 3, 4]
print(list8[1:])
print(list8[:])

#inverting values in a list
names = ['Ronaldo', 'Battisti']
names[0], names[1] = names[1], names[0]
print(names)
names.reverse()
print(names)

list = [1, 2, 3, 4, 5, 6]

print(sum(list))
print(max(list))
print(min(list))
print(len(list))

#transform lint in tupla
print(list)
print(type(list))

tup = tuple(list)
print(tup)
print(type(tup))

#unpacking list
list = [1, 2, 3]

num1, num2, num3 = list
print(num1)
print(num2)
print(num3)

#copying a list for another - shallow copy and deep copy
new = list.copy()#still being two independent lists - deep copy
print(new)

new.append(4)
print(list)
print(new)

new = list

print(new)
new.append(4)
print(list)
print(new)