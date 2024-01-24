"""
StringIO

To read or write data in OS files, the software needs permission
     read permission
     write permission

StringIO -> Used to create files in memory
"""

from io import StringIO
msg = "This is just a normal string"
#We can create a file in memorywith a string or void, to insert than
file = StringIO(msg)#THis is equivalent to file = open('file.txt', 'w')

#Now we can use everything we know
print(file.read())

file.write("\nAnother text")
file.seek(0)
print(file.read())