"""
Writing in files

OBS: When opening a file to read, we cant write in it
On the other side, when opwning a file to write, we can't read

If the file doesn't exists, it'll be created

Opening a file to write with W parameter, if the file does not exists, it will be created, if it exists will be overwritten
"""

with open('Chapter_13\\new.txt', 'w') as file:
    file.write('New data\n')#Argument of write() should be str(TypeError)
    file.write('We can add as much lines want\n')
    file.write('Last line')

with open('Chapter_13\\text2.txt', 'w') as file:
    file.write('Ronaldo\n' * 1000)

with open('Chapter_13\\Fruits.txt', 'w') as file:
    while True:
        fruit = input("Write a fruit or type \'out\':")
        if fruit != 'out':
            file.write(fruit + '\n')
        else:
            break