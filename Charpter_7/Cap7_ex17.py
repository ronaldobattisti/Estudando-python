vet1 = [1, -1, 2, -1, -1, 3, 4, -4, 5, -5]
for i in vet1:
    if i < 0: vet1[vet1.index(i)] = 0
print(vet1)