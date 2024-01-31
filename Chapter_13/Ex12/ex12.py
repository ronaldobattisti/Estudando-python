alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex12/ex_12_text.txt.txt") as file:
    buffer = file.read()
    num_of_char = len(buffer.split(' '))
    num_of_line = len(buffer.split('\n'))
    for letter in alphabet:
        num_of_letter = 0
        for char in buffer:
            if letter == char:
                num_of_letter += 1
        print(f'Letter {letter} appeared {num_of_letter} times')
    print(num_of_char)
    print(num_of_line)
    file.close()
