"""
range + for para usar intervalos de numeros
range -> range(start vira 0, stop , step vira 1)

"""
#numeros = range(10) #stop  (começa no 0 para 9)
#numeros = range(5,10)# start (começa no 5 ate 9)
#numeros = range(5,10,2) #step (de quanto em quanto)
#print(numeros)



numeros = range(10) #step (de quanto em quanto)

for numero in numeros:
  print(numero)


print('-'*30)
numeros = range(5,10) #stop (do cinco ate 10)

for numero in numeros:
  print(numero)


print('-'*30)
numeros = range(5,10,2) #step (de quanto em quanto)

for numero in numeros:
  print(numero)

print('-'*30)
numeros = range(0,100,4) #step (de quanto em quanto)

for numero in numeros:
  print(numero)


print('-'*30)
numeros = range(0,-10,-1) #step (de quanto em quanto negativo)

for numero in numeros:
  print(numero)


print('-'*30)
numeros = range(-5,-10,-1) #step (de quanto em quanto negativo)

for numero in numeros:
  print(numero)