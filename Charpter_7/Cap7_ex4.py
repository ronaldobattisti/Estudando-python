i = 0
list1 = []
while i < 8:
    value = int(input(f"Write {i + 1}° value: "))
    list1.append(value)
    i += 1
print(list1)
value1 = int(input("Write 1st value: "))
value2 = int(input("Write 2st value: "))
suma = list1[value1] + list1[value2]
print(suma)
