file_loc = "C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex24/storage.txt"

#read the file into a string
def read_file():
    with open(file_loc, 'r') as file:
        text = file.read().split('\n')
    if '' in text:
        text.pop(text.index(''))
    text = [item.split(',') for item in text]
    text = [[int(num2) if num2.isdigit() else num2 for num2 in num1] for num1 in text]
    return text

#write the text in the file
def print_file(text):
    with open(file_loc, 'w') as file:
        for item in text:
            line = ','.join([str(collumn) for collumn in item])
            file.write(f'{line}\n')

#find a index free to use
def get_next_free_index(text):
    indexes = []
    for item in text:
        indexes.append(item[0])
    cont = 0
    for item in range(1, len(indexes)+2):
        cont += 1
        if cont not in indexes:
            new_index = cont
    return new_index

#update the list based on a new register or quantity update
def ins_prod(name, quant):
    text = read_file()
    exists = False
    for enum, item1 in enumerate(text, start=0):
        for item2 in item1:
            if name.upper() in str(item2).upper():
                text[enum][2] += quant
                exists = True
                break
    if not exists:
        text.append([get_next_free_index(text), name, int(quant)])
                #print(f"{name} now have {text[enum][2]} unitys")
            
    sorted_text = sorted(text, key=lambda x: x[0])
    print_file(sorted_text)

def delete_item(text, index):
    print(text)
    print(index)
    for enum, line in enumerate(text, start=0):
        if line[0] == index:
            print(index)
            text.pop(enum)
            print(text)
            break
    print_file(text)

#retur a list with the items from the file separated by '|'
def show_items():
    text = read_file()
    out_string = []
    for item in text:
        out_string.append('|'.join([str(collumn) for collumn in item]))
    return out_string

def show_empty_items():
    text = read_file()
    out_string = []
    for item in text:
        if item[2] == 0:
            out_string.append('|'.join([str(collumn) for collumn in item]))
    return out_string

#if __name__ == '__main__':
while True:
    option = int(input("Select the option:\n1-Add a product\n2-Remove a product\n3-Check stoock\n4-0 product\n"))
    if option == 1:
        product = input("Insert the product name: ")
        try:
            quant = int(input("Insert the quantity:"))
        except ValueError:
            print('Quantity should be an integer')
        ins_prod(product, quant)
    elif option == 2:
        print('INDEX | DESCRIPTION | QUANTITY')
        for item in show_items():
            print(item)
        delete_index = int(input("select a item to delete: "))
        delete_item(read_file(), delete_index)
    elif option == 3:
        print('INDEX | DESCRIPTION | QUANTITY')
        for item in show_items():
            print(item)
    elif option == 4:
        print('INDEX | DESCRIPTION | QUANTITY')
        for item in show_empty_items():
            print(item)
    else: 
        print("Invalid option")