save_file = "output"

with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex22/student_s_grades.txt", 'r') as file:
    text = file.readlines()

text = [line.replace('/n', '') for line in text]
#text = [line.rsplit() for line in text]
print(text)