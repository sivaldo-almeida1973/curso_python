'''
calculando primeiro digito do CPF:

'''

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int( digito) * contador_regressivo1
    contador_regressivo1 -= 1
digito = ((resultado_digito_1 * 10) % 11)
digito_1 = digito if digito <= 9 else 0
print(digito_1)
    
