'''
high performance list
'''

from collections import deque

# creating deque
deq = deque('geek')
print(deq)

# adding elements
deq.append('y')  # add in the end

print(deq)

deq.appendleft('k')
print(deq)

# removing
print(deq.pop())

print(deq.popleft())

print(deq)
