'''
Introdução ao tr/except
except -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero_str = input('Vou dobrar o número que você digitar: ')
try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f' o dobro de {numero_str} é {numero_float * 2:.2f} ')
except:
    print('isso não é um número')



#if numero_str.isdigit():
#     numero_float = float(numero_str)
#    print(f' o dobro de {numero_str} é {numero_float# * #2:.2f} ')
#else:
#   print('isso não é um número')

print(numero_str.isdigit())