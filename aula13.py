nome = 'Alice Moraes'
altura = 1.60
peso = 64
imc = peso / altura ** 2


# f-strings (formatação)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f} '


print(linha_1)
print(linha_2)
print(linha_3)