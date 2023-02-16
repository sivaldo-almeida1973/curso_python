#listas em python
#tipo list -Mutavel
#suporta varios valores de qualquer tipo
#conhecimentos reutilizavel - indices e fatiamento
#Metodos uteis: 
# append- Adiciona um item ao final
# insert - adiciona um item no indice escolhido
#Pop - remove no final ou do indice escolhido
#del - apaga um indice
#clear - limpa a lista
#extend- estende a lista
# + - concatena listas
#Metodos Úteis:

#create  read   update     delete
#criar   ler    alterar     apagar = lisat[i]  (CRUD)
#
print('='*30)

#         1  2  3  4   indices
lista = [10,20,30,40]
lista.append('Sivaldo') #adicionar no final
print(lista)



print('='*30)

lista = [10,20,30,40]
lista.append('Sivaldo') #adicionar no final
nome = lista.pop()  #remove o ultimo item
print(lista)



print('='*30)

lista = [10,20,30,40]
lista.append('Sivaldo') #adicionar no final
print(lista, lista.pop()) #nesse remove e mostra

print('='*30)

lista = [10,20,30,40,50]
lista.append('sivaldo')
lista.append(12345)
print(lista)


print('='*30)
#DEL 
lista = [10,20,30,40,50]
lista.append('sivaldo')
lista.append(12345)
del lista[-1]  #remove o ultimo usando indice negativo
print(lista)


print('='*30)
#clear (limpa lista)
lista = [10,20,30,40,50]
lista.append('sivaldo')
lista.append(12345)
del lista[-1] 
lista.clear() #limpar lista
print(lista)


#Insert adiciona usando o indice


print('='*30)
#clear (limpa lista)
lista = [10,20,30,40,50]
lista.append('sivaldo')
lista.append(12345)
del lista[-1] 
lista.insert(0,300) #inserir no indice 0 o numero 300
print(lista)
