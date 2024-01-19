'''
module - just a python archyve that could have many functions

packages - a folder containing a module collections

in the 2.x version was obligatory the using of __init__.py

3.x version isn't, but still being used for compatibility

'''

from test_package import geek1, geek2

from test_package.test_package_2 import geek3, geek4

print(geek1.pi)
print(geek1.fun1(1, 2))

print(geek2.course)
print(geek2.fun2())

print(geek3.fun3())

print(geek4.fun4())