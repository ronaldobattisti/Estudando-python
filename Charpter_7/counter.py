'''
Collection Module - Counter

Collection -> High-performance Container Datetypes

Counter -> recieve a iterable as parameter and create a Collections Couter 
obj like a dictionary 
'''
#ex1
#using counter
from collections import Counter
#coul be any iterable9tuple, dict, string, etc
list1 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 4, 5, 3, 45, 66, 66, 66, 43, 34]

res = Counter(list1)
print(res)
print(type(res))#like dict - for each list ellement, couter create a key anda a value

#ex2
print(Counter('Geek University'))

#ex3
text = """Marseille, de ascendência huguenote francesa, juntou-se à Luftwaffe em 1938. 
Aos 20 anos formou-se em uma das escolas de pilotos de caça da Luftwaffe a tempo de 
participar da Batalha da Grã-Bretanha, sem sucesso notável. Tinha uma vida noturna 
tão agitada que às vezes ficava cansado demais para poder voar na manhã seguinte. 
Como resultado da falta de disciplina, foi transferido para o Jagdgeschwader 27 
(JG 27), que se mudou para o Norte da África em abril de 1941"""
words = text.split()
#print(words)
res = Counter(words)
print(res)
print(res.most_common(5))