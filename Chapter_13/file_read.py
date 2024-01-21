'''
file reading

to read a file content in python, use the built-in function open()

open() -> the most simple way, we send a input parameter and return a _io.TextIOWrapper, and we work with it

#OBS: by default, open() opens the file for read.
The file should exist, or wi'll have FileNotFoundError

mode r -> read mode

encoding -> UTF8 -> all special charaters will be interpreted by the program

'''

archive = open('Chapter_13\\text.txt')

#print(archive)

#print(type(archive))

#to read the content of the fyle, use read() function

print(archive.read())
print(archive.read())#nothing happen with a second print
#working with archyves, python use cursor, like when we're writing
#in the end of the fisrt read, the cursor is in the end of the text
#It read all the content of the fyle

print(type(archive.read()))#str