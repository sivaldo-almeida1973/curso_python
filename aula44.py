"""
Iterarvel -> str , range , etc  (metodo(__iter__)) entrega uma coisapor vez
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o proximo valor
iter -> me entrega seu iterador
"""
#esses comandos print(next(texto)) e print(texto.__next__())
texto = iter('lucas')  #__iter__()

print(texto.__next__())
print(next(texto))

print(next(texto))
print(next(texto))


print('-'*30)


#For letra in texto

#texto = 'sivaldo' #iteravel
#iterador = iter(texto)  #itrator

#while True:
 # try:
    # letra = next(iterador)
   #  print(letra)
 # except StopAsyncIteration:
    #  break
texto = 'sivaldo'
for letra in texto:
  print(letra)