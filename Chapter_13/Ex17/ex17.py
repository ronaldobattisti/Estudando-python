def split_content(string):
    text = string.split('\n')
    try:
        text.pop(text.index(''))
    except:
        0
    try:
        matrix_size = text.pop(0).split(' ')#return the dimension 1, dimension 2 and anulated positions
        matrix_size = [int(item) for item in matrix_size]#convert the numbers to string

        quant_null = int(matrix_size.pop(len(matrix_size)-1))
        
        voided_position = [item.split(' ') for item in text]
        voided_position = [[int(element) for element in inner_list] for inner_list in voided_position]#convert inner list into int
    
    except ValueError as err:
        print(f"{err} error. \nSome character in the file isn't a integer.")
    return matrix_size, quant_null, voided_position


with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex17/matrix.txt", "r") as file:
    content = file.read()
m_size, q_null, v_position = split_content(content)

matrix = [[0 if [num2, num1] not in v_position else 1 for num1 in range(m_size[0])]for num2 in range(m_size[1])]

with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex17/solution.txt", 'w') as file:
    for row in matrix:
        for collumn in row:
            print(collumn)
            file.write(str(collumn))
        file.write('\n')
