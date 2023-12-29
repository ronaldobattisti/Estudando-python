list1 = [5, 4, 1, 3, 2, 9, 10, 7, 8, 6]
list2 = []

for i in range(len(list1)):
    list2.append(min(list1))
    list1.pop(list1.index(min(list1)))

print(list2)