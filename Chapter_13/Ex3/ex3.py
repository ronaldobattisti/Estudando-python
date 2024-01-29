vowels = ['a', 'e', 'i', 'o', 'u']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex3/consoants.txt", 'r') as file:
    string = file.read()
    for item in string:
        if item in alphabet:
            if item not in vowels:
                print(f"the character {item} is a consonant")
            else:
                print(f"the character {item} is a vowel")
        else:
            0
file.close()
