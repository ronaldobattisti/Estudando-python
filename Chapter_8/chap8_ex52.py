def is_square(matrix):
    if len(matrix) == len(matrix[1]):
        return True
    return False

def transpose(m1):
    m2 = [[element for element in row] for row in m1]
    for row in range(0, len(m1)):
        for collumn in range(0, len(m1[1])):
            print(m1[row][collumn])
            m2[collumn][row] = m1[row][collumn]
    return(m2)

m1 = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

m2 = transpose(m1)
for row in m1:
    print(row)
for row in m2:
    print(row)