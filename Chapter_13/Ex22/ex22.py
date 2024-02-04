def remove_b_line(str):
    print(str)
    if '\n' in str:
        buffer =  str.replace('\n','')
        return float(buffer)
    else:
        return float(str)

def div_string(str):
    print(str)
    for enum, cont in enumerate(str):
        #print(f"{enum}, {cont}")
        if cont.isnumeric():
            name = str[:enum]
            print(name)
            grades = str[enum:].split(' ')
            print(grades)
            break
    #print(grades)
    grades = [remove_b_line(item) for item in grades]
    ordered_grades = sorted(grades, reverse = True)
    return name, ordered_grades


save_file = "output"

with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex22/student_s_grades.txt", 'r') as file:
    text = file.read()
name, grade = div_string(text)
grade_str = (' ').join([str(item) for item in grade])

with open(f"C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex22/{save_file}.txt", 'w') as file:
    file.write(f"{name} {grade_str}")