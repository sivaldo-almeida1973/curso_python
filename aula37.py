contador = 0

while contador <= 100:
  contador += 1
  if contador == 6:
    print('nao vou mostrar o 6')
    continue #vai continuar apos o 6

  if contador >= 10 and contador <=27:
    print('nao vou mostrar o ', contador)
    continue

  print(contador)

  if contador == 40:
    break

print('acabou')

