'''
Get data to be processed

'''
def multip(n1, n2, msg): #parameter
    return (n1 + n2) * msg

print(multip(2, 4, 'text ')) #arguments
#print(multip(2, 5, 'msg', 2))#TypeError

#KeyWords arguments
#Be able to use arguments in any order
print(multip(n1 = 1, n2 = 2, msg = 'msg'))