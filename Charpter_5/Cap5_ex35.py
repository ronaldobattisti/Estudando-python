def ano_bissexto(ano):
    if ano % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


while True:
    date = input("Digite uma data(dd/mm/yyyy): ")
    day = int(date[0]) * 10 + int(date[1])
    month = int(date[3]) * 10 + int(date[4])
    year = int(date[6]) * 1000 + int(date[7]) * \
        100 + int(date[8]) * 10 + int(date[9])

    if 1 <= month <= 12:
        if month % 2 == 0 and 1 <= day <= 30 or month % 2 != 0 and 1 <= day <= 31:
            if month == 2 and ano_bissexto(year) == True and day > 29 or ano_bissexto(year) == False and day > 28:
                print("Data inválida")
            else:
                print("Data correta!")
    else:
        print("Data inválida")

print(day)
print(month)
print(year)
