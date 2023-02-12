
#iterando strings com while(qual letra apareceu mas vezes na frase?)

frase = 'O Python é uma linguagem de programação'\
  'Multiparadigma.'\
    'Python foi criado por Guido van Rossum.'.upper() #tudo maiusculas

print(frase)
print(frase.count('Python'))

#quantas vezes apareceu Python na frase?
print('-'*30)
frase = 'O Python é uma linguagem de programação'\
  'Multiparadigma.'\
    'Python foi criado por Guido van Rossum.'


print(frase.count('Python'))




#Qual letra apareceu mais na frase?
print('-'*30)
frase ='aaaooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
  letra_atual = frase[i]


  if letra_atual == ' ':
    i += 1
    continue

  qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

  if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
    qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
    letra_apareceu_mais_vezes = letra_atual

  i += 1

print('A letra que apareceu mais vezes foi o: '
      f'"{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_apareceu_mais_vezes} X' )

