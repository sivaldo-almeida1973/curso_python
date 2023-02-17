#Introdução ao desempacotamento .
#No empacotamento numero de variaveis tem que ser igual ao de elementos
#se não terá um erro!!
nomes = ['Maria','Sivaldo','Alice','Lucas']

nome1, nome2, nome3, nome4 = nomes
print(nome2)



print('='*30)

nome1, nome2, nome3, nome4 =  ['Maria','Sivaldo','Alice','Lucas']
print(nome2)


#podemos corrigir o erro criando uma variavel(*resto)
print('='*30)

nome1, * resto =  ['Maria','Sivaldo','Alice','Lucas']
print(nome1, resto)


#podemos corrigir o erro criando uma variavel(*_) usando anderline
print('='*30)

nome1, *_ =  ['Maria','Sivaldo','Alice','Lucas']
print(nome1, resto)


#podemos ignorar os outros elementos(_) usando anderline
print('='*30)

_, nome2, _ =  ['Maria','Sivaldo','Alice']
print(nome2)




print('='*30)

nomes = ['Maria','Sivaldo','Alice','Lucas']
print(nomes[2])
