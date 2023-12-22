import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)

print(f"{n1} + {n2}: ")
if int(input()) != n1 + n2:
    print(f"Incorreto, a resposta certa é {n1 + n2}")
else:
    print("Correto")
