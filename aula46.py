""""
listas em python
tipo list -Mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizavel - indices e fatiamento
Metodos uteis: append , insert , pop, del, clear , extend, +
"""

# +01234
# -54321
 
string = 'ABCDE' #5 caracteres (len)
lista = []  # string vazia
print(lista, type(lista))


print('='*30)


lista = []  # string vazia
print(bool(lista))  # bool false
#print(lista, type(lista))


print('='*30)

#         0     1         2           3     4   -indice positivos
#        -5    -4        -3          -2    -1   -indice negativos
lista = [123, True, 'Sivaldo Vieira', 1.2, []]  
print(lista)  # traz toda lista
print(lista[2]) # sivaldo vieira
print(lista[-4]) #True
print(lista[2].upper(), type(lista[2])) #traz tudo maiusculas e o tipo 



# alterar itens na lista
print('='*30)

#         0     1         2           3     4   -indice positivos
#        -5    -4        -3          -2    -1   -indice negativos
lista = [123, True, 'Sivaldo Vieira', 1.2, []]  

lista[2]  = 'Lucas Almeida'  # substituir (sivaldo )por( luacs)
print(lista)  # traz toda lista