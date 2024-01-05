def draw_line(qnt):
    list1 = []
    for i in range(qnt):
        list1.append('=')
    print(''.join(list1))

val = int(input('Insert the number of signals: '))
draw_line(val)