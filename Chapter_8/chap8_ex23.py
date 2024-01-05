def triangle(lines):
    str = []
    for i in range(1, lines+1):
        str = ['*']*i
        print(''.join(str))
    for i in range(lines+1, 1, -1):
        str = ['*']*i
        print(''.join(str))


while True:
    triangle(int(input('Write the number: ')))