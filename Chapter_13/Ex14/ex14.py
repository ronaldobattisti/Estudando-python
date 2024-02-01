with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex14/names_birth.txt.txt") as file:
    text = file.read()
    text = text.split('\n')
    print(text)
    for item in text:
        if text[text.index(item)] == '':
            #print(text.index(item))
            text.pop(text.index(item))
    print(text)
    for item in text:
        for cont in range(10), :
            if item[cont].isnumeric():
                index_split = cont - 1
                print(index_split)
                break
            else:
                cont += 1
            
    print(text)
    file.close()