#Tipos de Tuplas - São listas imutaveis
#tuplas usa parenteses ou não!
#para inserir valores em uma tupla tem que transformar em um lista
#nesse caso é melhor criar uma lista

nomes =( 'Maria','Alice','Lucas')
print(nomes[1])
print(nomes)


#podemos converter uma lista para uma (tupla)

nomes = ['Maria','Alice','Lucas'] #lista
nomes = tuple(nomes) #converte para tupla
print(nomes[1])
print(nomes)

#podemos converter uma tupla para uma (lista)

nomes = ('Maria','Alice','Lucas') #lista
nomes = list(nomes) #converte para tupla
print(nomes[1])


nomes = ['Maria','Alice','Lucas'] #lista

print(nomes[1])
print(nomes)