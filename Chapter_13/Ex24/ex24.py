file_loc = "C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex24/storage.txt"

def read_file():
    with open(file_loc, 'r') as file:
        text = file.read().split('\n')
    if '' in text:
        text.pop(text.index(''))
    text = [item.split(',') for item in text]
    text = [[int(num2) if num2.isdigit() else num2 for num2 in num1] for num1 in text]
    return text

def print_file(text):
    with open(file_loc, 'w') as file:
        for item in text:
            line = ','.join([str(collumn) for collumn in item])
            file.write(f'{line}\n')

def ins_prod(name, quant):
    text = read_file()
    for enum, item1 in enumerate(text, start=0):
        for item2 in item1:
            if name.upper() in str(item2).upper():
                text[enum][2] += quant
                print(f"{name} now have {text[enum][2]} unitys")
    print_file(text)
    print(text)

#if __name__ == '__main__':
#while 0:
option = int(input("Select the option:\n1-Add a product\n2-Remove a project\n3-Check stoock\n4-0 product\n"))
if option == 1:
    product = input("Insert the product name: ")
    try:
        quant = int(input("Insert the quantity:"))
    except ValueError:
        print('Quantity should be an integer')
    ins_prod(product, quant)
elif option == 2:
    2
elif option == 3:
    3
elif option == 4:
    4
else: 
    print("Invalid otion")