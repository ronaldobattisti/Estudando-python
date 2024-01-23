"""
with block is used to create a work space, where the files are closed after the mannipulation
"""

with open('Chapter_13\\text.txt') as file:
    print(file.readlines())

"""print(file.read())#ValueError, the file is no longer available"""
