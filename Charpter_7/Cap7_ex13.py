list1 = []

for i in range(5):
    val = input(f'Write {i+1}° value:')
    list1.append(int(val))

print(list1.index(max(list1)))
print(list1.index(min(list1)))