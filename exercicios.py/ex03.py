"""
Faça um programa que pergunte a hora ao usuario e, baseando_se no horario
descrito, exiba a saudação apropriada.
Ex:bom dia 0-11, boa tarde 12-17, boa noite 18-23.
"""

entrada = input('Digite a hora atual em numero inteiros:')

try:
  hora = int(entrada)
  if hora >= 0 and hora <= 11:
    print('Bom dia')
  elif hora >= 12 and hora <=17:
    print('Boa tarde')
  elif hora >= 18 and hora <= 23:
    print('Boa noite')
  else:
    print('Não conheço essa hora!!')
except:
  print('Por favor ,digite apenas numeros inteiros!!')