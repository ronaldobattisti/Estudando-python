from datetime import datetime
import math

def get_age(date_birth):
    age = math.floor((datetime.today() - date_birth).days/365)
    return age

def convert_date(date_str):
    day = int(date_str[:2])
    month = int(date_str[3:5])
    year = int(date_str[6:])
    formatted_date = datetime(year, month, day)
    #print(formatted_date)
    return formatted_date

with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex14/names_birth.txt", 'r') as file:
    text = file.read()
    file.close()
    text = text.split('\n')
    dict = {}
    print(text)
    for item in text:
        if text[text.index(item)] == '':
            #print(text.index(item))
            text.pop(text.index(item))
    print(text)
    for item in text:#for each line in the list [name birth]
        for enum, cont in enumerate(item):#for each letter in line
            if cont.isnumeric():#if starts to appear a number
                index_split = enum#this number will be the split index
                name = item[:index_split]
                birth = item[index_split:]
                date_birth = convert_date(birth)
                dict.update({name: date_birth})
                break
            
    print(dict)
    with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex14/names_age.txt", 'w') as file:
        for item in dict:
            file.write(item + ' is ' + str(get_age(dict[item])) + ' years\n')
    file.close()