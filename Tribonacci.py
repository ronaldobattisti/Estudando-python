size = int(input("Escreva o tamanho da lista Tribonacci: "))

tribonacci = [0, 0, 1]

i = 2

while i < size:
    buffer = tribonacci[i - 2] + tribonacci[i - 1] + tribonacci[i]
    tribonacci.append(buffer)
    i += 1

print(tribonacci)

size = int(input("Escreva o tamanho da lista: "))