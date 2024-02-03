
vector = [1, 5, 10, 16, 60, 100, 156, 952, 1650, 10231]
vector_bin = [bin(num) for num in vector]
with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/ex16.txt", 'w') as file:
    for item in vector_bin:
        file.write(f"{item}\n")