
#listas em python
#tipo list -Mutavel
#suporta varios valores de qualquer tipo
#conhecimentos reutilizavel - indices e fatiamento
#Metodos uteis: append , insert , pop, del, clear , extend, +
#Metodos Úteis:

#create  read   update     delete
#criar   ler    alterar     apagar = lisat[i]  (CRUD)
print('='*30)

#alterar ou substituir  usando indice
lista = [10,20,30,40]
lista[2] = 300   #trocar 300 no indice 2 por (30)
print(lista)
print(lista[2])

print('='*30)
#apagar ou deletar  usando indice
lista = [10,20,30,40]
lista[2] = 300  
del lista[2] 
print(lista)
print(lista[2])

print('='*30)
# usando o Append para inserir itens na lista
lista = [15,20,25,30,35,40]
lista.append(45)
lista.append(50)
lista.append(55)
lista.append(60)
print(lista)


#remover o ultimo elemento usando (pop)

print('='*30)
lista = [15,20,25,30,35,40]
lista.append(45)
lista.pop()    #vai remover o 45
lista.append(50)
lista.append(55)
lista.append(60)
ultimo_valor = lista.pop()  #remove o 60

print(lista, 'removido', ultimo_valor)


#u

#remover o ultimo elemento usando (pop)

print('='*30)
lista = [15,20,25,30,35,40]
lista.append(45)
lista.pop()    #vai remover o 45
lista.append(50)
lista.append(55)
lista.append(60)
ultimo_valor = lista.pop(3)  #remove usando indice

print(lista, 'removido', ultimo_valor)