"""
walrus operator 

variable := expression
"""

from typing import List
name = 'Ronaldo Battisti'
print(name)

# with walrus

print(name := 'Ronaldo Battisti')

print('--------------------------------')

basket: List[str] = []
fruit = input("Input a fruit: ")
while fruit != 'jaca':
    basket.append(fruit)
    fruit = input("Input a fruit: ")

print('--------------------------------')

basket: List[str] = []
while (fruit := input("Input a fruit: ")) != 'jaca':
    basket.append(fruit)
