import math

rad = float(input("Insert the radious: "))
calc = lambda rad: 4/3 * math.pi * pow(rad, 3)
print(calc(rad))