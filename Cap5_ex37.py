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
        if year % 4 == 0 and year % 100 != 0 or year % 100 == 0 and year % 400 == 0:  ###Testa se é ano bissexto###
            return 29
        else:
            return 28

def validade_data_input(day_in, month_in, year_in, hour_in, minute_in, day_out, month_out, year_out, hour_out, minute_out):
    data_atual = datetime.now()
    if year_in == data_atual.year and month_in == data_atual.month and day_in == data_atual.day:
        if year_in == year_out:
            if month_in == month_out:
                if day_in == day_out:
                    if hour_in == hour_out:
                        if minute_in < minute_out:
                            return 1  # Retorna 1 quando uma data é possível
                        else:
                            return 0  # Retorna 0 quando uma data é impossível
                    elif hour_in < hour_out:
                        return 1
                    else:
                        return 0
                elif day_in < day_out:
                    return 1
                else: 
                    return 0
            elif month_in < month_out:
                return 1
            else:
                return 0


def tempo_estacionado(day_in, month_in, year_in, hour_in, minute_in, day_out, month_out, year_out, hour_out, minute_out):
    if year_in == year_out:
        if month_in == month_out:
            if day_in == day_out:
                if hour_in == hour_out:
                    if minute_in == minute_out:
                        print(
                            "Valor não admissível, datas iguais de entrada e de saída.")
                    else:
                        tempoEstacionado = minute_out - minute_in
                else:
                    tempoEstacionado = (hour_out - hour_in) * \
                        60 + minute_out - minute_in
            elif day_out - day_in == 1:  # Testa se saiu no dia posterior ao da entrada###
                tempoEstacionado = (hour_out + 24 - hour_in) * \
                    60 + minute_out - minute_in
            else:
                tempoEstacionado = (day_out - day_in - 1) * 24 * 60 + \
                    (hour_out + 24 - hour_in) * 60 + minute_out - minute_in
        elif month_in > month_out:
            print("Valor não admissível, mês de entrada posterior ao mês de saída.")
        elif month_out - month_in == 1:  # testa se saiu no mês posterior ao da entrada###
            tempoEstacionado = (day_out + verifica_dias_mes(month_in, year_in) - day_in - 1) * \
                24 * 60 + (hour_out + 24 - hour_in) * 60 + minute_out - minute_in
    else:
        return 0
    return tempoEstacionado  # retorna o tempo estacionado em minutos###


while True:
    date_in = input("Escreva a data de entrada(dd/mm/yyyy): ")
    day_in, month_in, year_in = testa_data(date_in)
    time_in = input("Escreva o horário de entrada(hh:mm):")
    hour_in, minute_in = testa_hora(time_in)
    print(
        f"Entrada \nDia: {day_in}/{month_in}/{year_in}\nHorário: {hour_in}:{minute_in}")

    date_out = input("Escreva a data de saída(dd/mm/yyyy): ")
    day_out, month_out, year_out = testa_data(date_out)
    time_out = input("Escreva o horário de saída(hh:mm):")
    hour_out, minute_out = testa_hora(time_out)
    print(
        f"Saída \nDia: {day_out}/{month_out}/{year_out}\nHorário: {hour_out}:{minute_out}")

    tempo_estacionado = tempo_estacionado(
        day_in, month_in, year_in, hour_in, minute_in, day_out, month_out, year_out, hour_out, minute_out)
    horas_estacionado = int(tempo_estacionado) / 60
    print(f"O tempo estacionado foi {tempo_estacionado}")
