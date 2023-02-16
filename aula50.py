"""
Cuidado com dados mútaveis
= - copiado o valor(imutaveis)
= - aponta para o mesmo valor na memoria(mutavel)
"""

nome = "sivaldo"
noutra_variavel = nome
nome = 'Alice'
print(nome)
print(noutra_variavel)


print('='*30)
#dessa forma não estamos copiando a lista
lista_a = ['alice', 'lucas']
lista_b = lista_a
print(lista_b)
lista_a[0] = 'sivaldo'
print(lista_b)



print('='*30)
#dessa forma sim,  estamos copiando a lista usando (copy(
# ))
lista_a = ['Alice', 'Lucas','Sivaldo']
lista_b = lista_a.copy()

lista_a[0] = 'Guti'
print(lista_a)
print(lista_b)


print('='*30)
#For  in com listas

lista = ['Maria','Lucas','Sivaldo','Alice']

for nome in lista:
  print(nome)



print('='*30)

for letra in 'ABC':
  print(letra)