a = 1263
b = 98765

print(a + b)

veta = [veta for veta in str(a)]
vetb = [vetb for vetb in str(b)]
veta.reverse()
vetb.reverse()

c = veta.copy()
c.reverse()
c = int(''.join(c))
d = vetb.copy()
d.reverse()
d = int(''.join(d))

print(c + d)