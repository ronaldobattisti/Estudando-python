alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#       0    1    2n   3n   4    5n   6    7n    8    9   10

alphabet_wopn = []
try_prime = []
for i in range(1, len(alphabet) + 1):
    ##print(alphabet[i - 1])
    if i == 1:
        alphabet_wopn.append(alphabet[i-1])
    else:
        buff = 0
        pos = alphabet.index(alphabet[i-1])
        for j in range(pos):
            if j > 1 and j < pos and pos % j == 0:
                ##buff = buff + (pos % j)
                alphabet_wopn.append(alphabet[pos])
        '''if buff != 0:
            alphabet_wopn.append(alphabet[pos])'''

print(alphabet_wopn)
print()
