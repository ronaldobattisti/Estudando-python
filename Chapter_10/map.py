'''
Map

With map we map the values for a function
'''
import math

def area(r):
    """Calculate a circle area"""
    return math.pi * (r ** 2)
print(area(2))
print(area(2.5))

######################################

radious = [2, 5, 7.1, 0.3, 10, 44]

#common way
areas = []
for r in radious:
    areas.append(area(r))
print(areas)

#lambda way
areas = map(area, radious) #->->->->->->->->->->map pecive 2 values; 1st a value, 2nd a iterable | Return a map object<-<-<-<-<-<-<-<-<-<-<-<-
print(list(areas))#convert to list to print

#using lambda directly
print(list(map(lambda r: math.pi * r ** 2, radious)))#after 1st map, its become empty(in the conversion) - clean the memory

#the map object is like f(a1), f(a2), f(a3), ...

cities = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27),
         ('New York', 28), ('London', 22)]
print(cities)

#we need to show in farenheit
#f = 9/5 * c + 32

c_to_f = lambda data: (data[0], (9/5 * data[1] + 32))
print(list(map(c_to_f, cities)))#map recieve only one parameter
