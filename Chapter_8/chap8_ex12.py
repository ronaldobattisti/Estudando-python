def alg_sum(alg):
    alg = list(str(alg))
    j = 0
    for i in alg:
        j = j+int(i)
    return j


print(alg_sum(123456))