alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex6/Text.txt", 'r') as file:
    text = file.read()
    for letter in alphabet:
        cont_letter = 0
        for char in text:
            if letter == char:
                cont_letter += 1
        print(f'Letter {letter} appeared {cont_letter} times')


file.close()