import math

withdraw = int(input("Valor do saque: "))

buf_withdraw = withdraw



while buf_withdraw > 0:
    if buf_withdraw >= 50:
        quant_50 = math.floor(buf_withdraw / 50)
        buf_withdraw = buf_withdraw % 50
        print(f"Notas de 50: {quant_50}")
    elif buf_withdraw >= 20:
        quant_20 = math.floor(buf_withdraw / 20)
        buf_withdraw = buf_withdraw % 20
        print(f"Notas de 20: {quant_20}")
    elif buf_withdraw >= 10:
        quant_10 = math.floor(buf_withdraw / 10)
        buf_withdraw = buf_withdraw % 10
        print(f"Notas de 10: {quant_10}")
    elif buf_withdraw >= 5:
        quant_5 = math.floor(buf_withdraw / 5)
        buf_withdraw = buf_withdraw % 5
        print(f"Notas de 5: {quant_5}")
    elif buf_withdraw >= 2:
        quant_2 = math.floor(buf_withdraw / 2)
        buf_withdraw = buf_withdraw % 2
        print(f"Notas de 2: {quant_2}")
    elif buf_withdraw >= 1:
        quant_1 = math.floor(buf_withdraw / 1)
        buf_withdraw = buf_withdraw % 1
        print(f"Notas de 1: {quant_1}")