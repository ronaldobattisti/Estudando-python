dict1 = {}
with open("C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex10/cities.txt") as file:
    text = file.read().split('\n')
    for item in text:
        buffer = item.split(' ')
        population = int(buffer.pop())
        city = ' '.join(buffer)
        print(f'The city {city} have {population} inhabitants')
        dict1.update({city: population})
    dict_sorted = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
    print(dict_sorted)
