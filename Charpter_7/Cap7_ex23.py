cnj1 = []
cnj2 = []
for i in range(5):
    val = int(input(f'Write {i+1}° value for list 1: '))
    cnj1.append(val)
    val = int(input(f'Write {i+1}° value for list 2: '))
    cnj2.append(val)

buf = 0
for i in range(len(cnj1)):
    buf += (cnj1[i] * cnj2[i])

print(buf)