"""
writing a custom iterator

"""



'''for n in range(11):
    print(n)'''

class Counter:
    def __init__(self, smallest, higher):
        self.smallest = smallest
        self.higher = higher
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.smallest < self.higher:
            number = self.smallest
            self.smallest += 1
            return number
        raise StopIteration

con = Counter(1, 6)
print(con)

it = iter(con)

for n in Counter(1, 61):
    print(n)
