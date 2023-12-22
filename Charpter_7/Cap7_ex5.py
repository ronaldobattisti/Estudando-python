i = 0
cont = 0
list1 = []
while i < 10:
    value = int(input(f"Write {i + 1}° value: "))
    list1.append(value)
    i += 1
for i in list1:
    if i % 2 == 0:
        cont += 1

print(cont)
print(min(list1))
print(max(list1))
print(list1.index(max(list1)))

list1.reverse()
print(list1)
print(list1[::-1])