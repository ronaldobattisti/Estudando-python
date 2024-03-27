"""
In python we use reserved word "assert" to check if a expression is valid or no
If true, assert return none
if false, raise AssertionError

# we can specify a second argument or a personalized error message

# asser coul be user in any funct or code, don't need to use just in test

--->Warning<---
If a python program is executed with '-o' parameter, none assertion will be validated
"""
"""
assert 4 == 4
assert 4 == 2, "4 isn't equal 2"
"""


def sum_pos_num(a, b):
    assert a > 0 and b > 0, 'Both should be positive'
    return a + b


print(sum_pos_num(2, 4))
# print(sum_pos_num(-2, 4))


def eat_fast_food(food):
    assert food in [
        'pizza',
        'icecream',
        'hot dog'
    ], 'Food should be a fast food'
    return food


print(eat_fast_food('pizza'))
print(eat_fast_food('carrot'))

print('---------------------')

# WARNING: caution using assert use try
