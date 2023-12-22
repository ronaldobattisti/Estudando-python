alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabet_wopn = []
try_prime = []
for i in range(1, len(alphabet) + 1):
    if i == 1:
        alphabet_wopn.append(alphabet[i-1])
    else:
        buff = 0
        pos = alphabet.index(alphabet[i-1])
        for j in range(i):
            if j > 1 and j < i and i % j == 0:
                buff = buff + (pos % j)
        if buff != 0:
            alphabet_wopn.append(alphabet[pos])

print(alphabet_wopn)
print()
