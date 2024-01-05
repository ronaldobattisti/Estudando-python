print("escreva um número inteiro positivo com 3 caracteres: ")

inp = str(int(input()))

lista = list(inp)

buff = lista[0]
lista[0] = lista[2]
lista[2] = buff

imp_mod = "".join([lista[0], lista[1], lista[2]])
print(imp_mod)
