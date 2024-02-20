"""
memory test with generators

"""


#funct using list = 400mb
def fib_list(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

#test
"""for n in fib_list(100000):
    print(n)"""

#funct using gen
def fib_gen(max):
    a, b, cont = 0, 1, 0
    while cont < max:
        a, b = b, a + b
        yield a
        cont += 1

for n in fib_gen(100000):
    print(n)