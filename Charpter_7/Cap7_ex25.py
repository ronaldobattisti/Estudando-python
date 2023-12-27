vet = []
i = 0
while len(vet) < 100:
    if (i % 7 == 0) or ((i - 7) % 10 == 0):
        vet.append(i)
    i += 1
print(vet)