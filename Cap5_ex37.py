from datetime import datetime


def testa_data(date):
    day = int(date[0]) * 10 + int(date[1])
    month = int(date[3]) * 10 + int(date[4])
    year = int(date[6]) * 1000 + int(date[7]) * \
        100 + int(date[8]) * 10 + int(date[9])
    return day, month, year


def testa_hora(time):
    hour = int(time[0]) * 10 + int(time[1])
    minute = int(time[3]) * 10 + int(time[4])
    return (hour, minute)


def verifica_dias_mes(mes, year):
    if mes != 2:
        if mes % 2 != 0:
            return 31
        else:
            return 30
    else:
        if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:  # Testa se é ano bissexto###
            return 29
        else:
            return 28


def validade_data_input(dayIn, monthIn, yearIn, hourIn, minuteIn, dayOut, monthOut, yearOut, hourOut, minuteOut):
    data_atual = datetime.now()
    if yearIn == data_atual.year and monthIn == data_atual.month and dayIn == data_atual.day:
        if yearIn == yearOut:
            if monthIn == monthOut:
                if dayIn == dayOut:
                    if hourIn == hourOut:
                        if minuteIn < minuteOut:
                            return 1  # Retorna 1 quando uma data é possível
                        else:
                            return 0  # Retorna 0 quando uma data é impossível
                    elif hourIn < hourOut:
                        return 1
                    else:
                        return 0


def tempo_estacionado(dayIn, monthIn, yearIn, hourIn, minuteIn, dayOut, monthOut, yearOut, hourOut, minuteOut):
    if yearIn == yearOut:
        if monthIn == monthOut:
            if dayIn == dayOut:
                if hourIn == hourOut:
                    if minuteIn == minuteOut:
                        print(
                            "Valor não admissível, datas iguais de entrada e de saída.")
                    else:
                        tempoEstacionado = minuteOut - minuteIn
                else:
                    tempoEstacionado = (hourOut - hourIn) * \
                        60 + minuteOut - minuteIn
            elif dayOut - dayIn == 1:  # Testa se saiu no dia posterior ao da entrada###
                tempoEstacionado = (hourOut + 24 - hourIn) * \
                    60 + minuteOut - minuteIn
            else:
                tempoEstacionado = (dayOut - dayIn - 1) * 24 * 60 + \
                    (hourOut + 24 - hourIn) * 60 + minuteOut - minuteIn
        elif monthIn > monthOut:
            print("Valor não admissível, mês de entrada posterior ao mês de saída.")
        elif monthOut - monthIn == 1:  # testa se saiu no mês posterior ao da entrada###
            tempoEstacionado = (dayOut + verifica_dias_mes(monthIn, yearIn) - dayIn - 1) * \
                24 * 60 + (hourOut + 24 - hourIn) * 60 + minuteOut - minuteIn
    else:
        return 0
    return tempoEstacionado  # retorna o tempo estacionado em minutos###


while True:
    dateIn = input("Escreva a data de entrada(dd/mm/yyyy): ")
    dayIn, monthIn, yearIn = testa_data(dateIn)
    timeIn = input("Escreva o horário de entrada(hh:mm):")
    hourIn, minuteIn = testa_hora(timeIn)
    print(
        f"Entrada \nDia: {dayIn}/{monthIn}/{yearIn}\nHorário: {hourIn}:{minuteIn}")

    dateOut = input("Escreva a data de saída(dd/mm/yyyy): ")
    dayOut, monthOut, yearOut = testa_data(dateOut)
    timeOut = input("Escreva o horário de saída(hh:mm):")
    hourOut, minuteOut = testa_hora(timeOut)
    print(
        f"Saída \nDia: {dayOut}/{monthOut}/{yearOut}\nHorário: {hourOut}:{minuteOut}")

    tempoEstacionado = tempo_estacionado(
        dayIn, monthIn, yearIn, hourIn, minuteIn, dayOut, monthOut, yearOut, hourOut, minuteOut)
    horasEstacionado = int(tempoEstacionado) / 60
    print(f"O tempo estacionado foi {tempoEstacionado}")
