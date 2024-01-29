with open("C:/Users/RONAL\Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex1/arq.txt", "a+") as file:
    file.truncate(0)
    value = 'a'
    cont = 1
    while value != '0':
        value = input(f'Write the {cont}º character')
        cont += 1
        file.write(value + '\n')
    file.close()