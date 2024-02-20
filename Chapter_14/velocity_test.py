"""
Velocity test with generating expressions



"""

#generators
def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()#generator

print(ge1)

print(next(ge1))
print(next(ge1))

ge2 = (num for num in range(1, 10))

print(ge2)#generation expression

print(next(ge2))
print(next(ge2))

#velocity test
import time

#generator expression

gen_start = time.time()
print(sum(num for num in range(1, 100000000)))
gen_tempo = time.time() - gen_start

gen_start = time.time()
print(sum([num for num in range(1, 100000000)]))
list_tempo = time.time() - gen_start

print(gen_tempo)
print(list_tempo)