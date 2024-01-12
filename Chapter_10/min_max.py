'''
Min e Max

max() return the greatest value in a iterable or the greatest of two or more ellements
'''

list1 = [1, 8, 4, 9, 34, 129]
print(max(list1))

dict1 = {'a': 1, 'b': 2, 'c': 8, 'd': 130, 'e': 50}
print(max(dict1))#return the greatest by the key
print(max(dict1.values()))#return the greatest by the value


names = ['Ronaldo', 'Cassio', 'Daniela', 'Tony']
print(max(names))#returns Tony because consider alphabetic order
print(min(names))#returns Cassio...

print(max(names, key=lambda name: len(name)))#return Ronaldo because the lenght of the word
print(min(names, key=lambda name: len(name)))#Return tonu because the lenght

musics = [
    {"music": "sertanejo", "plays": 10},
    {"music": "rock", "plays": 11},
    {"music": "funk", "plays": 9},
    {"music": "pagode", "plays": 8}
]

print(max(musics, key=lambda music: music["plays"]))
print(min(musics, key=lambda music: music["plays"]))

print(max(musics, key=lambda music: music["plays"])["music"])
print(min(musics, key=lambda music: music["plays"])["music"])

buffer = musics[0]
for music in musics:
    if music["plays"] > buffer["plays"]:
        buffer = music
print(buffer)
