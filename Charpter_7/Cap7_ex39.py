a = int(input('Write a number: '))
list1 = []
for i in range(a):
    list1.append(1)
    list1.append(i)
    for j in range(i):

        list1.append(1)
        print(list1)