"""
Reading CSV files

CSV - comma separated values

#Separated by comma:
1, 2, 3, 4, 4

"ronaldo", "battisti", "teste"

#separated by dot
1. 2. 3. 4


"""
# Possible to do but not recommended - too much work
"""with open('Chapter_18/lutadores.csv', encoding='utf-8') as file:
    data = file.read()
    # print(type(data))
    data = data.split(',')[2:]
    print(data)"""

"""
Python lenguage have 2 different way to work with cvs files;
- reader - to work as list
- DictReader - work as ordered dicts
"""

# reader


'''with open('Chapter_18/lutadores.csv', encoding='utf-8') as file:
    csv_reader = reader(file)
    next(csv_reader)
    for line in csv_reader:
        # Each lina is a list
        print(f"{line[0]} was born in {line[1]} and is {line[2]} tall")'''


# use header to create the key, so it's not necessary to next first line
from csv import DictReader
from csv import reader
with open('Chapter_18/lutadores.csv', encoding='utf-8') as file:
    csv_reader = DictReader(file)
    for line in csv_reader:
        print(
            f"{line['Nome']} was born in {line['País']} and is {line['Altura (em cm)']} tall")

# if the document use a separator different from coma:
# csv_reader = DictReader(file, delimiter=';')
