with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex8/exercice8.txt", 'r') as file:
    text = file.read().upper()
file.close()
with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex8/exercice8_past.txt", 'w') as file:
    file.write(text)
file.close()
