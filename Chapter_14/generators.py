"""
We saw that:

- Generators are Iterators;

contrary isn't true, not all iterator is a generator

-Generators could be created with generatig functions
-Generating functions use Yield word
-Generators could be created with generating expressions

Differences between functions and generating functions
--------------------------------------------------------------------------------------------|
|Functions                                          |Generator Functions                    |
--------------------------------------------------------------------------------------------|                  
|Use 'return'                                       |Use 'yield'                            |
|Return once                                        |Could use 'yield' many times           |
|When runned, return 1 value                        |When runned, return a generator        |
|-------------------------------------------------------------------------------------------|

"""

#exemple of gererator function (it's not a generator, but generate a generator)

def count_to(num):
    cont = 1
    while cont <= num:
        yield cont      #different from the 'return', 'yield' don't quit the loop and wait a 'next'
        cont += 1

gen = count_to(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = count_to(10)

for num in gen:
    print(num)