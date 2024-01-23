"""
Files opening mode
r -> read only
w -> write only - overwrite existing files
x -> open to write just if the file doesn't exists, if the file exists, generate a FileExistsError
a -> Open to write adding the new content at the END of the file. If the file doesn't exists, create a file.
+ -> Open to update mode - read a write
"""

#'x' exemple
try:
    with open('Chapter_13\\text3.txt', 'x') as file:
        file.write("Content test.\n")
except FileExistsError:
    print('File already exists')
#file.close()

#'a' Exemple - writing in the end of the file
with open ('Chapter_13\\fruits.txt', 'a') as file:#If use 'w', will erase the old content
    while True:
        fruit = input('Write a fruit or "exit" to exit:')
        if fruit != 'exit':
            file.write(fruit + '\n')
        else:
            break
#file.close()

#'a' Exemple - writing in the begining of the file
with open ('Chapter_13\\fruits.txt', 'a+') as file:#If use 'w', will erase the old content
    while True:
        fruit = input('Write a fruit or "exit" to exit:')
        if fruit != 'exit':
            file.seek(0)
            file.write(fruit + '\n')
        else:
            break
