'''
Filter

filter() -> to filter a collection data.
'''
#lib for work with statistcs data
import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
#calculating mean
mean = statistics.mean(data)#calculate mean

#as map function, filter gets 2 parameters - 1 funct and 1 iterable
res = filter(lambda x: x > mean, data)
print(list(res))
#As map function, the data are cleared from memory


##Clear blank spaces
countries = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(None, countries)

print(list(res))

res2 = filter(lambda country: len(country) > 0, countries)

print(list(res2))

res3 = list(map(lambda x: x != '', countries))#return true or false
print(res3)

#Difference between map() and filter():
#map()    -> 2 parameters: 1 funct and 1 iterable | return a obj mapping the funct for each iterable ellement
#filter() -> 2 parameters: 1 funct and 1 iterable | return a obj filtering the ellements according to the function

#complex exemple
users = [
    {"user_name": "Ronaldo", "tweets": ["I love cakes", "I love pizza"]},
    {"user_name": "Smuel", "tweets": ["I love cats"]},
    {"user_name": "Daniela", "tweets": []},
    {"user_name": "Bob", "tweets": []},
    {"user_name": "Diego", "tweets": ["I love dogs", "I will go out"]},
    {"user_name": "Galdemar", "tweets": []}
]

print(users)
#Filter innatible users
inative = list(filter(lambda x: len(x['tweets']) == 0, users))
print(inative)