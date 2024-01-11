'''
any and all are funcions built-in

return True if all ellements of the iterable are True or if it's empty

'''

###All Return 
print(all([0, 1, 2, 3, 4]))#return false because f the 'zero'
print(all([ 1, 2, 3, 4]))#return True
print(all([]))

names = ['Carlos', 'Cristina', 'Cassiano']
print(all(name[0] == "C" for name in names))

print(all(letter for letter in 'eio' if letter in 'prow'))#True
print([letter for letter in 'eio' if letter in 'prow'])

print(all(num % 2 == 0 for num in [4, 2, 6, 7, 8]))#False
print([num % 2 == 0 for num in [4, 2, 6, 7, 8]])

#any() -> if any element is true, return true, if all elements == False return False | if iterable is empty, return false
print(any(num % 2 == 0 for num in [4, 2, 6, 7, 8]))#True
print([num % 2 == 0 for num in [4, 2, 6, 7, 8]])