with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex2/Quant_lines.txt.txt", 'r') as file:
    string = file.read()
    string = string.split('\n')
    print(len(string))
    file.close()