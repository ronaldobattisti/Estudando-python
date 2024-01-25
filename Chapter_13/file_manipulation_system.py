"""
File Manipulation system


"""

#Finding out if a directory exists

import os

os.chdir('c:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13')

#relatives paths 
#file
print(os.path.exists('files.txt'))#False
print(os.path.exists('fruits.txt'))#True

#directory
print(os.path.exists('Ronaldo'))#True
print(os.path.exists('teste'))#False

#Absolute path
print(os.path.exists('c:/users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_4'))#True

#Not the best way to create a file
#1 -> to create a file
open('text.txt', 'w').close()
"""#2 -> to create a file
open('Test_file2.txt', 'a').close()
#3 -> to create a file
with open('Test_file3.txt', 'w') as file:
    pass#to do nothing"""

"""#best way to create a file #don't work in windows
os.mkdir('Test_file4.txt')"""

#if the file already exists, FileExistError

#to create directoryes
#os.mkdir('templates')

os.makedirs('new', exist_ok=True)#ignore if exists

#to create directories in directorues that doesn't exists
os.makedirs('temp0/temp1/temp2/temp3/temp4')

#To rename a file
os.rename('new', 'newest')  #If directory doens't exists FileNotFoundError
                                    #If the directory isn't void, OsError

#to change the name with the full path:
os.makedirs('new/new', exist_ok=True)#ignore if exists
os.rename('new/new', 'new/newest2')

#removing files
os.remove('text.txt')

#removing directoryes, the don't go to the bin, they vanish
os.rmdir('newest')
os.rmdir('new/newest2')
os.rmdir('new')

os.removedirs('temp0/temp1/temp2/temp3/temp4')

#If the fole doesn't exists : FileNotFoundError

#To remove al content from directory (tree directory)
'''for file in os.scandir('temp0'):
    if file.is_file():
        os.remove(file.path)
    if not file.is_file():
        os.rmdir(file.path)'''

import tempfile

#WO if block
file = tempfile.TemporaryFile()
file.write(b'Ronaldo Battisti\n')
file.seek(0)
print(file.read())
file.close()#temporary file desapears

#
file = tempfile.NamedTemporaryFile()
file.write(b"Ronaldo Battisti\n")#b from bits
print(file.name)
print(file.read())
file.close()