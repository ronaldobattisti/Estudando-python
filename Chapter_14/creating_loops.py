"""
Creating our own loop version



"""

for num in [1, 2, 3, 4, 5]:#from under the cover,python do: iter([1, 2, 3, 4, 5]) and use next()
    print(num)



def my_for(iterab):
    it = iter(iterab)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

my_for("Ronaldo Battisti")