import math

while True:
    num = int(input("Write a number to verify if it's a perfect square: "))
    a = not(bool(math.sqrt(num)%1))
    print(a)