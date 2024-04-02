import statistics
import math

nuns = [2, 3, 4, 5]

print(math.prod(nuns))
print('---------------------')
print(math.isqrt(10))
print(math.sqrt(10))

print('---------------------')
p1 = (12, 50, 40)
p2 = (6, 7, 13)

print(math.dist(p1, p2))
print('---------------------')

print(math.hypot(*p1))  # the '*' is used to npack the container
print('---------------------')

values = [1.45, 1.864, 1.682]
print(statistics.fmean(values))

print('---------------------')
seq1 = 'Ronaldo Battisti'
seq2 = [1, 2, 3, 1, 3, 4, 9, 8, 7, 2, 2, 2, 5, 4]
print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
