"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::] _____i(indice) f(fim)  p(passos)
Obs.: a função len retorna a qtd
de carateres da str,
"""

variavel = 'Olá mundo'
print(variavel [4:])# toda variavel
print(variavel [0:9:2])# do 0 ate o 9 de 2 em 2
print(variavel [::-1])# do 0 ate o 9 de invertido
print(variavel [-1:-10:-1])# do 0 ate o 9 de invertido
print(len(variavel))# quantas letras
print(variavel[-1])#ultima letra