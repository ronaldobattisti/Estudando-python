print("Digite o valor: ")

valor_total = float(input())
total_desc = valor_total - valor_total*0.1
valor_parcela_3x = valor_total/3
com_vend_vista = total_desc*0.05
com_vend_prazo = valor_total*0.05

print(f"O total a pagar com desconto de 10% é: {total_desc}")
print(f"O valor de cada parcela, se parcelado em 3x, é: {valor_parcela_3x}")
print(f"A comissão do vendedor na venda a vista é: {com_vend_vista}")
print(f"A comissão do vendedor na venda a vista é: {com_vend_prazo}")
