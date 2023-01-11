"""
Faça um programa que pergunte a hora ao usuário e,baseado
no horario descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

entrada = input('Digite a hora em numeros inteiros:')

try:
   hora = int(entrada)

   if hora >= 0 and hora <= 11:
    print(f'bom dia')
   elif hora >= 12 and hora <= 17:
    print(f'boa tarde')
   elif hora >= 18 and hora <=23:
    print(f'boa noite')

   else:
    print(f'voce não digitou nada,encerrando')

except:
    print('por favor digite um numero inteiro')