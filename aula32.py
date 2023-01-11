"""
faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar.Caso o usuario não digite um numero
inteiro , informe que não é.

"""
entrada = input('Digite um numero inteiro: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar: 
          par_impar_texto = 'par'

    print(f'o numero {entrada_int} é {par_impar_texto} ')
else:
    print('este numero não é par')