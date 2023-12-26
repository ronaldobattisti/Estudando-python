'''
dict = {'course': 'Python programming'}
print(dict)
print(dict['course'])

print(dict['outro'])#key error
'''
#in dafault dict, if we try to acess a non existing key,
# these key will be created with the default value
#lambda are funct wo name that can or no get a in value

from collections import defaultdict

dict = defaultdict(lambda: 0)
print(dict)

dict['curso'] = 'Python programming'
print(dict)

print(dict['outro'])#don return key error

print(dict)