#nome = input("Qual o seu nome? ")
#print(f'o seu nome é {nome=}')

#print(f'A soma de {numero1} + {numero2} é {soma=}:')

#aqui gerou uma concatenação 

print('-')
#para vitar o erro é melhor dessa forma
numero1 = int(input('Digite um numero:'))
numero2 = int(input('Digite outro numero:'))

int_numero1 = int(numero1)
int_numero2 = int(numero2)
soma= int_numero1 + int_numero2
print(f'A soma de {int_numero1} + {int_numero2}  e igual a {soma}:')
