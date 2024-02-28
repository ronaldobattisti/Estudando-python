"""
In POO

Classes are models of real life objects being represented computationally

imagine that you want to make a system to manage the lamps in your home

Classes can contain:
    * Attributes -  Representing tha object characteristics. With attributes we can reproduce the state of the object
                    In the lamp case we probably want to know its voltage, its color, its luminosity, is it on or of, etc...
    * Methods -     Functions that represent the behavior of the object, the actions that this object can realize in the system
                    In the lamp exemple, it's like turn the lamp on or off
    
#when we name a class in python, we use first class upper case, ex:
class DemoTest():
    pass
#native python classes are lower case ti easily identify who is python native
    
In JAVA, the class name should be the main file mane. In Python it's not necessary

When we are plannin a software and defining the classes, we call these objects that will be mapped as classes of entities
"""


class Lamp:
    pass  # Use this word when we have a not implemented code block yet


age = 32  # Type int
price = 35.2  # Type float
name = 'Ronaldo'  # Type string

lamp = Lamp()
print(type(lamp))  # Type Lamp
