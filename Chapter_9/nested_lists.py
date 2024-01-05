'''
List comprehension

we can add ligic conditional structures
'''

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(lists)

print(type(lists))

print(lists[1][2])

'''for row in lists:
    for num in row:
        print(num)'''

#list comprehension

[[print(value) for value in list] for list in lists]

board = [[collumn for collumn in range(1, 4)] for row in range(1, 4)]
print(board)

#plays for hash game

board = [['X' if num % 2 == 0 else '0' for num in range(1, 4)]for row in range(1, 4)]
for row in board:
    print(row)

#generating initial values
board = [['#' for i in range(1, 4)] for j in range(1,4)]
for row in board:
    print(row)