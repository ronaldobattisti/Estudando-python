list1 = []
for i in range(5):
    val = input(f'Write {i + 1}° value: ')
    list1.append(int(val))
list2 = list(set(list1.copy()))
for i in list2:
    list1.pop(list1.index(i))
print(list1)