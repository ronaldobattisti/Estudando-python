"""

"""

import datetime

today = datetime.datetime.now()

event = datetime.datetime(2025, 3, 3, 0)

least = event - today

print(repr(least))
print(least)
# printing just days
print(least.days)


print('---------------------------------------')
buy_date = datetime.datetime.now()
ticket_rule = datetime.timedelta(days=3)
ticket_expiration = buy_date + ticket_rule