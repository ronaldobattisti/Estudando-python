'''
-Refeers to math set theory

-Can't have duplicate value
-Don't have ordenated value
-can't be acessed by index - aren't indexed

Are good when need to store ellements that don't need order and could have duplicated keys values and items
{sets} are referencied with keys {}

sets    maps(dictionaries in python)
value   keys/value
'''

# sets
# 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Have duplicated value
print(s)  # don't print duplicated values***
print(type(s))
# 2 - most commom
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# can conver string, list, tuple to a set

if 9 in s:
    print('Have 9')
else:
    print('Don\'t have 3')

data = '99, 2, 34, 23, 2, 12, 1, ,34, 44, 5'

# besides don't have duplicated values, don't have order

#list accept duplicated values
list1 = [99, 2, 34, 23, 2, 12, 1, 34, 44, 5]
print(f'List: {list1} com {len(list1)} elementos')

#Tuples acc dupplicated values
tuple1 = {99, 2, 34, 23, 2, 12, 1, 34, 44, 5}
print(f'Tuple: {tuple1} com {len(tuple1)} elementos')

#dict don't accept dupplicated keys
dict = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 34, 44, 5], 'dict')
print(f'Dictionary: {dict} com {len(dict)} elementos')

#set don't accept duplicated value
set1 = {99, 2, 34, 23, 2, 12, 1, 34, 44, 5}
print(f'set: {set1} com {len(set1)} elementos')#order the values by itself

#we can use merger type of data

set2 = {1, True, 'b', 32.44, 10}
print(set2)
print(type(set2))

#iterate
for value in set2:
    print(value)

#interesting uses:
#imagine a forms for visitor registration.
#Manually input city of origin

#We add each city n a list

city = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'São Paulo', 'Cuiabá']
print(city)
print(len(city))

#Now we need to know hou many diffrent cities we have
print(len(set(city)))

#adding elements in set
s1 = {1, 2, 3}
s1.add(4)
print(s1)

#removing 1
s1.remove(3)#value, not index - if value don't exist, key error
print(s1)

#removing 2
s1.discard(2)
print(s1)#if don't exists, don't generate any error - none return
print('############')
#copiyng
s2 = {1, 2, 3}
print(s2)

#copy 1 - deep
new = s2.copy()
print(new)
new.add(4)
print(new)
print(s2)

#copy 2 - shallow
new2 = s2
new2.add(4)
print(new2)
print(s2)

#clearing sets
s2.clear()
print(s2)

#math methods
#imagine 2 sets
#1 with pythons students
#2 with java students

py_students = {'Marcos', 'Patrícia', 'Ellen', 'Julia', 'Ana'}
java_students = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

#note that some alumns are common in both sets
#we need to generate a set with unique students name
#1 - union (recommended)
unique1 = py_students.union(java_students)
#{'Julia', 'Fernando', 'Gustavo', 'Ana', 'Ellen', 'Marcos', 'Patrícia'}
print(unique1)
#2 - char pipe '|'
unique2 = py_students | java_students
#{'Julia', 'Fernando', 'Gustavo', 'Ana', 'Ellen', 'Marcos', 'Patrícia'}
print(unique2)

#generate students in both courses set
#interception
both1 = py_students.intersection(java_students)
print(both1)
#&
both2 = py_students & java_students
print(both2)

#studant in a course that aren't in other
j_py = py_students.difference(java_students)
print(j_py)
j_ja = java_students.difference(py_students)
print(j_ja)

#if values int and real
ss = {1, 2, 3, 4, 5, 6}
print(sum(ss))
print(max(ss))
print(min(ss))
print(len(ss))