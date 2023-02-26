"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
http://en.wikipedia.org/wiki/double-precision_floating-point
https://docs.python.org/pt-br/3/tutorial/floatingpoint.tmhl
"""
#numero_1 = 0.1
#numero_2 = 0.7
#numero_3 = numero_1 + numero_2
#print(numero_3)
#print(f'{numero_3:.2f}')
#print(type(round(numero_3, 2))) #formata numeros(round) arredonda



print('='*30)
import decimal
#tem a mesma função dos de cima so que mas completa.
#corrige imprecisão de numeros float

numero_1 = decimal.Decimal('0.1')# tem que converter em str
numero_2 = decimal.Decimal('0.7') # tem que converter em str
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
print(type(round(numero_3, 2))) #formata numeros(round) arredonda