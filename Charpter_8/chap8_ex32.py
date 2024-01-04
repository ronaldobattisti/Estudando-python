def simplify(n1, n2):
    div = 1
    n=0
    if n1>=n2:
        n=n1
    else:
        n=n2
    for i in range(2, n):
        if n1 % i == 0 and n2 % i == 0:
            div = i
            break
    return(div)


while True:
    n1 = int(input('write the nominator: '))
    n2 = int(input('write the denominator: '))
    div = simplify(n1,n1)
    print(f'The value simplified is {int(n1/div)}/{int(n2/div)}')