vet1 = [0, 1, 2, 0, 0, 2, 0, 3, 4, 0, 5, 6, 0, 6, 7, 0]
for i in vet1.copy():
    if i == 0:
        vet1.pop(vet1.index(i))

print(vet1)

vet1 = [0, 1, 2, 0, 0, 2, 0, 3, 4, 0, 5, 6, 0, 6, 7, 0]
vet1 = [i for i in vet1 if i != 0]

print(vet1)