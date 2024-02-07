file_loc = "C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex28/file1.txt"
out_file_loc = "C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex28/out_file1.txt"

def file_read(file_loc):
    with open(file_loc, 'r', encoding='utf-8') as file:
        text = file.read()
    return(text)

def save_file(text, file_loc):
    with open(file_loc, 'w') as file:
        text = file.write(text)

if __name__ == "__main__":
    text = file_read(file_loc)
    txet = []
    for cont in range(1, len(text)):
        txet.append(text[len(text)-cont])
    txet = ''.join(txet)
    save_file(txet, out_file_loc)