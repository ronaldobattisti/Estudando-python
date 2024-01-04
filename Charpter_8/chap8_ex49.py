def is_square(matrix):
    if len(matrix) == len(matrix[1]):
        return True
    return False

def sum_main_diagonal(matrix):
    if is_square(matrix):
        sum = 0
        for ind, row in enumerate(matrix):
            sum += matrix[ind][ind]
        return sum
    return False

def sum_under_main_diagonal(matrix):
    if is_square(matrix):
        sum = 0
        for ind, row in enumerate(matrix):
            for i in range(0, ind+1):
                sum += matrix[ind][i]
        return sum
    return False

m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print(sum_main_diagonal(m1))
print(sum_under_main_diagonal(m1))