print("Escreva número e, para parar, pressione enter: ")

numeros = []
i = 1

while True:
    print(f"Digite o {i}° número: ")
    buf = input()
    if buf == '':
        break
    else:
        numeros.append(buf)
        i += 1

numeros.sort

for i in numeros:
    print(i)
