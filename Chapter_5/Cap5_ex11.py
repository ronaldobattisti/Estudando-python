print("Escreva um número para somar seus algarismos: ")

lista = list(input())
buff = 0

for i in lista:
    buff = buff + int(i)

print(f"A soma dos algarismos é {buff}")
