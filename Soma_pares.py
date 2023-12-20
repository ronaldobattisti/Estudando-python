print("Escreva os número para o array, e para finalizar pressione enter:\n")

arr = []
buff = input()
while buff != "":
    arr.append(int(buff))
    buff = input()

sum = int(input("Escreva a soma: "))

for i in arr:
    for j in arr:
        if i + j == sum and j > i:
            print(f"{i}, {j}")
