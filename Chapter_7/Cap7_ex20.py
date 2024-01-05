list1 = []

for i in range(10):
    print(f'Write {i+1}° number between 0 and 50:')
    num = int(input())
    if 0 <= num and num <= 50:
        list1.append(num)
    else: print('invalid value')

list2 = []
for i in range(len(list1)):
    if (i % 2) != 0:
        list2.append(i)

print(list1)
print(list2)

for i in range(0, len(list1), 2):
    if (i + 1) < len(list1):
        print(f"{list1[i]}, {list1[i + 1]}")
    else:
        print(list1[1])

for i in range(0, len(list2), 2):
    if (i + 1) < len(list2):
        print(f"{list2[i]}, {list2[i + 1]}")
    else:
        print(list2[1])