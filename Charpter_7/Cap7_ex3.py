i = 0
list1 = []
while i < 10:
    value = int(input(f"Write {i + 1}° value: "))
    list1.append(value * value)
    i += 1

print(list1)