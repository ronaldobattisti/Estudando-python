list1 = []
sex1 = 'm'
eye1 = 'a'
hair1 = 'l'
age1 = 20
dic = {'sex': sex1, 'eye': eye1, 'hair': hair1, 'age': age1}
list1.append(dic)
sex2 = 'f'
eye2 = 'c'
hair2 = 'p'
age2 = 50
dic = {'sex': sex2, 'eye': eye2, 'hair': hair2, 'age': age2}
list1.append(dic)
sex3 = 'm'
eye3 = 'a'
hair3 = 'c'
age3 = 30
dic = {'sex': sex3, 'eye': eye3, 'hair': hair3, 'age': age3}
list1.append(dic)
sex4 = 'm'
eye4 = 'c'
hair4 = 'p'
age4 = 19
dic = {'sex': sex4, 'eye': eye4, 'hair': hair4, 'age': age4}
list1.append(dic)
sex5 = 'f'
eye5 = 'a'
hair5 = 'l'
age5 = 27
dic = {'sex': sex5, 'eye': eye5, 'hair': hair5, 'age': age5}
list1.append(dic)

for item in list1:
    print(item)

buf = 0
ind = 0
max_age = 0

for item in list1:
    if item['eye'] == 'c' and item['hair'] == 'p':
        buf += item['age']
        ind += 1
    if item['age'] > max_age:
        max_age = item['age']

print(buf/ind)
print(max_age)

