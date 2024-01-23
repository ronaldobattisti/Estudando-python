'''
Seek and cursors

seek() is used to move the cursor through the file
'''

file = open('Chapter_13\\text.txt')
'''text = file.read()
print(text)

#if we want to print the text twice
#Moving he coursor through the file with seek
file.seek(0)# -> send the cursor to te position 0
text = file.read()
print(text)'''

"""#for read line by line: one print per line
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())"""

#readlines() -> just read lines with content
print(file.readlines())

#when we open a file with open() funct, a connection betwee the file and our computer is created, It's called streaming
#in the end of the work, this connection should be closed()
#steps to work with a fila
#1 -> Open fila
#2 -> Work the file
#3 -> close the file

#1
file = open('Chapter_13\\text.txt')

#2
text = file.read()

print(file.closed)#boolean that verifies if the file is opened or closed

#3
file.close()

print(file.closed)#if you try to work yith a closed file, ValueError