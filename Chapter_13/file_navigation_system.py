"""
File Navigation System

To manipulate OS files, we need to import OS module
"""
import os

#getcwd() -> get the current work directory
print(os.getcwd())#return the absolute path

#to change the current directory
os.chdir('..')#go one directory below

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

#we can check if a directory is relative os absolut
print(os.path.isabs('c:/Users/RONAL'))#True
print(os.path.isabs('c:Users/RONAL'))#False

#We can indetify OS with OS module
#print(os.uname_result()) -> not for windows

import sys

print(sys.platform)

#creating a folder in python
os.chdir('c:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13')
print(os.getcwd())
res = os.path.join(os.getcwd(),'Ronaldo')#gets 2 parametes, 1st the actual directory, 2nd the directory that will be joined
os.chdir(res)
print(os.getcwd())

#listing the directorys
os.chdir('c:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado')
#print(os.listdir())

#more datailes
#print(list(os.scandir()))

files = list(os.scandir())
#print(files)

print(dir(files[0].inode()))
print(dir(files[0].is_dir()))
print(dir(files[0].is_file()))
print(dir(files[0].is_symlink())) #Is a symbolik link?
print(dir(files[0].name))
print(dir(files[0].path))
print(dir(files[0].stat()))

#we need to close scandir
files.close()