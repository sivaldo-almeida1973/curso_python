#desempacotamento em chamadas
#de metodos e funções

string = 'ABCD'
lista = ['Maria','Helena',1,2,3,'Eduarda']
tupla = 'python', 'é', 'legal'

#p, b, *_, ap, u = lista
#print(p,u, ap)

#for nome in lista:
 #   print(nome, end=' ', sep=' ')

#print('Maria', 'Helena', 1,2,3, 'Eduarda')
#print(*lista)
#print(*string)
#print(*tupla)

salas =  [
    
    # 0............1
    ['Maria', 'Helena'],  #  0
    # 0............1
    ['Elaine','Alice'] , # 1
    # 0.......   1............2
    ['Lucas', 'João', 'Eduarda',(10,20,30,40,50,)], # 2




]

print(*salas)
print(*salas, sep='\n')