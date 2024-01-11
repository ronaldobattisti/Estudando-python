'''
do not confuse with sort, from list.

As it name says, sorted() is to order
'''

list1 = [1, 8, 5, 4, 6, 2]
list1.sort()#Just works with list
print(list1)
#ord_list = list.sort({1, 8, 5, 4, 6, 2})
#print(ord_list)
#ord_list = list.sort((1, 8, 5, 4, 6, 2))
#print(ord_list)

ord_list = sorted([1, 8, 5, 4, 6, 2])
print(ord_list)
ord_list = sorted({1, 8, 5, 4, 6, 2})#works eith tuple - return list
print(ord_list)
ord_list = sorted((1, 8, 5, 4, 6, 2))#works with set - return list
print(ord_list)

#adding parameters
ord_list = sorted((1, 8, 5, 4, 6, 2), reverse=True)#works with set - return list
print(ord_list)

#we can use sorted() for more complex things
users = [
    {"user_name": "Ronaldo", "tweets": ["I love cakes", "I love pizza"]},
    {"user_name": "Smuel", "tweets": ["I love cats"]},
    {"user_name": "Daniela", "tweets": []},
    {"user_name": "Bob", "tweets": []},
    {"user_name": "Diego", "tweets": ["I love dogs", "I will go out"]},
    {"user_name": "Galdemar", "tweets": []}
]

print(users)

#ordering by name - alphabetic
print(sorted(users, key=lambda user: user["user_name"]))

#ordering by number of tweets
print(sorted(users, key=lambda user: len(user['tweets']))) #from lower to higher

musics = [
    {"music": "sertanejo", "plays": 10},
    {"music": "rock", "plays": 11},
    {"music": "funk", "plays": 9},
    {"music": "pagode", "plays": 8}
]

print(sorted(musics, key=lambda music: music["plays"]))#always generate a new list