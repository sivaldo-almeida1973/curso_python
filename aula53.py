#Enumerate para enumerar valores de iteraveis(pegar indices)



print('='*30)
# usando com variavel, enumerate(iterator) só poderá usar o for  uma unica vez
lista = ['Maria','Alice','Lucas','Guti']
lista.append('sivaldo')

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
   print(item) #vai imprimir indice e todos os elementos e uma tupla




#assim podemos usar quantos for for necessario.(sem variavel enumerate
# )
print('='*30)
lista = ['Maria','Alice','Lucas','Guti']
lista.append('sivaldo')


for item in enumerate(lista):
  print(item)
for item in enumerate(lista):
  print(item)




#assim podemos usar quantos for for necessario.(sem variavel enumerate
# )
print('='*30)
lista = ['Maria','Alice','Lucas','Guti']


for item in enumerate(lista):
  indice, nome = item
  print(indice, nome)

#mesmo resultado do de cima
print('='*30)
for indice, nome in enumerate(lista):
  print(indice, nome)